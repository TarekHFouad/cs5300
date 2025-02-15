import math

def numPosNeg(x):
    if x > 0:
        return "Positive"
    elif x < 0:
        return "Negitive"
    else:
        return "Zero"

def primeFinder():
    prime = []
    num = 2
    while len(prime) < 10:
        prime_bool = True
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                prime_bool = False
                break
        if prime_bool:
            prime.append(num)
        num+=1
    return prime

def sumTo100():
    count = 0
    sum = 0
    while count != 101:
        sum +=count
        count+=1
    return sum


