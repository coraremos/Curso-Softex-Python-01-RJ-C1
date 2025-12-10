from rest_framework import serializers 
from .models import Tarefa 
from datetime import date
 
class TarefaSerializer(serializers.ModelSerializer): 
    """ 
    Serializer para o Model Tarefa. 
     
    Responsabilidades: 
    1. Converter Tarefa → JSON (serialização) 
    2. Converter JSON → Tarefa (desserialização) 
    3. Validar dados de entrada 
    """ 
     
    class Meta: 
        model = Tarefa
        fields = ['id', 'titulo', 'concluida', 'prioridade', 'prazo', 'deletada', 'criada_em']
        read_only_fields = ['id', 'criada_em', 'deletada']
        
    
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
        
        return data