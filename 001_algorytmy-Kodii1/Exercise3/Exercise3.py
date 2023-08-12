# Zadanie 3 [3 pkt]
# Problem Józefa Flawiusza. 

# Wyobraź sobie następującą sytuację: jesteś powstańcem żydowskim podczas oblężenia Jotopaty w 67 roku n.e. 
# Zostałeś otoczony wraz z 40 innymi żołnierzami przez legiony rzymskie, ale nie chcecie zostać pojmani. 
# Po krótkiej naradzie wymyśliliście rozwiązanie: ustawicie się w kole i pierwsza osoba zabije tą znajdującą się bezpośrednio po lewej, 
# kolejny żołnierz zabije kompana po swojej lewej, aż do momentu gdy zostanie tylko jeden powstaniec, który popełni samobójstwo. 
# Ty jednak nie chcesz zginąć z ręki innego powstańca ani popełniać samobójstwa. 
# Gdzie w takim razie ustawić się w tym kręgu, aby uniknąć śmerci? 
# Jak opracować uniwersalny sposób na obliczenie bezpiecznego miejsca w kole dla dowolnej liczby znajdujących się w nim osób? 
# W opisanej wyżej sytuacji znalazł się Józef Flawiusz, rzymsko-żydowski historyk, od którego wzięła się nazwa problemu.

# Napisz program rozwiązujący ten problen dla dowolnej liczby żołnierzy.


def repairRange(n):
    if n > 0:
        return suisideMission(n)+1 
    else:
        return "It's not passive number"

def suisideMission(n):
    if n == 1:
        return 0
    else:
        return (suisideMission(n-1) + 2) % n 
        
if __name__ == "__main__":
    n = int(input("Write number of people in circle: "))
    print(repairRange(n))
