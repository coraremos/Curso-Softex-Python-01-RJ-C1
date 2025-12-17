from rest_framework import serializers 
from django.contrib.auth.models import User, Group
from .models import Tarefa 
from datetime import date, datetime
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
 
class TarefaSerializer(serializers.ModelSerializer): 
    """ 
    Serializer para o Model Tarefa. 
     
    Responsabilidades: 
    1. Converter Tarefa → JSON (serialização) 
    2. Converter JSON → Tarefa (desserialização) 
    3. Validar dados de entrada 
    """ 

    # Mostra o username do usuário em vez do ID (read-only na saída)
    user = serializers.StringRelatedField(read_only=True)

    class Meta: 
        model = Tarefa
        fields = [
            'id', 
            'user',
            'titulo', 
            'concluida', 
            'prioridade', 
            'prazo', 
            'deletada', 
            'criada_em', 
            'concluida_em'
        ]
        read_only_fields = [
            'id', 
            'user',
            'criada_em', 
            'deletada', 
            'concluida_em'
        ]
        
    
    def validate_titulo(self, value):
        """Impedir títulos duplicados para o mesmo usuário."""
        if 'request' in self.context and hasattr(self.context['request'], 'user'):
            user = self.context['request'].user
            if user and user.is_authenticated:
                if Tarefa.objects.filter(user=user, titulo=value).exists():
                    raise serializers.ValidationError("Você já tem uma tarefa com este título.")
        return value

    def validate_prazo(self, value):
        if value and value < date.today():
            raise serializers.ValidationError("O prazo não pode ser uma data no passado.")
        return value

    def validate(self, data):
        concluida = data.get('concluida', False)
        prazo = data.get('prazo')

        if not concluida and not prazo:
            raise serializers.ValidationError({
                "prazo": "O prazo é obrigatório para tarefas pendentes (não concluídas)."
            })
        
        request = self.context.get('request')
        instance = self.instance
        
        if instance and request and 'concluida' in data:
            if request.method == 'PATCH':
                if instance.prioridade == 'alta' and data['concluida'] is True:
                    raise serializers.ValidationError({
                        "concluida": "Tarefas de prioridade 'alta' só podem ser concluídas via PUT para garantir a revisão completa dos campos."
                    })
        
        return data


    def update(self, instance, validated_data):

        if 'concluida' in validated_data:
            nova_concluida = validated_data['concluida']
            
            if nova_concluida and not instance.concluida:
                validated_data['concluida_em'] = datetime.now()
                
            elif not nova_concluida and instance.concluida:
                validated_data['concluida_em'] = None

        return super().update(instance, validated_data)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer): 
    @classmethod     
    def get_token(cls, user):         
        token = super().get_token(user)

        # Adicionar campos customizados ao payload         
        token['username'] = user.username         
        token['email'] = user.email         
        token['is_staff'] = user.is_staff     

        return token

class UserRegistrationSerializer(serializers.ModelSerializer):     
    """
    Serializer para cadastro de novos usuários.
        
    Funcionalidades:
    1. Aceita senha na entrada (write_only)
    2. Oculta senha na saída (nunca retorna em JSON)
    3. Aplica hashing automático (create_user)
    """
      
    password = serializers.CharField(        
        write_only=True, #ampo aceito no POST, mas NUNCA retornado no GET
        required=True,         
        style={'input_type': 'password'},
        min_length=8, # Segurança: mínimo 8 caracteres
        help_text="Senha com no mínimo 8 caracteres"
    )      

    # Campo extra para confirmação (opcional, mas recomendado)
    password_confirm = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
)

    class Meta:         
        model = User         
        fields = ['username', 'email', 'password', 'password_confirm']
        read_only_fields = ['id']
        extra_kwargs = {
            'email': {'required': True} # Tornar email obrigatório
        }

    def create(self, validated_data):         
        """         
        Intercepta a criação para usar o 'create_user' e hashear a senha.         
        """       
        #Remove campo extra
        validated_data.pop('password_confirm')   
        # Extrai a senha dos dados validados         
        password = validated_data.pop('password')                  
        # Extrai email e username        
        email = validated_data.get('email', '')         
        username = validated_data['username']          

        # Cria usuário usando o método seguro do Django         
        user = User.objects.create_user(             
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=password
        )         

        try:             
            # Busca o grupo 'Comum'
            grupo_comum = Group.objects.get(name='Comum')
            # Adiciona o usuário ao grupo
            user.groups.add(grupo_comum)
        except Group.DoesNotExist:
            # Fallback: Se o grupo não existir, o usuário é criado sem grupo.             
            # Em produção, use logging.error() aqui.             
            pass
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    model = User
    fields = ['username', 'email']
    read_only_fields = ['email']