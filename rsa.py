import random
import math

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

# função para verificar se um número é primo
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    # apenas verifica divisores ímpares até a raiz quadrada do número
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

#intervalo para a busca de primos
#definindo um intervalo de números maiores para p e q
#para propósitos de demonstração, podemos usar um intervalo de 100 a 500
#em uma aplicação real, esses primos seriam muito maiores.
MIN_PRIME_VALUE = 100
MAX_PRIME_VALUE = 500

def gerar_chaves():
    p = 0
    q = 0

    # gera o primeiro primo 'p'
    while not is_prime(p):
        p = random.randint(MIN_PRIME_VALUE, MAX_PRIME_VALUE)
    
    # gera o segundo primo 'q', garantindo que seja diferente de 'p'
    while not is_prime(q) or q == p:
        q = random.randint(MIN_PRIME_VALUE, MAX_PRIME_VALUE)

    n = p * q
    totiente = (p - 1) * (q - 1)
    
    # 'e' deve ser coprimo com totiente e 1 < e < totiente
    # vamos manter a busca por um 'e' coprimo, começando por 17.
    e = 17 
    while mdc(e, totiente) != 1:
        e += 2 # incrementa para encontrar um 'e' coprimo
        if e >= totiente: #evita loop infinito se totiente for muito pequeno ou e não for encontrado
            # Em casos raros, se totiente for muito pequeno ou não houver 'e' adequado,
            # você pode precisar gerar novos p e q.
            # Para este exemplo, apenas resetamos e tentamos novamente.
            e = 3 # Reinicia a busca por 'e' se chegar ao limite
            break # Saia do loop interno para tentar novos p, q.

    # Se e não foi encontrado adequadamente (ex: break acima), gere novas chaves
    if mdc(e, totiente) != 1:
        return gerar_chaves()

    d = modinv(e, totiente)
    return e, d, n

def rsa_encrypt(texto, e, n):
    # Converte cada caractere do texto para seu valor ASCII (ord())
    # e então aplica a exponenciação modular.
    # O resultado é uma lista de inteiros.
    return [pow(ord(char), e, n) for char in texto]

def rsa_decrypt(cifrado, d, n):
    #verifica se a entrada cifrada é ums lista de int.
    if not isinstance(cifrado, list):
        raise ValueError("Dados cifrados devem ser uma lista de inteiros.")
    try:
        # Para cada número cifrado na lista, aplica a exponenciação modular
        # com a chave privada (d) para obter o valor ASCII original.
        # Em seguida, converte o valor ASCII de volta para caractere (chr()).
        chars = [chr(pow(c, d, n)) for c in cifrado]
        return ''.join(chars) # Junta os caracteres para formar a mensagem decriptada.
    except Exception as e:
        print(f"[Erro] Falha ao descriptografar: {e}")
        return "[ERRO DE DECODIFICAÇÃO]"