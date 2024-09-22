# Passo a passo do projeto
	## https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 5: Repetir isso até acabar a base de dados

import pyautogui
import time
pyautogui.PAUSE = 2
# Digitar o link:
pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press('enter')

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
# Após pressionar o enter, aguardar 5 segundo:
time.sleep(3)

# Passo 2: clicar na aba de Fazer login
pyautogui.click(x=458, y=318)

#Digitar o email:
pyautogui.write("loakksjuah@gmail.com")
# Passar pra Senha:
pyautogui.press('tab')
#Digitar a Senha e Clicar no enter:
pyautogui.write('vannsusmo123')
pyautogui.press('enter')

# Passo 3: Importar a base de dados
import pandas
produtos = pandas.read_csv('produtos.csv')
print(produtos)

# Passo 4: Cadastrar um produto
for linha in produtos.index:
    pyautogui.click(x=489, y=225)
    # codigo
    codigo = produtos.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press('tab')  
    # marca
    pyautogui.write(produtos.loc[linha,'marca'])
    pyautogui.press('tab')
    # tipo
    pyautogui.write(produtos.loc[linha,'tipo'])
    pyautogui.press('tab')
    # categoria
    pyautogui.write(str(produtos.loc[linha,'categoria'])) #str transforma em string
    pyautogui.press('tab')
    # preco
    pyautogui.write(str(produtos.loc[linha,'preco_unitario']))
    pyautogui.press('tab')
    #custo
    pyautogui.write(str(produtos.loc[linha, 'custo']))
    pyautogui.press('tab')
    # obs
    obs = produtos.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(obs)
    # enviar produto
    pyautogui.press('tab')
    pyautogui.press('enter')
    # rolar pra baixo 
    pyautogui.scroll(-5000)
    #rolar pra cima
    pyautogui.scroll(5000)
