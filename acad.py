# classe aluno
class Aluno:
    def __init__(self, nome, cpf, peso, altura):
        self.nome = nome
        self.cpf = cpf
        self.peso = peso
        self.altura = altura
        self.status = False

# cadastrar um aluno
def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    cpf = input("CPF do aluno: ")
    peso = float(input("Peso em kg: "))
    altura = float(input("Altura em metros: "))

    aluno = Aluno(nome, cpf, peso, altura)
    alunos.append(aluno)
    treinos.append([])  # add lista vazia de treinos para o aluno
    print("Aluno cadastrado com sucesso!")

# gerenciar o treino de um aluno
def gerenciar_treino():
    nome = input("Nome do aluno: ")
    aluno_encontrado = False

    for i, aluno in enumerate(alunos):
        if aluno.nome.lower() == nome.lower():
            aluno_encontrado = True
            treino = treinos[i]  # obtem o treino do aluno

            print(f"\n--- Gerenciamento de treino do aluno {aluno.nome} ---")
            print("1 - Incluir novo exercício")
            print("2 - Alterar exercício existente")
            print("3 - Excluir exercício específico")
            print("4 - Excluir todos os exercícios do treino")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                nome_exercicio = input("Nome do exercício: ")
                repeticoes = int(input("Número de repetições: "))
                peso = float(input("Peso utilizado (em kg): "))

                for exercicio in treino:
                    if exercicio["nome"].lower() == nome_exercicio.lower():
                        print("Erro: O exercício já existe no treino do aluno.")
                        break
                else:
                    novo_exercicio = {"nome": nome_exercicio, "repeticoes": repeticoes, "peso": peso}
                    treino.append(novo_exercicio)
                    aluno.status = True
                    print("Exercício adicionado com sucesso!")

            elif opcao == "2":
                numero_exercicio = int(input("Digite o número do exercício a ser alterado: "))
                if 1 <= numero_exercicio <= len(treino):
                    exercicio = treino[numero_exercicio - 1]

                    nome_exercicio = input("Nome do exercício: ")
                    repeticoes = int(input("Número de repetições: "))
                    peso = float(input("Peso utilizado (em kg): "))

                    exercicio["nome"] = nome_exercicio
                    exercicio["repeticoes"] = repeticoes
                    exercicio["peso"] = peso

                    print("Exercício alterado com sucesso!")
                else:
                    print("Erro: Número de exercício inválido.")

            elif opcao == "3":
                numero_exercicio = int(input("Digite o número do exercício a ser excluído: "))
                if 1 <= numero_exercicio <= len(treino):
                    treino.pop(numero_exercicio - 1)

                    if not treino:
                        aluno.status = False

                    print("Exercício excluído com sucesso!")
                else:
                    print("Erro: Número de exercício inválido.")

            elif opcao == "4":
                treino.clear()
                aluno.status = False
                print("Todos os exercícios do treino foram excluídos com sucesso!")

            else:
                print("Opção inválida.")

            break

    if not aluno_encontrado:
        print("Aluno não encontrado.")

# consultar um aluno
def consultar_aluno():
    nome = input("Digite o nome do aluno: ")
    aluno_encontrado = False

    for i, aluno in enumerate(alunos):
        if aluno.nome.lower() == nome.lower():
            aluno_encontrado = True
            treino = treinos[i]

            print("\n--- Dados do Aluno ---")
            print(f"Nome: {aluno.nome}")
            print(f"CPF: {aluno.cpf}")
            print(f"Peso: {aluno.peso} kg")
            print(f"Altura: {aluno.altura} metros")

            if treino:
                print("\n--- Treino ---")
                for j, exercicio in enumerate(treino):
                    print(f"\nExercício {j+1}:")
                    print(f"Nome: {exercicio['nome']}")
                    print(f"Repetições: {exercicio['repeticoes']}")
                    print(f"Peso: {exercicio['peso']} kg")
            else:
                print("\nO aluno não possui exercícios cadastrados.")

            break

    if not aluno_encontrado:
        print("Aluno não encontrado.")

# atualizar o cadastro de um aluno
def atualizar_cadastro_aluno():
    nome = input("Digite o nome do aluno: ")
    aluno_encontrado = False

    for aluno in alunos:
        if aluno.nome.lower() == nome.lower():
            aluno_encontrado = True

            print("\n--- Atualização de Cadastro ---")
            print(f"Nome atual: {aluno.nome}")
            novo_nome = input("Digite o novo nome (ou deixe em branco para manter o atual): ")
            aluno.nome = novo_nome if novo_nome else aluno.nome

            print(f"CPF atual: {aluno.cpf}")
            novo_cpf = input("Digite o novo CPF (ou deixe em branco para manter o atual): ")
            aluno.cpf = novo_cpf if novo_cpf else aluno.cpf

            print(f"Peso atual: {aluno.peso} kg")
            novo_peso = input("Digite o novo peso (ou deixe em branco para manter o atual): ")
            aluno.peso = float(novo_peso) if novo_peso else aluno.peso

            print(f"Altura atual: {aluno.altura} metros")
            nova_altura = input("Digite a nova altura (ou deixe em branco para manter a atual): ")
            aluno.altura = float(nova_altura) if nova_altura else aluno.altura

            print("Cadastro atualizado com sucesso!")
            break

    if not aluno_encontrado:
        print("Aluno não encontrado.")

# excluir um aluno
def excluir_aluno():
    nome = input("Digite o nome do aluno: ")
    aluno_encontrado = False

    for i, aluno in enumerate(alunos):
        if aluno.nome.lower() == nome.lower():
            aluno_encontrado = True
            treinos.pop(i)  # Remove o treino do aluno da matriz
            alunos.pop(i)  # Remove o aluno do vetor
            print("Aluno excluído com sucesso!")
            break

    if not aluno_encontrado:
        print("Aluno não encontrado.")

# exibir o relatório de alunos
def relatorio_alunos():
    print("--- Relatório de Alunos ---")
    print("1 - Todos os alunos")
    print("2 - Somente alunos ativos")
    print("3 - Somente alunos inativos")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        lista_alunos = []
        for aluno in alunos:
            lista_alunos.append(aluno)
    elif opcao == "2":
        lista_alunos = []
        for aluno in alunos:
            if aluno.status:
                lista_alunos.append(aluno)
    elif opcao == "3":
        lista_alunos = []
        for aluno in alunos:
            if not aluno.status:
                lista_alunos.append(aluno)
    else:
        print("Opção inválida.")
        return

    if lista_alunos:
        # acha o aluno com o menor nome
        menor_nome = lista_alunos[0].nome
        for aluno in lista_alunos:
            if aluno.nome < menor_nome:
                menor_nome = aluno.nome

        # alunos em ordem alfabética pelo nome
        while lista_alunos:
            aluno_atual = lista_alunos[0]
            for aluno in lista_alunos:
                if aluno.nome < aluno_atual.nome:
                    aluno_atual = aluno

            print("\nNome: " + aluno_atual.nome)
            print("CPF: " + aluno_atual.cpf)
            if aluno_atual.status:
                print("Status: Ativo")
            else:
                print("Status: Inativo")

            lista_alunos.remove(aluno_atual)
    else:
        print("Nenhum aluno encontrado.")


# Lista para armazenar os alunos cadastrados
alunos = []

# Matriz para armazenar os treinos dos alunos
treinos = []


# Variável para controlar o número total de alunos cadastrados
num_alunos_cadastrados = 0

# Loop do Menu Principal
while True:
    print("\n--- Menu Principal ---")
    print("1 - Cadastrar aluno")
    print("2 - Gerenciar treino")
    print("3 - Consultar aluno")
    print("4 - Atualizar cadastro do aluno")
    print("5 - Excluir aluno")
    print("6 - Relatório de alunos")
    print("0 - Sair do programa")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()
        num_alunos_cadastrados += 1
    elif opcao == "2":
        gerenciar_treino()
    elif opcao == "3":
        consultar_aluno()
    elif opcao == "4":
        atualizar_cadastro_aluno()
    elif opcao == "5":
        excluir_aluno()
        num_alunos_cadastrados -= 1
    elif opcao == "6":
        relatorio_alunos()
    elif opcao == "0":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida.")
