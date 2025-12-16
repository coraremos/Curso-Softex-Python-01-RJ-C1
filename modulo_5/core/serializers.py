from rest_framework import serializers 
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
