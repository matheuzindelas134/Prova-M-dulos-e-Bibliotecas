alunos = {}

def AdicionarAluno():
    matricula = input("Digite o número de matrícula do aluno: ")
    nome = input("Digite o nome do aluno: ")
    
    if matricula in alunos:
        print("Aluno já cadastrado. Use a função AtualizarAluno() para alterar o nome.")
    else:
        alunos[matricula] = nome
        print("Aluno adicionado com sucesso!")

def RemoverAluno():
    matricula = input("Digite o número de matrícula do aluno a ser removido: ")
    
    if matricula in alunos:
        del alunos[matricula]
        print("Aluno removido com sucesso!")
    else:
        print("Número de matrícula não encontrado.")

def AtualizarAluno():
    matricula = input("Digite o número de matrícula do aluno a ser atualizado: ")
    
    if matricula in alunos:
        novo_nome = input("Digite o novo nome do aluno: ")
        alunos[matricula] = novo_nome
        print("Nome do aluno atualizado com sucesso!")
    else:
        print("Número de matrícula não encontrado.")

def VerAlunos():
    if alunos:
        print("\nLista de Alunos:")
        for matricula, nome in alunos.items():
            print(f"Número de matrícula: {matricula}, Nome: {nome}")
    else:
        print("Nenhum aluno cadastrado.")

def menu():
    while True:
        print("\nMenu de Gerenciamento de Alunos")
        print("1. Adicionar aluno")
        print("2. Remover aluno")
        print("3. Atualizar aluno")
        print("4. Ver alunos")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            AdicionarAluno()
        elif escolha == '2':
            RemoverAluno()
        elif escolha == '3':
            AtualizarAluno()
        elif escolha == '4':
            VerAlunos()
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()