import manipulacao_agenda as ma

def exibe_menu():
    print("\n\n" +
    "1 - Incluir contato na agenda" +
    "\n2 - Incluir uma forma de contato" +
    "\n3 - Alterar o nome de um contato" +
    "\n4 - Alterar uma forma de contato" +
    "\n5 - Exibir um contato" +
    "\n6 - Exibir toda a agenda" +
    "\n7 - Excluir um contato" +
    "\n8 – Exportar agenda para arquivo de texto" +
    "\n9 – Exportar agenda para arquivo JSON" +
    "\n10 – Carregar agenda a partir de arquivo JSON" +
    "\n11 - Sair do sistema")
    

def manipulador_agenda():
    agenda = {}

    op = 1
    while op != 11:
        exibe_menu()
        op = int(input("Informe a opção desejada: "))
        match op:
            case 1:
                ma.usuario_inclui_contato(agenda)
            case 2:
                ma.usuario_inclui_forma_contato(agenda)
            case 3:
                ma.usuario_altera_nome_contato(agenda)
            case 4:
                ma.usuario_altera_forma_contato(agenda)
            case 5:
                ma.usuario_contato_para_texto(agenda)
            case 6:
                print(ma.agenda_para_texto(**agenda))
            case 7:
                ma.usuario_exclui_contato(agenda)
            case 8:
                nome_arquivo = input("Informe o nome do arquivo para o qual deseja exportar a agenda: ")
                ma.agenda_para_txt(nome_arquivo, agenda)
            case 9:
                nome_arquivo = input("Informe o nome do arquivo para o qual deseja exportar a agenda: ")
                ma.agenda_para_json(nome_arquivo, agenda)
            case 10:
                nome_arquivo = input("Informe o nome do arquivo do qual deseja carregar a agenda: ")
                agenda = ma.json_para_agenda(nome_arquivo)
            case 11:
                print("Saindo do sistema...")
            case _:
                print("Opção inválida! Informe uma opção existente.")


manipulador_agenda()