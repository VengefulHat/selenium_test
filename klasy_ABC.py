import math
import sys





"""
REGUŁA LEGB

czyli: 

Local - 
Enclosing - 
Global - zakres globalny lecz najpier trzeba ją zapisać danymi 
BUilt-in - zakres wbudowany, uruchamia się zaraz po odpaleniu progamu

zmienne
chodzi o kolejność wyszukiwania zmiennych 
można mieć lokalnie a jak i globalnie i built-in zatem najpierw będzie lokalnie sprawdzał

"""

#
# print(sys.__dict__["platform"])
# print('\n')
#
# print(sys.platform)
#
#
# for key in sorted(sys.__dict__.keys()):
#     print(key)



# var1 = 'Python'
# var2 = '3.8'
# var3 = var1 + " " + var2
# print(globals())

print(dir(__builtins__))


import builtins

print(builtins.max(3, 5, 7, 8,))
print(builtins.enumerate('Python'))
print(builtins.list(builtins.enumerate('Python')))
# output po tym wyżej: [(0, 'P'), (1, 'y'), (2, 't'), (3, 'h'), (4, 'o'), (5, 'n')]
print(max)
max = lambda x: min(x) # ale się przypatrz, że z max zrobiło się min!!! aby w kodzie powrócić do narmlanych działań możńa wpisać del max i już
print(max([4, -3]))


# przykład na global
def func():
    global var1
    var1 = 10
    print(var1)

func()
print(var1)
# var1 będzie działało ale tylko po wywołaniu funkcji func()
# przykład na global

def test_locals():
    var1 = 1
    var2 = 2
    print(locals())
    var3 = 4
test_locals()
# teram wyprintowane wszystkie zmienne za locals, dobre dla analizy danych ;_;

"""
Przyppomnienie co robi *args i **kwargs jako ilośc argumentów funkcji
Ilość argumentów jakie spływają do funkci widać w pierwszej funkcji smaple
len popdaje ich liczbę ale z racji tego, że jako element jest to puste to po przeciku pookazuje nic
NIE MUSI SIĘ NAZWYAĆ ARGS, MOŻE JAK CHCE, O WSZYSTKIM DECYDUJE GWIAZDKA

"""


def sample1(*args):
    print(len(args))
    print(args)


sample1(4)
sample1(4, 'a', False, "asd as asdd ")
# output 4
# (4, 'a', False, 'asd as asdd ')

def sample2(*zonk):
    result = ''
    for once in zonk:
        result += str(once)
    return print(result)

# zatem sample2 wszystkie argumenty scala do siebie i zwraca jako tekst

sample2(12, 32, "python", 'maskras')

"""
Czes na **kwargs

"""


def sample3(**kwargs):
    print(len(kwargs))
    print(kwargs)


sample3(var1='Python', var2='isCool')

# tutaj też **kwargs nie jest obowiązkiem a zwyczajem
# 2
# {'var1': 'Python', 'var2': 'isCool'}

"""
Jest też możliwość:...
"""

def  sample4(*args, **kwargs):
    print(args)
    print(kwargs)

sample4(2, 3, 4, key1=3, key2=33)
# output:
# (2, 3, 4)
# {'key1': 3, 'key2': 33}

# można jeszcze zrobić tak:


zone = {'mag': 'aas', 'sds': 'sdadsaa', 'rrfr': 'sdaweae'}


def sample5(**kwargs):
    print(kwargs)


sample5(**zone)

class Phone:
    """Moja  mama jest najkochańsza"""
    pass

phone = Phone()

print(help(phone))

class PPhone(object):
    print(help(object))
    pass

print(type(PPhone))
print(Phone.__module__)
print(Phone.__doc__)

class DomDoMieszkania:

    def __init__(self, typ_projektu):
        self.typ_projektu = typ_projektu

project1 = DomDoMieszkania('hawira')

print(project1.typ_projektu)

project2 = DomDoMieszkania.__new__(DomDoMieszkania) # tworzenie nowego obiektu w tej samej klasie
# teraz tak, w klasie pod init podaliśmy ile potrzbuje ono argumentów aby zaistnieć (zainicjowac obiekt zgodnie z metodą jaka zastosowaliśmy w klasie :O
project2.__init__('wiata')
print(project2.typ_projektu)





