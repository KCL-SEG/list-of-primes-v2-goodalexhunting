"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
def isprime(n):  
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True

def primes(number_of_primes):
    # try:
    if number_of_primes < 1:
        raise ValueError("Number of prime numbers must be greater than one.")   
    i=2 
    list=[] 
    while(len(list) != number_of_primes):  
        if(isprime(i)):  
            list.append(i) 
        i+=1
    return list
    # except ValueError:
    #     print("Input value must be an integer")

print(primes(-2))