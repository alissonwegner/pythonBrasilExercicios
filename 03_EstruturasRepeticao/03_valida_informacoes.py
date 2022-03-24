# 3.Faça um programa que leia e valide as seguintes informações:
#     Nome: maior que 3 caracteres;
#     Idade: entre 0 e 150;
#     Salário: maior que zero;
#     Sexo: 'f' ou 'm';
#     Estado Civil: 's', 'c', 'v', 'd';
nome = input('Informe um nome: ')
while (len(nome) <= 3):
    nome = input('Informe um nome com mais de 3 caracteres: ')

idade = int(input('Informe a idade: '))
while (idade < 0) or (idade > 150):
    idade = int(input('Informe a idade maio a 0 e menor que 150: '))

salario = int(input('Informe o salario: '))
while (salario <= 0):
    salario = int(input('Informe o salario valido: '))

sexo = input('Informe o sexo: ').upper()
#upper utilizado para colocar em caixa alta 
while (sexo != 'F') and (sexo != 'M'):
    sexo = input('Informe o sexo valido: ').upper()

estado_civil = input('Informe o estado civil: ').upper()
while ('SCVD'.find(estado_civil) < 0):
    estado_civil = input('Informe o estado civil valido: ').upper()
    #find usado para saber se valor lido esta na string 'SCVD'

print("exercicio finalizado")
