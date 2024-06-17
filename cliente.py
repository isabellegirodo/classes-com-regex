import re

class Cliente:
    def valida_cpf(self):
        cpf = str(input('Digite seu cpf: '))
        padrao = r'\d{11}'
        verifica_cpf = re.fullmatch(padrao, cpf)
        
        if verifica_cpf:
            return f'Cpf formatado: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
        else:
            raise ValueError('Cpf inválido. O cpf deve conter 11 dígitos.')

c = Cliente()
print(c.valida_cpf())