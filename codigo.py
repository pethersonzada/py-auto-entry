#Se ainda não tiver os pacotes pyautogui/pandas instalados, vá no terminal da sua IDE, e digite o comando: "pip install pyautogui" e "pip install pandas".

#Importando os pacotes.

import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5 #Intervalo de 0.5 segundos para cada linha que for executada do python.

#Abrir o navegador (Aqui no exemplo, o navegador Firefox).

pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")

#Entra no sistema da empresa.

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
pyautogui.press("enter")

#Clicar na posição do login/senha e digitar o login.

#Login = pythonimpressionador@gmail.com
#Senha = sua senha

#Point(x=820, y=373) - Login
#Point(x=749, y=482) - Senha
#Point(x=955, y=527) - Botão

pyautogui.click(x=820, y=373) #Posição do mouse na tela (Varia de tela para tela).
pyautogui.write("pythonimpressionador@gmail.com") #Login.

pyautogui.click(x=749, y=482) #Posição do mouse na tela (Varia de tela para tela).
pyautogui.write("sua senha") #Senha.

pyautogui.click(x=955, y=527)

#Importar os dados da tabela.

tabela = pd.read_csv("projetos-python\py-auto-fill\produtos.csv") #(CASO NÃO FUNCIONAR, TENTE ALTERAR O DIRETÓRIO!!)
print(tabela)

linha = 0 

for linha in tabela.index: 
    
     #Selecionar o campo "Código do Produto", digitar o código do produto e passar para o próximo campo até chegar ao fim.

    pyautogui.click(x=828, y=257) #Posição do mouse na tela (Varia de tela para tela).

    codigo = tabela.loc[linha, "codigo"]

    pyautogui.write(str(codigo))
    
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    #Verifica se há observação na linha "obs" da tabela e insere.

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):    #Se não houver, simplesmente não preenche nada e vida que segue :)
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    pyautogui.press("tab")

    #Enviar e rolar de volta para cima.

    pyautogui.press("enter") 
    pyautogui.scroll(5000)
