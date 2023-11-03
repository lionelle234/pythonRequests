from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import logging


# Configurando o driver para headless
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64")

# Configura as mensagens de login
logging.basicConfig(filename='activity.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
logging.basicConfig(filename='activity.log', level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')
logging.basicConfig(filename='activity.log', level=logging.WARNING, format='%(asctime)s:%(levelname)s:%(message)s')


def saul_goodbot():
    # Variavel de opcao do menu
    choice = ""
    #Loop do Web Scraper
    while choice != "3":
        #Menu de opcoes
        print("----------------------------------------------------------------------")
        print("\nSelecione uma opcao: \n")
        print("1- Procurar por processo. \n")
        print("2- Checar logs de atividade. \n")
        print("3- Sair. \n")
        print("----------------------------------------------------------------------")
        choice = input("Opcao: ")

        #Web Scraper
        if choice == '1':
            #Numero do processo a ser buscado
            print("----------------------------------------------------------------------")
            print("\nDigite o numero do processo: ")
            value = input()
            logging.info(' Pesquisou por: {} \n'.format(value))
            try:
                #Site para consulta de processos
                url = 'https://tjpi.pje.jus.br/1g/ConsultaPublica/listView.seam'

                driver = webdriver.Chrome(options=options)
                driver.get(url)
                sleep(2)
            except (TypeError, NameError, SyntaxError, AttributeError):
                print("Erro: Verifique se o codigo esta correto.")
                logging.error(' Erro de sintaxe (URL/Driver). \n')
                sleep(2)
            else:
                try:
                    #Encontra os elementos de input no site
                    number = driver.find_element(By.ID, "fPP:numProcesso-inputNumeroProcessoDecoration:numProcesso-inputNumeroProcesso")
                    search = driver.find_element(By.ID, "fPP:searchProcessos")
                    sleep(2)
                except (NoSuchElementException, NameError):
                    print("Erro: Nenhum elemento encontrado.")
                    logging.error(' Erro na busca por elemento. \n')
                    sleep(2)
                except (TypeError, SyntaxError, AttributeError):
                    print("Erro: Verifique se o codigo esta correto.")
                    logging.error(' Erro de sintaxe (Find Element). \n')
                    sleep(2)

                else:
                    try:
                        #Insere o numero do processo no formulario e o busca
                        number.send_keys(value)
                        search.click()
                        sleep(2)

                        datas = driver.find_elements(By.CLASS_NAME, 'rich-table-cell')
                        if not datas:
                            print("\nNenhum processo encontrado.")
                            logging.warning(' Numero de processo invalido. \n')
                            sleep(2)
                        else:
                            #Printe de informacoes do processo buscado
                            for data in datas:
                                print("----------------------------------------------------------------------")
                                print(data.text)
                                print("----------------------------------------------------------------------")
                            sleep(2)
                    except (TypeError, NameError, SyntaxError, AttributeError):
                        print("Erro: Verifique se o codigo esta correto.")
                        logging.error(' Erro de sintaxe (Find Element). \n')
                        sleep(2)
        #Checagem de logs de atividade
        elif choice == '2':
            try:
                a = open('activity.log', 'r')
                log_contents = a.read()
                a.close()
                print("----------------------------------------------------------------------")
                print("Logs de atividade: ")
                print("----------------------------------------------------------------------")
                print(log_contents)
                sleep(2)
            except (TypeError, NameError, SyntaxError, AttributeError, EOFError, IOError, ValueError):
                print("Erro: Verifique se o codigo esta correto.")
                logging.error(' Erro de sintaxe (Activity Logs). \n')
                sleep(2)
            except FileNotFoundError:
                print("Erro: Nenhum arquivo encontrado.")
                logging.error(' Erro de arquivo (Activity Logs). \n')
                sleep(2)

        #Encerra o loop
        elif choice == '3':
            print(" \nFim da operacao.")
            exit()
        else:
            pass


saul_goodbot()









