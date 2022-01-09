from selenium import webdriver

#Preencher Formularios com Selenium

navegador = webdriver.Chrome()
navegador.get("https://forms.gle/fTG7MkjZqWaRgg2GA")


#preenchendo o cpf
navegador.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys()

#preencher o email
navegador.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys()

#preencher descrição
navegador.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys()

#preencher valor
navegador.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys()

#clicar no botão
navegador.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()


## fazer a partir de uma planilha e varias vezes:

import pandas as pd
from IPython.display import display 

tabela = pd.read_excel('Emitir.xlsx')
display(tabela)


# para cada cpf na planilha, emitir uma nota fiscal

for i,cpf in enumerate(tabela["CPF"]):
    email = tabela.loc[i, "Email"]
    descrição = tabela.loc[i, "Descrição"]
    valor = tabela.loc[i, "Valor"]

    navegador.get("https://forms.gle/fTG7MkjZqWaRgg2GA")
    

        #preenchendo o cpf
    navegador.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(cpf)

    #preencher o email
    navegador.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(email)

    #preencher descrição
    navegador.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(descrição)

    #preencher valor
    navegador.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(str(valor))

    #clicar no botão
    navegador.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()

        

