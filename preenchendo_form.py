from selenium import webdriver

#Preencher Formularios com Selenium

navegador = webdriver.Chrome()
navegador.get("https://forms.gle/fTG7MkjZqWaRgg2GA")


#preenchendo o cpf
#//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input

navegador.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('32223325521')
#preencher o email
navegador.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('mauricio@hot.com')
#preencher descrição
navegador.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys('Preenchendo as informações com python!!')
#preencher valor
navegador.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('3120')

#clicar no botão
navegador.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click('enviar')

