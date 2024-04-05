
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

def criar_dicionario_letras(cifra):
    letras = "abcdefghijklmnopqrstuvwxyz"
    dicionario = {}
    for i, letra in enumerate(letras, start=1):
        dicionario[letra] = chr(ord('a') + (i + cifra - 1) % 26)
    return dicionario

def limpar_texto(texto):
    # Remove espaços e pontuações
    texto_limpo = re.sub(r'[^a-zA-Z0-9\sáàâãéèêíïóôõöúüçÁÀÂÃÉÈÊÍÏÓÔÕÖÚÜÇ]', '', texto)    
    return unidecode(texto_limpo).lower()

def criar_matriz(texto, num_colunas):
    palavras = texto.split()  # Divide o texto em palavras
    matriz = []
    linha_atual = []
    for palavra in palavras:
        for char in palavra:
            linha_atual.append(char)
            if len(linha_atual) == num_colunas:
                matriz.append(linha_atual)
                linha_atual = []
    if linha_atual:
        matriz.append(linha_atual)  # Adiciona a última linha, se houver caracteres restantes
    return matriz

def exibe_matriz_original(matriz):    
    for linha in matriz:
        for char in linha:
            print(f"{style.GREEN}{char}", end="")
        print(f"{style.RESET} ", end="")
    print()

def exibe_matriz_codificada(matriz_resultante, dicionario):
    for linha in matriz_resultante:
        for char in linha:
            if char.isalpha():  # Verifica se é uma letra
                numero = dicionario[char]
                print(f"{style.YELLOW}{numero}", end="")  # Imprime o número codificado
            else:
                print(char, end="")  # Mantém espaços e outros caracteres
        print(f"{style.RESET} ", end="")  # Espaço entre as linhas   

# Usuario informa texto
os.system('cls')
texto_usuario = input("Digite um texto: ")

# Usuario informa qtd colunas
num_colunas = int(input("Digite a quantidade de colunas para a matriz: "))

#Usuario informa a cifra
cifra = int(input("Digite a cifra: "))

# Cria o dicionário
dicionario = criar_dicionario_letras(cifra) 

# Limpa texto
texto_limpo = limpar_texto(texto_usuario)

# Cria matriz
matriz_resultante = criar_matriz(texto_limpo, num_colunas)

#Exibe matriz decodificada
print("Texto decodificado: ")
exibe_matriz_original(matriz_resultante)

#Exibe matriz codificada
print("Texto codificada: ")
exibe_matriz_codificada(matriz_resultante, dicionario)
            