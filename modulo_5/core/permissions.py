from rest_framework import permissions  

class IsGerente(permissions.BasePermission):     
    """     
    Permissão customizada que concede acesso apenas se o usuário     
    pertencer ao grupo 'Gerente'.     
    """      

    def has_permission(self, request, view):         
        # 1. Verificação de Sanidade: Usuário deve estar logado         
        if not request.user or not request.user.is_authenticated:             
            return False
                      
        # 2. Verificação de Grupo: Checa se 'Gerente' está na lista de grupos         
        return request.user.groups.filter(name='Gerente').exists()

class IsAdminOrOwner(permissions.BasePermission):
    """
    Permite acesso se o usuário for da equipe (staff/admin) ou se for o dono(owner).
    
    Uso típico: Detail Views (GET, PUT, DELETE de recurso específico)
        
    Regras:
    - Staff/Superuser: Acesso total
    - Usuário comum: Apenas se for dono (obj.user == request.user)
    
    """
    def has_object_permission(self, request, view, obj):
        """
        Verifica permissão em nível de objeto.        
                
        Args:       
            request: Requisição HTTP        
            view: View sendo executada            
            obj: Objeto específico (ex: instância de Tarefa)          
                
        Returns:       
            bool: True se tem permissão, False caso contrário           
               
        """

        # Se o usuário for Staff (Admin), ele tem acesso a todos os objetos
        if request.user.is_staff:
            return True
        
        # Se for o dono do objeto ele consegue acessar o objeto
        return obj.user == request.user

class IsOwner(permissions.BasePermission):
    """
    Permissão simples: Apenas o dono pode acessar.

    Uso: Quando não há exceção para Admin.
    """
    def has_object_permission(self, request, view, obj):
        """Verifica se o usuário é o dono do objeto."""
        return obj.user == request.user
    
class CanDeleteTask(permissions.BasePermission):
    """
    Permissão de negócio: Apenas Gerentes podem deletar tarefas.

    Exemplo de regra de negócio customizada.
    """

    message = "Apenas gerentes podem deletar tarefas."

    def has_permission(self, request, view):
        """
        Verifica se a operação é DELETE e se o usuário é Gerente.
        """
        #se não é DELETE, permite (outras permissões vão validar)
        if request.method != 'DELETE':
            return True
        #se é DELETE, exige grupo Gerente
        return request.user.groups.filter(name='Gerente').exists()