import json

contatos_suportados = ("telefone", "email", "endereco")

agenda = {
    "Pessoa 1":{
        "telefone":["11 1234-5678"],
        "email":["pessoa@email.com", "email@profissional.com"],
        "endereco":["Rua 123"]
    },
    "Pessoa 2":{
        "telefone":["11 9874-5678"],
        "email":["pessoa2@email.com", "pessoa2@profissional.com"],
        "endereco":["Rua 345"]
    },
    "Pessoa 3":{
        "telefone":["51 4321-5678"],
        "email":["pessoa3@email.com", "pessoa3@profissional.com"],
        "endereco":["Rua 567"]
    }
    
}


#MÉTODOS:
def contato_para_texto(nome:str, **formas_de_contato): #Imprime o contato em um formato de texto.
    formato_texto = f"{nome.upper()}:"
    for meio_contato, contato in formas_de_contato.items():
        formato_texto = f"{formato_texto}\n{meio_contato.upper()}(S)"
        contador_formas = 1

        for valor in contato:
            formato_texto = f"{formato_texto}\n	{contador_formas} - {valor.upper()}"
            contador_formas = contador_formas + 1

    return formato_texto


def agenda_para_texto(**agenda_completa): #Imprime a agenda completa.
    formato_texto = ""
    formato_texto = f"{formato_texto}---------------------------\n"
    for nome_contato, formas_contato in agenda_completa.items():
        formato_texto = f"{formato_texto}{contato_para_texto(nome_contato, **formas_contato)}\n"
        formato_texto = f"{formato_texto}---------------------------\n"

    return formato_texto


def altera_nome_contato(agenda_original:dict, nome:str, nome_alterado:str): #Altera o nome do contato.
    if nome in agenda_original.keys():
        copia_contatos = agenda_original[nome].copy()
        agenda_original.pop(nome)
        agenda_original[nome_alterado] = copia_contatos
        return True
    
    return False
#EXEMPLO: altera_nome_contato(agenda, "Pessoa 1", "Pessoa 1 Alterada")


def altera_forma_contato(lista_contatos:list, valor_antigo:str, valor_atualizado:str): #Altera uma forma de contato.
    if valor_antigo in lista_contatos:
        posicao_valor_antigo = lista_contatos.index(valor_antigo)
        lista_contatos.pop(posicao_valor_antigo)
        lista_contatos.insert(posicao_valor_antigo, valor_atualizado)
        return True
    
    return False
#EXEMPLO: altera_forma_contato(agenda["Pessoa 1"]["endereco"], "Rua 123", "Rua 2323322")


def exclui_contato(agenda:dict, nome_contato:str): #Exclui um contato da agenda pelo nome.
    if nome_contato in agenda.keys():
        agenda.pop(nome_contato)
        return True
    
    return False
#EXEMPLO: exclui_contato_nome(agenda, "Pessoa 1")


def inclui_contato(agenda:dict, nome_contato:str, **formas_contato): #Adiciona um contato a agenda
    agenda[nome_contato] = formas_contato

#EXEMPLO: inclui_contato(agenda, "AZul", telefone=["11 1234-5678"])


def inclui_forma_contato(formas_contato:dict, forma_incluida:str, valor_incluido:str): #Adiciona uma forma de contato a um contato já existente.
    if forma_incluida in formas_contato.keys():
        formas_contato[forma_incluida].append(valor_incluido)
        return True
    elif forma_incluida in contatos_suportados:
        formas_contato[forma_incluida] = [valor_incluido]
        return True
    return False

#EXEMPLO: inclui_forma_contato(agenda["Pessoa 1"], "telefone", "78 1234-5678")


def usuario_inclui_contato(agenda:dict): #Permite que o usuário inclua um contato na agenda.
    nome = input("Informe o nome do novo contato que será inserido na agenda: ")
    dicionario_formas = {}
    for forma in contatos_suportados:
        resposta = input(f"Deseja inserir um {forma} para {nome.upper()}? \nS ou N: ")
        lista_contatos = []
        while "S" in resposta.upper():
            lista_contatos.append(input(f"Informe um {forma}: "))
            resposta = input(f"Deseja inserir outro {forma} para {nome.upper()}? \nS ou N: ")
        if len(lista_contatos) > 0:
            dicionario_formas[forma] = lista_contatos.copy()
            lista_contatos.clear()
    if len(dicionario_formas.keys()) > 0:
        inclui_contato(agenda, nome, **dicionario_formas)
        print(f"Inclusão bem sucedida! O contato {nome.upper()} foi adicionado à agenda. ")
        
    else:
        print("É necessário incluir pelo menos uma forma de contato! \nA agenda não foi alterada.")


def usuario_inclui_forma_contato(agenda:dict): #Permite que o usuário inclua uma forma de contato a um contato já existente.
    nome = input("Informe o nome do contato para o qual deseja incluir formas de contato: ")
    if nome in agenda.keys():
        print(f"As formas de contato suportadas pelo sistema são: {contatos_suportados}")
        forma_incluida = input("Qual forma de contato deseja incluir? ")
        if forma_incluida in contatos_suportados:
            valor_incluido = input(f"Informe o {forma_incluida} que deseja incluir: ")
            if inclui_forma_contato(agenda[nome], forma_incluida, valor_incluido):
                print("Operação bem sucedida! A nova forma de contato foi incluida! ")
            else:
                print("Ocorreu um erro durante a inserção. A agenda não foi alterada.")
        else:
            print("A forma de contato indicada não é suportada pelo sistema. A agenda não foi alterada.")
    else:
        print("O contato informado não existe na agenda. Não foram feitas alterações. ")


def usuario_exclui_contato(agenda:dict): #Exclui um contato
    nome = input("Informe o nome do contato que deseja excluir: ")
    if exclui_contato(agenda, nome):
        print("Usuário excluido com sucesso!")
    else:
        print("Nome do usuário não localizado na agenda. Não foram feitas alterações.")


def usuario_altera_nome_contato(agenda:dict): #Permite que o usuário altere o nome de um contato já existente.
    nome_original = input("Informe o nome do contato que deseja alterar: ")
    nome_atualizado = input("Informe o nome do novo contato: ")
    if altera_nome_contato(agenda, nome_original, nome_atualizado):
        print(f"O contato: {nome_original.upper()} foi atualizado para: {nome_atualizado.upper()}.")
    else:
        print(f"O contato original não foi localizado. A agenda não foi alterada.")


def usuario_altera_forma_contato(agenda:dict): #Permite que o usuário altere uma forma de contato de um contato já existente.
    nome = input("Informe o nome do contato que deseja alterar: ")
    if nome in agenda.keys():
        print(f"As formas de contato suportadas pelo sistema são: {contatos_suportados}")
        forma_incluida = input("Qual forma de contato deseja incluir? ")
        if forma_incluida in contatos_suportados:
            print(contato_para_texto(nome, **agenda[nome]))
            valor_antigo = input(f"Informe o {forma_incluida} que deseja alterar " )
            nova_valor = input(f"Informe o novo {forma_incluida} ")
            if altera_forma_contato(agenda[nome][forma_incluida], valor_antigo, nova_valor):
                print(f"Contato {nome} alterado. O {forma_incluida} {valor_antigo} foi atualizado para {nova_valor}.")
            else:
                print("Ocorreu um erro durante a alteração do contato. A agenda não foi alterada.")
        else:
            print(f"{forma_incluida} nõa é uma forma de contato suportada pelo sistema. A agenda não foi alterada.")
    else:
        print(f"O contato {nome} não está na agenda. A agenda não foi alterada.")


def usuario_contato_para_texto(agenda:dict): #Permite que o usuário escolha um contato para exibir em formato de texto.
    nome = input("Informe o nome do contato que deseja exibir: ")
    if nome in agenda.keys():
        print(contato_para_texto(nome, **agenda[nome]))
    else:
        print(f"O contato {nome} não está na agenda.")


def agenda_para_txt(nome_arquivo:str, agenda):
    if "txt" not in nome_arquivo:
        nome_arquivo = f"{nome_arquivo}.txt"
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(agenda_para_texto(**agenda))
        print("Agenda exportada com sucesso!")


def agenda_para_json(nome_arquivo:str, agenda):
    if ".json" not in nome_arquivo:
        nome_arquivo = f"{nome_arquivo}.json"
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(json.dumps(agenda, indent=4, ensure_ascii=False))
        print("Agenda exportada com sucesso!")


def json_para_agenda(nome_arquivo:str):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    print("Agenda carregada com sucesso!")
    return json.loads(conteudo)