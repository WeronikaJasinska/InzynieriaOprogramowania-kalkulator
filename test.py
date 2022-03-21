#To jest pierwsze repozytorium
def hello(name):
	return "Hello"  + str(name)

def dodaj(a,b):
	wynik = float(a) + float(b)
	return wynik


def odejmij(a,b):
	wynik = float(a) - float(b)
	return  wynik

pierwsza = int(input())
druga= int(input())

print (dodaj(pierwsza, druga))

