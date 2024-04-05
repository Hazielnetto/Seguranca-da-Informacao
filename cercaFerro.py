
import re, os
from unidecode import unidecode

class style:

    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"

def limpar_texto(texto):
    # Remove espaços e pontuações
    texto_limpo = re.sub(r'[^a-zA-Z0-9\sáàâãéèêíïóôõöúüçÁÀÂÃÉÈÊÍÏÓÔÕÖÚÜÇ]', '', texto)    
    return unidecode(texto_limpo).lower()

def criar_matriz(texto, num_trilhos):
    matriz = [[' ' for _ in range(len(texto))] for _ in range(num_trilhos)]

    x, y = 0, 0  # Inicializa as posições x e y

    for char in texto:
        matriz[y][x] = char  # Insere o caractere na posição (x, y)

        # Atualiza as posições x e y
        x += 1
        y += 1

        # Verifica se y ultrapassou o número de trilhos
        if y >= num_trilhos:
            y = 0  

    return matriz

def exibe_texto_original(texto):    
    print(f'''{style.GREEN}{texto}
    {style.RESET}''')

def exibe_texto_codificada(matriz_resultante):
    texto_codificado=''
    for linha in matriz_resultante:
        for char in linha:
            if char.isalpha():
                texto_codificado += char 
    print(f'''{style.YELLOW}{texto_codificado}
    {style.RESET}''')

os.system('cls')

texto_usuario = input("Digite um texto: ")
num_trilhos = int(input("Digite a quantidade de trilhos: "))

texto_limpo = limpar_texto(texto_usuario)
matriz_resultante = criar_matriz(texto_limpo, num_trilhos)

print("Texto Original:")
exibe_texto_original(texto_usuario)

print("Texto Codificado:")
exibe_texto_codificada(matriz_resultante)