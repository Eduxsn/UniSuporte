import sqlite3, os

banco = sqlite3.connect('banco.db')
cursor = banco.cursor()
exit = 'n'


def check_if_id_exists(id_check):
    cursor.execute(f'SELECT id FROM services WHERE id = {id_check}')
    return cursor.fetchone()


def list_services():
    cursor.execute("SELECT * FROM services")
    for row in cursor.fetchall():
        print('ID:', row[0])
        print('Nome:', row[1])
        print('Relato:', row[2])
        print('Status:', row[3])
        print('------------------------')


while exit == 'n':
    print("""### UniSuporte agendamentos ###
    [1] - Cadastrar computador
    [2] - Atualizar status de um computador
    [3] - Listar serviços
    [4] - Remover serviços
    [5] - Sair
    """)
    option = int(input("Escolha a opção desejada: "))

    if option == 1:
        cliente = input('Digite o nome do cliente:')
        report = input('Digite o relato do ocorrido')
        cursor.execute(f"INSERT INTO services (name, report, status) VALUES ('{cliente}', '{report}', 'na fila')")
        banco.commit()
        input('Registro inserido com sucesso... Tecle para continuar')
    elif option == 2:
        print(""""### Selecione o serviço a ser ATUALIZADO ###""")
        list_services()
        id = int(input('Selecione um ID para alterar o status: '))

        check = check_if_id_exists(id)

        if not check:
            input('ID NÃO ENCONTRADO! Enter para continuar....')
        else:
            print("""
            [1] - Na fila
            [2] - Em Manutenção
            [3] - Concluído""")
            new_status = int(input('Escolha o novo status do serviço: '))
            if new_status == 1:
                new_status = 'na fila'
            elif new_status == 2:
                new_status = 'em manutenção'
            elif new_status == 3:
                new_status = 'concluído'

            cursor.execute(f"UPDATE services SET status = '{new_status}' WHERE id = {id} ")
            banco.commit()

    elif option == 3:
        list_services()
        input('Tecle para continuar...')

    elif option == 4:
        print(""""### Selecione o serviço a ser REMOVIDO ###""")
        list_services()
        id = int(input('Selecione um ID para ser removido: '))

        check = check_if_id_exists(id)

        if not check:
            input('ID NÃO ENCONTRADO! Enter para continuar....')
        else:
            cursor.execute(f"DELETE FROM services WHERE id = {id}")
            banco.commit()
            input('Remoção executada, tecle enter para continuar')

    elif option == 5:
        print('Até logo!')
        exit = 's'

    else:
        input('Opção inválida, tecle enter para continuar...')
