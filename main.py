meu_dicionario = {
    'henrique': {'2011': ['10 gramas de morfina dada', '10/10/2023', '13:42']},
    'maria': {'1043': ['50 gramas paracetamol', '10/10/2023', '14:00']},
    'a': {'a': ['50 gramas paracetamol', '10/10/2023', '14:00'] },
}
usuariodic = {}
usuariologado = False
medicos={'larissa': '57742',
         'fernando': "98047",
         'a':'a'}

def adicionar_tarefa():
   
    usuario=input("digite o login:")
    senha=input("digite a sua senha:")
    if any(usuario and senha in valor for valor in medicos.values()):
        print(f'medico logado')
        nome = input("Digite o nome do paciente: ")
        codigo = input("Digite o código do paciente: ")
        if nome in meu_dicionario and codigo in meu_dicionario[nome]:
            while True:
                        
            
                    descricao = input("Digite a descrição da atividade realizada: ")
                    data = input("Digite a data: ")
                    horario = input("Digite o horário: ")

                    meu_dicionario[nome][codigo].extend([descricao, data, horario])
                    print(f"\nDados adicionados para {nome} com código {codigo}:")
                    print(f"  Descrição: {descricao}")
                    print(f"  Data: {data}")
                    print(f"  Horário: {horario}") 
                
                    
                    op=int(input("digite 1 para continuar ou 0 para sair: "))
                    if op==0:
                        break
                   
        else:
         print("A chave ou o código não estão presentes em nenhum valor do dicionário.")                             
    else:
     print(f'medico não encontrado')
     
     
     
def pacientes():
     usuario=input("digite o login:")
     senha=input("digite a sua senha:")
     if any(usuario and senha in valor for valor in medicos.values()):
        print(f'medico logado')
            
        while True:
                    
                chave = input("Digite o nome do paciente: ")
                codigo = input("Digite o código do paciente: ")
                descricao = input("Digite a descrição da atividade realizada: ")
                data = input("Digite a data: ")
                horario = input("Digite o horário: ")

                meu_dicionario[chave] = {codigo: [descricao, data, horario]}

                print(f"\nNovo paciente adicionado:")
                print(f"Nome: {chave}")
                print(f"Código: {codigo}")
                print(f"Descrição: {descricao}")
                print(f"Data: {data}")
                print(f"Horário: {horario}")
                
                                
                op=int(input("digite 1 para continuar ou 0 para sair: "))
                if op==0:
                 break
                    
     else:
      print(f'usuario não encontrado')
     

  
def fazer_login():
    global usuariologado
    usuario = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")

    if usuario in usuariodic and usuariodic[usuario][0] == senha:
        print("Usuário logado")
        usuariologado = True
    else:
        print("Credenciais inválidas. Tente novamente.")

def cadastrar_usuario():
      usuario = input("Digite o nome do usuario: ")
      senha = input("Digite  a senha: ")
      usuariodic[usuario] = [senha]
      print("usuario criado")
      
def mostrar_atividades_paciente():
    
    nome = input("Digite o nome do paciente: ")
    codigo = input("Digite o código do paciente: ")

    if nome in meu_dicionario and codigo in meu_dicionario[nome]:
        historico = meu_dicionario[nome][codigo]
        print(f'\nHistórico de atividades de {nome} ({codigo}):\n')

        for i, item in enumerate(historico, 1):
            print(item)

            if i % 3 == 0:
                print()
    else:
        print("Paciente não encontrado")

def criar_medico():
     usuario=input("digite o login:")
     senha=input("digite a sua senha:")
     if usuario=="python" and senha=="fiap":
        print(f'master logado')
            
        while True:
                    
                chave = input("Digite o nome do medico: ")
                codigo = input("Digite o código do medico: ")
               

                medicos[chave] = codigo

                print(f"\nNovo medico adicionado:")
                print(f"Nome: {chave}")
                print(f"Código: {codigo}")
                                
                op=int(input("digite 1 para continuar ou 0 para sair: "))
                if op==0:
                 break
                    
     else:
      print(f'master não encontrado')
     
    



opcao = int(input("Digite:\n1 para cadastrar usuário\n2 fazer login\n3 para ver o histórico de atividades\n4 para adicionar tarefa (necessita login de médico)\n5 para adicionar pacientes (necessita login de médico)\n6 para deslogar\n7 para acesso a camera do paciente\n8 para addicionar medico (master necessario)\n9 para ver medicos(master necessario)\n0 para sair\n"))

while opcao != 0:
    match opcao:
        case 2:
            fazer_login()
        case 4:
            adicionar_tarefa()
        case 3:
            if usuariologado:
                mostrar_atividades_paciente()
            else:
                print("Faça login primeiro.")
        case 1:
            cadastrar_usuario()
        case 6:
            usuariologado = False
            print("Usuário deslogado")
        case 5:
            pacientes()
        case 7:
            if usuariologado:
                 nome = input("Digite o nome do paciente: ")
                 codigo = input("Digite o código do paciente: ")

                 if nome in meu_dicionario and codigo in meu_dicionario[nome]:
                    print("paciente encontrado")
            else:
                print("faça login primeiro")
        case 8:
            criar_medico()
        case 9:
             usuario=input("digite o login:")
             senha=input("digite a sua senha:")
             if  usuario=="python" and senha=="fiap":
                    print(f'master logado')
                    print("Lista de Médicos:")
                    for nome, crm in medicos.items():
                        print(f"{nome.capitalize()}: CRM {crm}")
             else:
                print(f'master não encontrado')
     
        case _:
            print("opção invalida")
        
    opcao = int(input("Digite:\n1 para cadastrar usuário\n2 fazer login\n3 para ver o histórico de atividades\n4 para adicionar tarefa (necessita login de médico)\n5 para adicionar pacientes (necessita login de médico)\n6 para deslogar\n7 para acesso a camera do paciente\n8 para addicionar medico(master necessario)\n9 para ver medicos(master necessario)\n0 para sair\n"))
    