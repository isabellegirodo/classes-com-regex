import re

class ValidaNumerosCliente:
    def valida_cpf(self):
        cpf = str(input('Digite seu cpf: '))
        padrao = r'\d{11}'
        verifica_cpf = re.fullmatch(padrao, cpf)
        
        if verifica_cpf:
            return f'Cpf formatado: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
        else:
            raise ValueError('Cpf inválido. O cpf deve conter 11 dígitos.')
    
    def telefone_formatado(self):
        telefone = str(input('Digite seu número de telefone(celular ou fixo): '))
        
        padrao = r'^(?:9[1-9]\d{7})|(?:[1-8]\d{7})$'
        verifica_telefone = re.fullmatch(padrao, telefone)
        
        if verifica_telefone:
            if len(telefone) == 9:
                print('O número digitado pertence a um telefone celular')
                print(f'Telefone formatado: {telefone[:5]}-{telefone[5:]}')
                
            elif len(telefone) == 8:
                print(f'O número digitado pertence a um telefone fixo')
                print(f'Telefone formatado: {telefone[:4]}-{telefone[4:]}')
        else:
            raise ValueError('Telefone inválido. O telefone deve conter 8 ou 9 dígitos.')
        
    def cep_formatado(self):
        cep = str(input('Digite seu cep: '))
        padrao = r'^\d{8}$'
        valida_cep = re.fullmatch(padrao, cep)
        
        if valida_cep:
            return f'Cep formatado: {cep[:5]}-{cep[5:]}'
        else:
            raise ValueError('Cep inválido. O cep precisa conter 8 dígitos')

c = ValidaNumerosCliente()

print(c.valida_cpf())
c.telefone_formatado()
print(c.cep_formatado())
