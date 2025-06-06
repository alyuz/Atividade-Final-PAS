ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '

def cifra_cesar(texto: str, deslocamento: int) -> str:
    resultado = ''
    for caractere in texto:
        if caractere in ALFABETO:
            indice = ALFABETO.index(caractere)
            novo_indice = (indice + deslocamento) % len(ALFABETO)
            resultado += ALFABETO[novo_indice]
        else:
            resultado += caractere
    return resultado

def criptografia(texto: str) -> str:
    return cifra_cesar(texto, 3)

def descriptografia(texto: str) -> str:
    return cifra_cesar(texto, -3)
