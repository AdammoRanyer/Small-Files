import os

def fim():
    sair = input('\npressione a tecla ENTER para sair...')
    exit()

def capturandoTodosArquivos():
    cwd = os.getcwd()
    listaTodos = os.listdir(cwd)
    return listaTodos

def validandoArquivos(tipo, listaTodos):
    listaArq = []
    for x in listaTodos:
        x = x.lower()
        if x.endswith(tipo):
            listaArq.append(x)
    print('-'*50)
    if(len(listaArq) == 0):
        print('nenhum arquivo foi encontrado...')
        fim()
    elif(len(listaArq) == 1):
        print('foram encontrados apenas 1 arquivo...')
        fim()
    else:
        print(f'foram encontrados {len(listaArq)} arquivos...')
        return listaArq

def concatenando(arquivos):
    contador = 1
    for x in arquivos:
        manipulador = open(x, 'r')
        x = manipulador.read()
        manipulador.close()
        arquivo = open('arquivoConcatenado.txt', 'a')
        if(contador < len(arquivos)):
            arquivo.write(x + '\n')
        else:
            arquivo.write(x)
        arquivo.close()
        contador += 1
    print('-'*50)
    print('arquivos concatenados com sucesso!')

def main():
    print('Concatenador de Arquivos txt\n')
    tipo = 'txt'
    todos = capturandoTodosArquivos()
    arquivos = validandoArquivos(tipo, todos)
    concatenando(arquivos)
    fim()

main()
