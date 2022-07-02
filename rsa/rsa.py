import random
from sympy import randprime
min_prime = 0
max_prime = 10000
# NOTE : MAX_PRIME BIGGER THAN 10,000 FREEZES. WILL BE BUGFIXED IN THE FUTURE

#Inverse function bugfixed, wont return None
def multiplicative_inverse(e,r):
    for i in range(r):
        if((e*i)%r == 1):
            return i
# Gretest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
#randomly Generate prime numbers
def primesInRange(x, y):
    prime_list = []
    for n in range(x, y):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False

        if isPrime:
            prime_list.append(n)
            
    return prime_list
#Test to see if num is prime

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def genKeys(p,q):
    if not (is_prime(int(p)) and is_prime(int(q))):
        raise ValueError("Numbers P & Q aren't prime")
    elif p == q:
        raise ValueError("Numbers P & Q shouldn't be equal")
    #Calculate N
    n = int(p) * int(q)
    print("N = " + str(n))
    #Calculate the totient of N (phi)
    phi =  ((int(p)-1) * (int(q)-1))
    #E must be coprime with phi(n)
    
    e = random.randrange(1,phi)
    

    #Verify that E and PHi(n) are coprime with Euclid's algorithm
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    #we can generate D using extended euclids algorithm
    d = multiplicative_inverse(e, phi)

    #return the numbers
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]

    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)

if __name__ == "__main__":
    print("my implementation of RSA")
    Gen = input("Randomly generate P & Q or manually enter? R for random, M for manual \n")
    if Gen == "R":
        P = randprime(min_prime,max_prime)
        Q = randprime(min_prime,max_prime)
        if P == Q:
            Q = randprime(min_prime,max_prime)
    elif Gen == "M":
        P = input("Input P (Must be prime) : ")
        Q = input("Input Q (Must be prime, Shouldn't be the same as P)")
    else:
        print("Wrong, Quitting.")
    
    public,private = genKeys(P,Q)
    print(f"Public key = {public} \n Private key = {private}")

    msg = input("Input your plaintext : ")
    encrypted_msg = encrypt(public,msg  )

    print("encrypted message = ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))

    print("decrypted message = ")
    print(decrypt(private,encrypted_msg))


