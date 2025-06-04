import random

def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def gerar_chaves():
    p = 61
    q = 53
    n = p * q
    totiente = (p - 1) * (q - 1)
    e = 17
    while mdc(e, totiente) != 1:
        e += 2
    d = modinv(e, totiente)
    return e, d, n

def rsa_encrypt(texto, e, n):
    return [pow(ord(char), e, n) for char in texto]

def rsa_decrypt(cifrado, d, n):
    if not isinstance(cifrado, list):
        raise ValueError("Dados cifrados devem ser uma lista de inteiros.")
    try:
        chars = [chr(pow(c, d, n)) for c in cifrado]
        return ''.join(chars)
    except Exception as e:
        print(f"[Erro] Falha ao descriptografar: {e}")
        return "[ERRO DE DECODIFICAÇÃO]"
