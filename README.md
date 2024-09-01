
# Scraper de Imóveis

Este projeto automatiza o processo de extração de listagens de imóveis, incluindo preços e links, do site [Imóveis Martinelli](https://www.imoveismartinelli.com.br/). Os dados são então salvos em uma planilha Excel para análise posterior. Esta ferramenta é útil para profissionais que precisam comparar preços de imóveis como parte de seu trabalho em avaliação imobiliária.

## Funcionalidades

- **Web Scraping**: Usa Selenium para navegar e extrair dados do site.
- **Armazenamento de Dados**: Salva os dados extraídos (preço, link, data) em um arquivo Excel.
- **Fluxo de Trabalho Automatizado**: Automatiza totalmente o processo de coleta de dados do site e armazenamento em um formato estruturado.

## Pré-requisitos

- **Python**: Certifique-se de que você tem Python instalado no seu sistema.
- **Selenium**: Instale o Selenium via pip:
  ```bash
  pip install selenium
  ```
- **ChromeDriver**: Baixe o [ChromeDriver](https://sites.google.com/chromium.org/driver/) que corresponda à versão do seu Chrome e certifique-se de que ele está no PATH do sistema.
- **Openpyxl**: Instale a biblioteca openpyxl para manipulação de arquivos Excel:
  ```bash
  pip install openpyxl
  ```
- **Arquivo Excel**: Crie um arquivo Excel chamado `imoveis.xlsx` com uma planilha nomeada `precos`, onde os dados serão armazenados.

## Como Executar

1. **Configuração**: Certifique-se de que todas as dependências estão instaladas e o arquivo `imoveis.xlsx` está configurado corretamente.
2. **Execute o Script**: Execute o script para iniciar o processo de scraping:
   ```bash
   python nome_do_script.py
   ```
   Substitua `nome_do_script.py` pelo nome do seu script Python.

3. **Saída**: Os dados serão adicionados à planilha `precos` no arquivo `imoveis.xlsx`, com colunas para preço, link e a data da extração.

## Visão Geral do Código

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import openpyxl

# Define o driver do Chrome
driver = webdriver.Chrome()

# Navega até o site
driver.get('https://www.imoveismartinelli.com.br/')

# Encontra os elementos de preço e link
precos = driver.find_elements(By.XPATH, "//div[@class='card-valores']/div[2]")
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
```

## Observações

- **Tratamento de Erros**: Certifique-se de que a estrutura do site não mude, pois isso exigiria ajustes nas consultas XPath.
- **Armazenamento de Dados**: O script adiciona dados, então certifique-se de que a planilha Excel esteja formatada corretamente antes de executar o script várias vezes.
- **Automatização**: Este script pode ser agendado para rodar periodicamente usando agendadores de tarefas como cron (Linux) ou Agendador de Tarefas (Windows).

## Licença

Este projeto é licenciado sob a Licença MIT. Sinta-se à vontade para usar e modificar o código conforme necessário.

---

Sinta-se à vontade para ajustar o README conforme necessário!
