from rolepermissions.roles import AbstractUserRole

class Aluno(AbstractUserRole):
    available_permissions = {
        'detalhe_da_conta':True,
        'pegar_armario':True
    }