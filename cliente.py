import re

class ValidaNumerosCliente:
    def cpf_formatado(self):
        """Formata o cpf"""
        cpf = str(input('Digite seu cpf: '))
        padrao = r'\d{11}'
        verifica_cpf = re.fullmatch(padrao, cpf)
        
        if verifica_cpf:
            return f'Cpf formatado: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}\n'
        else:
            raise ValueError('Cpf inválido. O cpf deve conter 11 dígitos.')
    
    def telefone_formatado(self):
        """Formata o telefone e diz se é fixo ou celular"""
        print('Observações: o telefone fixo não pode começar com 0')
        print('O celular não pode conter o 0 após o 1º dígito 9\n')
        
        telefone = str(input('Digite seu número de telefone): '))
        
        padrao = r'^(?:9[1-9]\d{7})|(?:[1-8]\d{7})$'
        verifica_telefone = re.fullmatch(padrao, telefone)
        
        if verifica_telefone:
            if len(telefone) == 9:
                print('O número digitado pertence a um telefone celular')
                print(f'Telefone formatado: {telefone[:5]}-{telefone[5:]}\n')
                
            elif len(telefone) == 8:
                print(f'O número digitado pertence a um telefone fixo')
                print(f'Telefone formatado: {telefone[:4]}-{telefone[4:]}\n')
        else:
            raise ValueError('Telefone inválido. O telefone deve conter 8 ou 9 dígitos.')
        
    def cep_formatado(self):
        """Formata o cep"""
        cep = str(input('Digite seu cep: '))
        padrao = r'^\d{8}$'
        valida_cep = re.fullmatch(padrao, cep)
        
        if valida_cep:
            return f'Cep formatado: {cep[:5]}-{cep[5:]}'
        else:
            raise ValueError('Cep inválido. O cep precisa conter 8 dígitos')

c = ValidaNumerosCliente()

print(c.cpf_formatado())
c.telefone_formatado()
print(c.cep_formatado())
