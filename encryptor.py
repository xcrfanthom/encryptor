import random

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1
def generate_primes():
    primes = []
    while len(primes) < 2:
        num = random.randint(100, 500)
        if is_prime(num):
            primes.append(num)
    return primes
def rsa_encrypt(message, public_key):
    return [pow(ord(char), public_key[0], public_key[1]) for char in message]
def generate_keys():
    p, q = generate_primes()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, phi)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi)
    d = mod_inverse(e, phi)
    public_key = e, n
    private_key = d, n
    return public_key, private_key

public_key, private_key = generate_keys()
pk = str(private_key).replace('(','').replace(')','')
message = input("Enter the text to encrypt: ")
encrypted_message = str(rsa_encrypt(message, public_key)).replace('[',', ').replace(']','')
em = pk + encrypted_message

print("Encrypted message:", em)
