#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import platform
import time
from datetime import datetime

logFile = "/home/autopsy1/Documentos/TestesAutopsy/x/Log/autopsy.log.0"

# Função main

#Abrir script Autopsy
os.system("/usr/bin/actexec Script\ de\ Inicio.ascr")

print("Abri o autopsy")

time.sleep(120);

def main():
    __run_scripts()

# Verifica se o número de parâmetros está correto e se os parâmetros estão corretos e devolve o número de testes
def __verificar_parametros():
    # Verifica se foi enviado um argumento como parâmetro
    if (len(sys.argv) != 2):
        print("Erro: Parâmetros inválidos!\nSyntax: 'python3 runTests.py [nr_testes]'")
        sys.exit(1)

    # Verifica se o parâmetro é um inteiro
    try:
        numeroDeTestes = int(sys.argv[1])
    except ValueError:
        # Handle the exception
        print("Erro: Número de testes inválido!\nSyntax: 'python3 runTests.py [nr_testes]'")
        sys.exit(2)

    if numeroDeTestes <= 0:
        print("Erro: O número de testes tem que ser superior a 0!\nSyntax: 'python3 runTests.py [nr_testes]'")
        sys.exit(3)

    return numeroDeTestes


# Verifica se o ficheiro enviado por parâmetro existe ou não, caso exista devolve o nome
def __verfy_file_exists():
    # Vai buscar o 2º parâmetro que te o caminho do ficheiro
    if (os.path.exists(logFile)):
        print("[" + datetime.today().strftime("%Y-%m-%d %H:%M:%S") + "]\n")
        print("O ficheiro '" + logFile + "' foi encontrado!\n")
    else:
        print("[" + datetime.today().strftime("%Y-%m-%d %H:%M:%S") + "]\n")
        print("Erro: O ficheiro '" + logFile + "' não existe!\n")
        sys.exit(4)




def __run_scripts():
    numeroDeTestes = __verificar_parametros()

    __verfy_file_exists()

    # Escreve a hora e data corrente no formato 'YYYY-mm-dd H:M:S'
    print("[" + datetime.today().strftime("%Y-%m-%d %H:%M:%S") + "]\n")

    if (platform.system() == "Darwin" or platform.system() == "Linux"):
        

        # Vai buscar a data e hora do início do módulo e escre para o ficheiro 'FinishedFile.txt'
        os.system("grep \"DataSourceIngestJob startFirstStage\" " + logFile + " >> FinishedFile.txt")

        # Vai buscar a data e hora do fim do módulo e escre para o ficheiro 'FinishedFile.txt'
        os.system("grep \"DataSourceIngestJob finishFirstStage\" " + logFile + " >> FinishedFile.txt")
    else:
        # Mostra o conteúdo do ficheiro Log
        os.system("findstr \"close\" " + logFile)

        # Vai buscar a data e hora do início do módulo e escre para o ficheiro 'FinishedFile.txt'
        os.system("findstr \"DataSourceIngestJob startFirstStage\" " + logFile + " >> FinishedFile.txt")

        # Vai buscar a data e hora do fim do módulo e escre para o ficheiro 'FinishedFile.txt'
        os.system("findstr \"DataSourceIngestJob finishFirstStage\" " + logFile + " >> FinishedFile.txt")

    print("\nCorreu tudo vai iniciar os scripts\n")
    counter = 1


    numLines=0
    
    while (counter <= numeroDeTestes):
        # Escreve a hora e data corrente no formato 'YYYY-mm-dd H:M:S'
        print("[" + datetime.today().strftime("%Y-%m-%d %H:%M:%S") + "]\n")
        #passa para a var numLines o numero de vezes que encontrou o "finish"
        numLines=os.system("grep -c \"DataSourceIngestJob finish\" FinishedFile.txt")
        # Chamar o script

        if(counter == 1 && numLines == 0):	
               os.system("/usr/bin/actexec Script\ M1.ascr")
               print("\nVai iniciar o script 1\n" + datetime.today().strftime("%Y-%m-%d %H:%M:%S"))   
        if(counter == 2 && numLines == 1):	
               os.system("/usr/bin/actexec Script\ M2.ascr")
               print("\nVai iniciar o script 2\n" + datetime.today().strftime("%Y-%m-%d %H:%M:%S")) 
        if(counter == 3 && numLines == 2):	
               os.system("/usr/bin/actexec Script\ M3.ascr")
               print("\nVai iniciar o script 3\n" + datetime.today().strftime("%Y-%m-%d %H:%M:%S")) 
        if(counter == 4 && numLines == 3):	
               os.system("/usr/bin/actexec Script\ M4.ascr")
               print("\nVai iniciar o script 4\n" + datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
        if(counter == 5 ):	
               os.system("/usr/bin/actexec Script\ M5.ascr")
        if(counter == 6 ):	
               os.system("/usr/bin/actexec Script\ M6.ascr")
        if(counter == 7 ):	
               os.system("/usr/bin/actexec Script\ M7.ascr")
        if(counter == 8 ):	
               os.system("/usr/bin/actexec Script\ M8.ascr")
        if(counter == 9 ):	
               os.system("/usr/bin/actexec Script\ M9.ascr")

        time.sleep(20)
        os.system("grep \"DataSourceIngestJob startFirstStage\" " + logFile + " >> FinishedFile.txt")

	#espera pelo 'finish' do módulo
        
        x = 256
        while (x != 0 or numLines != counter):
                x = os.system("grep  \"DataSourceIngestJob finish\" " + logFile + " >> FinishedFile.txt")
                time.sleep(30)

        counter += 1		
        print("Script counter\n", counter)

    print("Foram feitos", numeroDeTestes " testes")


# Chama a função main
if __name__ == "__main__":
    main()
