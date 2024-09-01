from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import openpyxl

# Define o driver do Chrome
driver = webdriver.Chrome()

# Navega até o site
driver.get('https://www.imoveismartinelli.com.br/')

# Encontra os elementos de preço e link
precos = driver.find_elements(By.XPATH, "//div[@class='card-valores']/div[2]")  # Ajusta o XPath para a div que contém o preço
links = driver.find_elements(By.XPATH, "//a[@class='carousel-cell is-selected']")

# Carrega a planilha
workbook = openpyxl.load_workbook('imoveis.xlsx')
pagina_imoveis = workbook['precos']

# Itera sobre os elementos e salva os dados na planilha
for preco, link in zip(precos, links):
    preco_formatado = preco.text.strip()  # Remove espaços em branco
    link_pronto = link.get_attribute('href')
    data_atual = datetime.now().strftime('%d/%m/%Y')
    pagina_imoveis.append([preco_formatado, link_pronto, data_atual])

# Salva a planilha
workbook.save('imoveis.xlsx')

# Fecha o driver
driver.quit()