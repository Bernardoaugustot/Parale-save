# montarum sistema python para savar os arquivos do diretorio X para o diretorio Y
# Documentação do Python para trabalhar com arquivos: https://docs.python.org/3/library/functions.html#open

arquivo = open('name.txt','w+')
arquivo.write('teste 1\n')
arquivo.write('teste 2\n')
arquivo.close()