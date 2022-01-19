import random
num = random.SystemRandom()

def teste_miller(n, a):
    exp = n - 1
    while not exp & 1:      # Enquanto o expoente é par pode-se deslocar
        exp >>= 1           # o 1 para a esquerda e acrescenta um zero no final do bit
 
    if pow(a, exp, n) == 1:
        return True
        
    while exp < n - 1: 
        if pow(a, exp, n) == n - 1:
            return True      
        exp <<= 1
        
    return False
    
def miller_rabin(n, k=40):
    for i in range(k):
        a = num.randrange(2, n - 1)
        if not teste_miller(n, a):
            return False
            
    return True

def generatePrimeNumber(bits = 5):
    while True:
        # Garante que a é ímpar.
        a = (num.randrange(1 << bits - 1, 1 << bits) << 1) + 1
        if miller_rabin(a):
            return a
