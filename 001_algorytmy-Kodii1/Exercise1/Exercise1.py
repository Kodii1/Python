
# Zadanie 1 [2 pkt]
#Napisz program, który wypisze na ekranie wszystkie liczby pierwsze z zadanego zakresu.


def primeNumbers(minNumber,maxNumber):
    allPrimeNumbers = [] 
    allPrimeNumbers.clear() 
    for number in range(minNumber,maxNumber+1): 
        if number > 1: 
            for i in range(2,number):
                if number % i == 0:
                    break or"
            else: 
                allPrimeNumbers.append(number)
    return allPrimeNumbers

if __name__ == "__main__":
    minNumber = int(input("Write min number: "))
    maxNumber = int(input("Write max number: "))
    print(primeNumbers(minNumber,maxNumber))
