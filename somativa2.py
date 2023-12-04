'''
    Aluno: RENATO HIDEKI MOTIKAWA
    Curso: ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
'''

import json #importando a biblioteca json para o armazenamento de dados no disco rígido

def salvar_dados(arquivo, dados): #função para salvar dados no arquivo json
    with open(arquivo, 'w') as f:
        json.dump(dados, f)

def recuperar_dados(arquivo): #função para recuperar dados do arquivo json
    try:
        with open(arquivo, 'r') as f:
            dados = json.load(f)
    except FileNotFoundError:
        dados = [] #caso o arquivo não seja encontrado, retornará uma lista vazia
    return dados

def menu_principal(): #menu principal
    print(
        '========== MENU PRINCIPAL ==========\n\n'
        '(1) Gerenciar Estudantes\n'
        '(2) Gerenciar Disciplinas\n'
        '(3) Gerenciar Professores\n'
        '(4) Gerenciar Turmas\n'
        '(5) Gerenciar Matrículas\n'
        '(9) Sair\n'
    )

def menu_operacoes(tipo): #menu de operações
    print(
        f'========== [{tipo.upper()}] MENU DE OPERAÇÕES ==========\n\n' #o tipo de opção escolhida no menu anterior é exibida no menu de operações
        '(1) Incluir\n'
        '(2) Listar\n'
        '(3) Atualizar\n'
        '(4) Excluir\n'
        '(9) Voltar ao menu principal\n'
    )

def incluir(tipo, arquivo, lista_pessoas): #função para inclusão de dados
    if tipo == "Estudante" or tipo == "Professor": #inclusão de estudantes e professores
        codigo = int(input(f'Digite o código do {tipo.lower()}: '))
        pessoa = input(f'Digite o nome do {tipo.lower()}: ')
        cpf = input(f'Digite o CPF do {tipo.lower()}: ')

        lista = recuperar_dados(arquivo) #recuperando o arquivo json mais atualizado

        pessoa_ja_cadastrada = any(codigo == tupla[0] or cpf == tupla[2] for tupla in lista) #verifica se já há uma pessoa cadastrada com o código ou cpf fornecido (a função any retorna true sempre que pelo menos um dos elementos iteráveis passados como argumento for verdadeiro)

        if not pessoa_ja_cadastrada:
            tupla_pessoa = (codigo, pessoa, cpf)
            lista.append(tupla_pessoa)
            salvar_dados(arquivo, lista) #salvando as informações no arquivo json
            print(f'{tipo} cadastrado com sucesso!\n') 
        else:
            print(f'{tipo} já cadastrado com o CPF ou código informado!\n')
            
    if tipo == "Disciplina": #inclusão de disciplinas 
        codigo = int(input(f'Digite o código da {tipo.lower()}: '))
        disciplina = input(f'Digite o nome da {tipo.lower()}: ')

        lista = recuperar_dados(arquivo) #recuperando o arquivo json mais atualizado

        disciplina_ja_cadastrada = any(codigo == tupla[0] for tupla in lista)

        if not disciplina_ja_cadastrada:
            tupla_disciplina = (codigo, disciplina)
            lista.append(tupla_disciplina)
            salvar_dados(arquivo, lista) #salvando as informações no arquivo json
            print(f'{tipo} cadastrada com sucesso!\n')
        else:
            print(f'{tipo} já cadastrada com o código informado!\n')

    if tipo == "Turma": #inclusão de turmas 
        codigo = int(input(f'Digite o código da {tipo.lower()}: '))
        professor = int(input(f'Digite o código da professor: '))
        disciplina = int(input(f'Digite o código da disciplina: '))

        lista = recuperar_dados(arquivo) #recuperando o arquivo json mais atualizado

        turma_ja_cadastrada = any(codigo == tupla[0] for tupla in lista)

        if not turma_ja_cadastrada:
            tupla_turma = (codigo, professor, disciplina)
            lista.append(tupla_turma)
            salvar_dados(arquivo, lista) #salvando as informações no arquivo json
            print(f'{tipo} cadastrada com sucesso!\n')
        else:
            print(f'{tipo} já cadastrada com o código informado!\n')

    if tipo == "Matricula": #inclusão de matrículas 
        codigo = int(input(f'Digite o código da turma: '))
        estudante = int(input(f'Digite o código do estudante: '))

        lista = recuperar_dados(arquivo) #recuperando o arquivo json mais atualizado

        matricula_ja_cadastrada = any(estudante == tupla[1] for tupla in lista)

        if not matricula_ja_cadastrada:
            tupla_disciplina = (codigo, estudante)
            lista.append(tupla_disciplina)
            salvar_dados(arquivo, lista) #salvando as informações no arquivo json
            print(f'{tipo} cadastrada com sucesso!\n')
        else:
            print(f'{tipo} já cadastrada com o código informado!\n')

def listar(tipo, arquivo): #função para listagem de dados
    lista = recuperar_dados(arquivo)
    if len(lista) < 1:
        if tipo == "Estudante" or tipo == "Professor":
            print(f'\nNenhum {tipo.lower()} cadastrado.\n')
        if tipo == "Disciplina" or tipo == "Turma" or tipo == "Matricula":
            print(f'\nNenhuma {tipo.lower()} cadastrada.\n')
    else:
        if tipo == "Estudante": #listagem de estudantes
            print(f'========== {tipo.upper()}S ==========\n')
            for tupla in lista:
                print(f'- Código: {tupla[0]}, {tipo}: {tupla[1]}, CPF: {tupla[2]}')
            print('\n')
        if tipo == "Professor": #listagem de professores
            print('========== PROFESSORES ==========\n')
            for tupla in lista:
                print(f'- Código: {tupla[0]}, {tipo}: {tupla[1]}, CPF: {tupla[2]}')
            print('\n')
        if tipo == "Disciplina": #listagem de disciplinas
            print(f'========== {tipo.upper()}S ==========\n')
            for tupla in lista:
                print(f'- Código: {tupla[0]}, {tipo}: {tupla[1]}')
            print('\n')
        if tipo == "Turma": #listagem de turmas
            print(f'========== {tipo.upper()}S ==========\n')
            for tupla in lista:
                print(f'- Código: {tupla[0]}, Professor: {tupla[1]}, Disciplina: {tupla[2]}')
            print('\n')
        if tipo == "Matricula": #listagem de matrículas
            print(f'========== {tipo.upper()}S ==========\n')
            for tupla in lista:
                print(f'- Código: {tupla[0]}, Estudante: {tupla[1]}')
            print('\n')

def atualizar(tipo, arquivo): #função para atualização de dados
    lista = recuperar_dados(arquivo) #recuperando o arquivo json mais atualizado
    if len(lista) < 1:
        if tipo == "Estudante" or tipo == "Professor":
            print(f'\nNenhum {tipo.lower()} cadastrado.\n')
        if tipo == "Disciplina" or tipo == "Turma" or tipo == "Matricula":
            print(f'\nNenhuma {tipo.lower()} cadastrada.\n')
    else:
        if tipo == "Estudante" or tipo == "Professor": #atualização de estudantes e professores
            codigo = int(input(f'Digite o código do {tipo} que deseja atualizar: '))
            pessoa_encontrada = False

            for tupla in lista:
                if codigo == tupla[0]:
                    novo_codigo = int(input(f'Digite o novo código do {tipo.lower()}: '))
                    novo_nome = input(f'Digite o novo nome do {tipo.lower()}: ')
                    novo_cpf = input(f'Digite o novo CPF do {tipo.lower()}: ')

                    pessoa_ja_cadastrada = any(novo_codigo == t[0] or novo_cpf == t[2] for t in lista if t != tupla)

                    if not pessoa_ja_cadastrada:
                        lista.remove(tupla)
                        tupla = (novo_codigo, novo_nome, novo_cpf)
                        lista.append(tupla)
                        salvar_dados(arquivo, lista) #salvando as informações no arquivo json
                        print(f'{tipo} atualizado(a) com sucesso!\n')
                        pessoa_encontrada = True
                    else:
                        print(f'{tipo} já cadastrado com o CPF ou código informado!\n')
                        pessoa_encontrada = True

            if not pessoa_encontrada:
                print(f'{tipo} não encontrado!\n')

        if tipo == "Disciplina": #atualização de disciplinas
            codigo = int(input(f'Digite o código da {tipo.lower()} que deseja atualizar: '))
            disciplina_encontrada = False

            for tupla in lista:
                if codigo == tupla[0]:
                    novo_codigo = int(input(f'Digite o novo código da {tipo.lower()}: '))
                    novo_nome = input(f'Digite o novo nome da {tipo.lower()}: ')

                    disciplina_ja_cadastrada = any(novo_codigo == t[0] for t in lista if t != tupla)

                    if not disciplina_ja_cadastrada:
                        lista.remove(tupla)
                        tupla = (novo_codigo, novo_nome)
                        lista.append(tupla)
                        salvar_dados(arquivo, lista) #salvando as informações no arquivo json
                        print(f'{tipo} atualizada com sucesso!\n')
                        disciplina_encontrada = True
                    else:
                        print(f'{tipo} já cadastrada com o código informado!\n')
                        disciplina_encontrada = True

            if not disciplina_encontrada:
                print(f'{tipo} não encontrada!\n')

        if tipo == "Turma": #atualização de turmas
            codigo = int(input(f'Digite o código da {tipo.lower()} que deseja atualizar: '))
            turma_encontrada = False

            for tupla in lista:
                if codigo == tupla[0]:
                    novo_codigo = int(input(f'Digite o novo código da {tipo.lower()}: '))
                    novo_professor = int(input(f'Digite o novo código do professor: '))
                    nova_disciplina = int(input(f'Digite o novo código da disciplina: '))

                    turma_ja_cadastrada = any(novo_codigo == t[0] for t in lista if t != tupla)

                    if not turma_ja_cadastrada:
                        lista.remove(tupla)
                        tupla = (novo_codigo, novo_professor, nova_disciplina)
                        lista.append(tupla)
                        salvar_dados(arquivo, lista) #salvando as informações no arquivo json
                        print(f'{tipo} atualizada com sucesso!\n')
                        turma_encontrada = True
                    else:
                        print(f'{tipo} já cadastrada com o código informado!\n')
                        turma_encontrada = True

            if not turma_encontrada:
                print(f'{tipo} não encontrada!\n')
        
        if tipo == "Matricula": #atualização de matrículas
            codigo = int(input(f'Digite o código da {tipo.lower()} que deseja atualizar: '))
            matricula_encontrada = False

            for tupla in lista:
                if codigo == tupla[0]:
                    novo_codigo = int(input(f'Digite o novo código da {tipo.lower()}: '))
                    novo_estudante = input(f'Digite o novo código do estudante: ')

                    matricula_ja_cadastrada = any(novo_codigo == t[0] for t in lista if t != tupla)

                    if not matricula_ja_cadastrada:
                        lista.remove(tupla)
                        tupla = (novo_codigo, novo_estudante)
                        lista.append(tupla)
                        salvar_dados(arquivo, lista) #salvando as informações no arquivo json
                        print(f'{tipo} atualizada com sucesso!\n')
                        matricula_encontrada = True
                    else:
                        print(f'{tipo} já cadastrada com o código informado!\n')
                        matricula_encontrada = True

            if not matricula_encontrada:
                print(f'{tipo} não encontrada!\n')

def excluir(tipo, arquivo): #função para exclusão de dados
    lista = recuperar_dados(arquivo) #recuperando o arquivo json mais atualizado
    if len(lista) < 1:
        if tipo == "Estudante" or tipo == "Professor":
            print(f'\nNenhum {tipo.lower()} cadastrado.\n')
        if tipo == "Disciplina" or tipo == "Turma" or tipo == "Matricula":
            print(f'\nNenhuma {tipo.lower()} cadastrada.\n')
    else:
        codigo = int(input(f'Digite o código do {tipo.lower()} que deseja excluir: '))
        for tupla in lista:
            if codigo == tupla[0]:
                lista.remove(tupla)
                salvar_dados(arquivo, lista) #salvando as informações no arquivo json
                if tipo == "Estudante" or tipo == "Professor":
                    print(f'{tipo} excluído com sucesso!\n')       
                if tipo == "Disciplina" or tipo == "Turma" or tipo == "Matricula":
                    print(f'{tipo} excluída com sucesso!\n')       
                break
        else:
            if tipo == "Estudante" or tipo == "Professor":
                print(f'\n{tipo} não encontrado!\n')
            if tipo == "Disciplina" or tipo == "Turma" or tipo == "Matricula":
                print(f'\n{tipo} não encontrada!\n')

while True:
    menu_principal()
    try: #controle de exceções
        opcao = int(input('Selecione uma opção: '))
        print('\n')
        if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4 or opcao == 5 or opcao == 9:
            if opcao == 1:
                while True:
                    menu_operacoes("estudantes")
                    opcao = int(input('Selecione uma opção: '))
                    print('\n')
                    if opcao == 1:
                        incluir("Estudante", "estudantes.json", "estudantes")
                    elif opcao == 2:
                        listar("Estudante", "estudantes.json")
                    elif opcao == 3:
                        atualizar("Estudante", "estudantes.json")
                    elif opcao == 4:
                        excluir("Estudante", "estudantes.json")
                    elif opcao == 9:
                        print('========== [ESTUDANTES] ATUALIZAÇÃO ==========\n\nVoltando ao menu principal...\n')
                        break
                    else:
                        print('Digite uma opção válida!\n')
            elif opcao == 2:
                while True:
                    menu_operacoes("disciplinas")
                    opcao = int(input('Selecione uma opção: '))
                    print('\n')
                    if opcao == 1:
                        incluir("Disciplina", "disciplinas.json", "disciplina")
                    elif opcao == 2:
                        listar("Disciplina", "disciplinas.json")
                    elif opcao == 3:
                        atualizar("Disciplina", "disciplinas.json")
                    elif opcao == 4:
                        excluir("Disciplina", "disciplinas.json")
                    elif opcao == 9:
                        print('========== [DISCIPLINAS] ATUALIZAÇÃO ==========\n\nVoltando ao menu principal...\n')
                        break
                    else:
                        print('Digite uma opção válida!\n')
            elif opcao == 3:
                while True:
                    menu_operacoes("professores")
                    opcao = int(input('Selecione uma opção: '))
                    print('\n')
                    if opcao == 1:
                        incluir("Professor", "professores.json", "professores")
                    elif opcao == 2:
                        listar("Professor", "professores.json")
                    elif opcao == 3:
                        atualizar("Professor", "professores.json")
                    elif opcao == 4:
                        excluir("Professor", "professores.json")
                    elif opcao == 9:
                        print('========== [PROFESSORES] ATUALIZAÇÃO ==========\n\nVoltando ao menu principal...\n')
                        break
                    else:
                        print('Digite uma opção válida!\n')
            elif opcao == 4:
                while True:
                    menu_operacoes("turmas")
                    opcao = int(input('Selecione uma opção: '))
                    print('\n')
                    if opcao == 1:
                        incluir("Turma", "turmas.json", "turmas")
                    elif opcao == 2:
                        listar("Turma", "turmas.json")
                    elif opcao == 3:
                        atualizar("Turma", "turmas.json")
                    elif opcao == 4:
                        excluir("Turma", "turmas.json")
                    elif opcao == 9:
                        print('========== [TURMAS] ATUALIZAÇÃO ==========\n\nVoltando ao menu principal...\n')
                        break
                    else:
                        print('Digite uma opção válida!\n')
            elif opcao == 5:
                while True:
                    menu_operacoes("matrículas")
                    opcao = int(input('Selecione uma opção: '))
                    print('\n')
                    if opcao == 1:
                        incluir("Matricula", "matriculas.json", "matriculas")
                    elif opcao == 2:
                        listar("Matricula", "matriculas.json")
                    elif opcao == 3:
                        atualizar("Matricula", "matriculas.json")
                    elif opcao == 4:
                        excluir("Matricula", "matriculas.json")
                    elif opcao == 9:
                        print('========== [MATRÍCULAS] ATUALIZAÇÃO ==========\n\nVoltando ao menu principal...\n')
                        break
                    else:
                        print('Digite uma opção válida!\n')
            else:
                print('Saindo...\n')
                break
        else:
            print('Digite uma opção válida!\n')
    except ValueError: #caso o usuário digite um caractere diferente de um número o erro é tratado e uma mensagem mais agradável é exibida sem quebrar o fluxo do programa
        print('\nPor favor, digite uma opção válida e tente novamente.\n')