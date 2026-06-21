class Livro:
    titulo=''
    autor=''
    anop=0
    codigo=''
    status=0

def EncCod(lista,cod):
    for i in range(len(lista)):
        if lista[i].codigo==cod:
            return i
    return -1

def EncAut(lista,aut):
    laut=[]
    cont=0
    for i in range(len(lista)):
        if lista[i].autor==aut:
            laut.append(i)
            cont+=1
    if cont>0:
        return laut
        #laut é uma lista de posições
    else:
        return -1

def CadLivro(lista):
    l=Livro()
    l.titulo=input('Registre o título: ')
    l.autor=input('Registre o autor: ')
    l.anop=int(input('Registre o ano de publicação: '))
    l.codigo=(input('Registre o código: '))
    i=EncCod(lista,l.codigo)
    while i!=-1:
        l.codigo=input('CÓDIGO JÁ EXISTENTE!\nDigite outro código: ')
        i=EncCod(lista,l.codigo)
    lista.append(l)
    print('Livro cadastrado com sucesso!')
    print()

def ConLivro(lista):
    op=int(input('Deseja consultar por:\n(1)Código\n(2)Autor\n--'))
    if op==1:
        cod=input('Informe o Código: ')
        i=EncCod(lista,cod)
        if i!=-1:
            print('--Título:            ',lista[i].titulo)
            print('--Autor:             ',lista[i].autor)
            print('--Ano de Publicação: ',lista[i].anop)
            print('--Código:            ',lista[i].codigo)
            if lista[i].status==0:
                print('--Status:            ','Disponível')
            else:
                print('--Status:            ','Ocupado')
        else:
            print('LIVRO NÃO ENCONTRADO!')
    else:
        if op==2:
            aut=input('Informe o autor: ')
            i=EncAut(lista,aut)
            if i!=-1:
                for q in range(len(i)):
                    print('--Título:            ',lista[i[q]].titulo)
                    print('--Autor:             ',lista[i[q]].autor)
                    print('--Ano de Publicação: ',lista[i[q]].anop)
                    print('--Código:            ',lista[i[q]].codigo)
                    if lista[i[q]].status==0:
                        print('--Status:            ','Disponível')
                    else:
                        print('--Status:            ','Ocupado')
                    print()
            else:
                print('AUTOR NÃO ENCONTADO!')
        else:
            print('OPÇÃO INEXISTENTE!')

def AltLivro(lista):
    cod=input('Informe o código: ')
    i=EncCod(lista,cod)
    if i!=-1:
        op=int(input('Deseja alterar: \n(1)Título\n(2)Autor\n(3)Ano\n(4)Todos os anteriores\n--'))
        if op==1:
            lista[i].titulo=input('Cadastre o novo título: ')
        if op==2:
            lista[i].autor=input('Cadastre o novo autor: ')
        if op==3:
            lista[i].anop=int(input('Cadastre o novo ano de publicação: '))
        if op==4:
            lista[i].titulo=input('Cadastre o novo título: ')
            lista[i].autor=input('Cadastre o novo autor: ')
            lista[i].anop=int(input('Cadastre o novo ano de publicação: '))
        if op<1 or op>4:
            print('OPÇÃO INEXISTENTE!')
    else:
        print('LIVRO NÃO ENCONTRADO!')

def RemLivro(lista):
    cod=input('Informe o código: ')
    i=EncCod(lista,cod)
    if i!=-1:
        lista.pop(i)
        #LLM Gemini usada para tirar dúvida de como remover item de lista
        print('Livro removido com sucesso!')
    else:
        print('LIVRO NÃO ENCONTRADO!')

def LisTudo(lista):
    for i in range(len(lista)):
        print('--Título:            ',lista[i].titulo)
        print('--Ano de Publicação: ',lista[i].anop)
        print()

def EmpLivro(lista):
    cod=input('Informe o Código: ')
    i=EncCod(lista,cod)
    if i!=-1:
        if lista[i].status==0:
            lista[i].status=1
            print('Livro ',lista[i].titulo,' emprestado com sucesso!')
        else:
            print('LIVRO JÁ EMPRESTADO!')
    else:
        print('LIVRO NÃO ENCONTRADO!')

def DevLivro(lista):
    cod=input('Informe o Código: ')
    i=EncCod(lista,cod)
    if i!=-1:
        if lista[i].status==1:
            lista[i].status=0
            print('Livro ',lista[i].titulo,' devolvido!')
        else:
            print('O LIVRO NÃO FOI EMPRESTADO!')
    else:
        print('LIVRO NÃO ENCONTRADO!')

def Menu():
    print('Selecione uma das opções: ')
    print('(1)Cadastrar um livro')
    print('(2)Consultar um livro')
    print('(3)Alterar dados de um livro')
    print('(4)Remover um livro')
    print('(5)Listar todos os livros')
    print('(6)Emprestar um livro')
    print('(7)Devolver um livro')
    print('(8)Sair')
    op=int(input('--'))
    return op

#Início do programa
llivros=[]
while True:
    op=Menu()
    if op>8 or op<1:
        print('OPÇÃO INEXISTENTE!')
    if op==1:
        CadLivro(llivros)
    if op==2:
        ConLivro(llivros)
    if op==3:
        AltLivro(llivros)
    if op==4:
        RemLivro(llivros)
    if op==5:
        LisTudo(llivros)
    if op==6:
        EmpLivro(llivros)
    if op==7:
        DevLivro(llivros)
    if op==8:
        print('Programa Encerrado!')
        break