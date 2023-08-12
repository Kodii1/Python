#  Zadanie 4 [3 pkt]
# Napisz program, który posortuje n dat. 
# Zdefiniuj i wykorzystaj słownik, która będzie posiadał klucze zawierające informacje na temat dnia, miesiąca i roku. 
# Następnie posortuje dowolnym algorytmem daty rosnąco.

# Uwaga: Napisz algorytm sortujący od podstaw. Nie korzystaj z gotowych rozwiązań dostępnych w Pythonie.

def sortDates(dates):
   for j in range(len(dates),0,-1): # always last item must be in the correct place so we can optimalize this code with -1 position every loop
        for i in range(j-1): # search all dates are they in correct order

                        #year

            if dates[i]["year"] > dates[i+1]["year"]:   # date i+1 is ealier than i
                dates[i],dates[i+1] = dates[i+1],dates[i]
            elif dates[i]["year"] == dates[i+1]["year"]: # years are the same /search months
                
                        #month

                if dates[i]["month"] > dates[i+1]["month"]:   # date i+1 is ealier than i
                    dates[i],dates[i+1] = dates[i+1],dates[i]
                elif dates[i]["month"] == dates[i+1]["month"]: # months are the same /search days

                        #days

                    if dates[i]["day"] > dates[i+1]["day"]:   # date i+1 is ealier than i
                        dates[i],dates[i+1] = dates[i+1],dates[i]
        return dates

if __name__ == "__main__":
    
    dates={}
    howMany = int(input("Write how many dates You want to add: "))
    print (howMany)

    for i in range(0,howMany):
        print(f"for {i+1} date:")
        day = int(input("Write day: "))
        month = int(input("Write month: "))
        year = int(input("Write year: "))
        dates.update({i:{"day":day,"month":month,"year":year}})


    print(sortDates(dates))
