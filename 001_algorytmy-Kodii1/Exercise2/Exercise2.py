# Zadanie 2 [2 pkt]
# Liczby zaprzyjaźnione to dwie liczby naturalne, gdzie każda z nich jest równa sumie dzielników właściwych drugiej liczby. 
# Napisz program wypisujący liczby zaprzyjaźnione z zadanego zakresu.

def dividesOfNumber(n): 
    divSum=0
    for i in range (1,n):
        if n % i == 0:
            divSum += i
    return divSum


def friendlyNumbers(minRange,maxRange):
    pairs = [] # unique collection 
    for i in range (minRange,maxRange+1):
        divSum = dividesOfNumber(i) 
        if divSum > i and dividesOfNumber(divSum) == i: 
            pairs.append([i,divSum])
    return pairs


if __name__ == "__main__":
    minRange = int(input("Write min range: "))
    maxRange = int(input("Write max range: "))
    print(friendlyNumbers(minRange,maxRange))
