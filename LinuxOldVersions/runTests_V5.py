#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import platform
import time
from datetime import datetime

logFile = "/home/autopsy1/Documentos/TestesAutopsy/x/Log/autopsy.log.0"


# Função main

def main():
    numeroDeTestes = verificar_parametros()

    #Abrir script Autopsy
    os.system("/usr/bin/actexec Script\ de\ Inicio.ascr")

    print("Abri o autopsy")

    time.sleep(10)
    __run_scripts(numeroDeTestes)

# Verifica se o número de parâmetros está correto e se os parâmetros estão corretos e devolve o número de testes
def verificar_parametros():
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
        print("Erro: O número de testes tem que ser superior a 0.\nSyntax: 'python3 runTests.py [nr_testes]'")
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




def __run_scripts(numeroDeTestes):

    __verfy_file_exists()

    # Escreve a hora e data corrente no formato 'YYYY-mm-dd H:M:S'
    print("[" + datetime.today().strftime("%Y-%m-%d %H:%M:%S") + "]\n")

    

    print("\nVai iniciar os scripts\n")
    #mete o contador a 1 para iniciar os testes
    counter = 1
    numLines = 1000

   
    while (counter <= numeroDeTestes):
        # Escreve a hora e data corrente no formato 'YYYY-mm-dd H:M:S' - Apenas debug
        print("[" + datetime.today().strftime("%Y-%m-%d %H:%M:%S") + "]\n")

        

        if(counter == 1):	
            os.system("/usr/bin/actexec Script-M1.ascr")
            print("\nVai iniciar o script 1\n" + datetime.today().strftime("%Y-%m-%d %H:%M:%S"))   
        if(counter == 2):	
            os.system("/usr/bin/actexec Script-M2.ascr")
            print("\nVai iniciar o script 2\n" + datetime.today().strftime("%Y-%m-%d %H:%M:%S")) 
        if(counter == 3 ):	
            os.system("/usr/bin/actexec Script-M3.ascr")
            print("\nVai iniciar o script 3\n" + datetime.today().strftime("%Y-%m-%d %H:%M:%S")) 
        if(counter == 4):	
            os.system("/usr/bin/actexec Script-M4.ascr")
            print("\nVai iniciar o script 4\n" + datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
        if(counter == 5):	
            os.system("/usr/bin/actexec Script-M5.ascr")
        if(counter == 6):	
            os.system("/usr/bin/actexec Script-M6.ascr")
        if(counter == 7):	
            os.system("/usr/bin/actexec Script-M7.ascr")
        if(counter == 8):	
            os.system("/usr/bin/actexec Script-M8.ascr")
        if(counter == 9):	
            os.system("/usr/bin/actexec Script-M9.ascr")
                
	    #espera um bocadinho que o módulo tenha tempo de começar
        time.sleep(10)
        
        

        while (numLines != counter):
            
            print("numLines atual ")
            os.system("grep -c \"DataSourceIngestJob finishFirstStage\" " + logFile + "")

            with open("/home/autopsy1/Documentos/TestesAutopsy/x/Log/autopsy.log.0") as f:
                contents = f.read()
                count = contents.count("DataSourceIngestJob finishFirstStage")
                print("contagem do numero de vezes que encontrou finish=", count)
            numLines = count
            print("numLines toma o valor do num finish ", numLines)
            print("contador atual de modulos", counter)
            if(numLines != counter):
                time.sleep(300)
    
        counter += 1		
        print("Terminou o loop, o contador de modulos passa a ", counter)


    if (platform.system() == "Darwin" or platform.system() == "Linux"):
        # Vai buscar a data e hora do início do módulo e escre para o ficheiro 'FinishedFile.txt'
        os.system("grep \"DataSourceIngestJob startFirstStage\" " + logFile + " >> FinishedFile.txt")

        # Vai buscar a data e hora do fim do módulo e escre para o ficheiro 'FinishedFile.txt'
        os.system("grep \"DataSourceIngestJob finishFirstStage\" " + logFile + " >> FinishedFile.txt")
    else:

        # Vai buscar a data e hora do início do módulo e escre para o ficheiro 'FinishedFile.txt'
        os.system("findstr \"DataSourceIngestJob startFirstStage\" " + logFile + " >> FinishedFile.txt")

        # Vai buscar a data e hora do fim do módulo e escre para o ficheiro 'FinishedFile.txt'
        os.system("findstr \"DataSourceIngestJob finishFirstStage\" " + logFile + " >> FinishedFile.txt")

    
    print("Realizados", numeroDeTestes, " testes\n")


# Chama a função main
if __name__ == "__main__":
    main()
