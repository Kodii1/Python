

def sortDates(date):
    for j in range(len(date),0,-1):
        for i in range(j-1):
            if date[i]["r"] > date[i+1]["r"]:
                date[i],date[i+1]=date[i+1],date[i]
            elif date[i]["r"] == date [i+1]["r"]:

                if date[i]["m"] > date[i+1]["m"]:
                    date[i],date[i+1]=date[i+1],date[i]
                elif date[i]["m"] == date [i+1]["m"]:
                    
                    if date[i]["d"] > date[i+1]["d"]:
                        date[i],date[i+1]=date[i+1],date[i]
    return date

if __name__ == "__main__":
    dates =  []
    howMany = int(input("Write how many dates You want to add: "))

    for i in range(0,howMany):
        print(f"for {i+1} date:")
        day = int(input("Write day: "))
        month = int(input("Write month: "))
        year = int(input("Write year: "))
        dates.append({"d":day,"m":month,"r":year})

    print(sortDates(dates))
