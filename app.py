from primeNumberGenerator import generatePrimeNumber
import random as rd

def mdc(n1, n2):  # MDC(Φ(n), e) == 1
    while(n2 != 0):
        r = n1 % n2
        n1 = n2
        n2 = r
    return n1

def generatePublicKey(n): # MDC(Φ(n), e) == 1
    while True:
        e = rd.randrange(2, n)
        if(mdc(n, e) == 1):
            return e

def generatePrivateKey(totiente, e): # d*e = 1 mod(Φ(n))
    d = 0
    while((d * e) % totiente != 1):
        d += 1
    return d

def encrypt(mensagem, e, n):
    msg_cifrada = ''
    for letra in mensagem:
        k = (ord(letra) ** e) % n
        msg_cifrada += chr(k)
    return msg_cifrada

def decode(mensagem, n, d):
    msg_decifrada = ''
    for letra in mensagem:
        k = (ord(letra) ** d % n)
        msg_decifrada += chr(k)
    return msg_decifrada

def rsa ():
    msg = input('Digite a mensagem: ')
    p = generatePrimeNumber()
    q = generatePrimeNumber()
    print(f"p = {p}  q = {q}")

    n = p * q
    totiente = (q - 1) * (p - 1)       # Função totiente de Euler ou função Φ

    e = generatePublicKey(totiente)
    print(f"Chave Publica: ({e}, {n})")

    d = generatePrivateKey(totiente, e)
    print(f'Chave Privada: ({d}, {n})')

    msg = encrypt(msg, e, n)
    print(f'MENSAGEM CIFRADA: ' + msg)

    msg = decode(msg, n, d)
    print(f'MENSAGEM DECIFRADA: ' + msg)

rsa()