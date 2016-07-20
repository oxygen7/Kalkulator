import cmath

def dodawanie():
    dodliczba1 = eval(input("Podaj pierwszą liczbę: "))
    dodliczba2 = eval(input("Podaj drugą liczbę: "))
    dodwynik = dodliczba1 + dodliczba2
    print("Wynik: %s" % dodwynik)
    dodwybor()
    
def dodwybor():
    dodwybor2 = eval(input("Wybierz 1 aby powrócić do menu lub 2 aby wyjść... "))
    if dodwybor2 == 1:
     menu()
    if dodwybor2 == 2:
     exit
    while not dodwybor2 in (1, 2):
        print ("Błąd... uruchamianie restartu")
        dodwybor()

def odejmowanie():
    odeliczba1 = eval(input("Podaj pierwszą liczbę: "))
    odeliczba2 = eval(input("Podaj drugą liczbę: "))
    odewynik = odeliczba1 - odeliczba2
    print("Wynik: %s" % odewynik)
    odewybor()
    
def odewybor():
    odewybor2 = eval(input("Wybierz 1 aby powrócić do menu lub 2 aby wyjść... "))
    if odewybor2 == 1:
     menu()
    if odewybor2 == 2:
     exit
    while not odewybor2 in (1, 2):
        print ("Błąd... uruchamianie restartu")
        odewybor()

def mnozenie():
    mnoliczba1 = eval(input("Podaj pierwszą liczbę: "))
    mnoliczba2 = eval(input("Podaj drugą liczbę: "))
    mnowynik = mnoliczba1*mnoliczba2
    print("Wynik: %s" % mnowynik)
    mnowybor()
    
def mnowybor():
    mnowybor2 = eval(input("Wybierz 1 aby powrócić do menu lub 2 aby wyjść... "))
    if mnowybor2 == 1:
     menu()
    if mnowybor2 == 2:
     exit
    while not mnowybor2 in (1, 2):
        print ("Błąd... uruchamianie restartu")
        mnowybor()

def dzielenie():
    dziliczba1 = eval(input("Podaj pierwszą liczbę: "))
    dziliczba2 = eval(input("Podaj drugą liczbę: "))
    dziwynik = dziliczba1/dziliczba2
    print("Wynik: %s" % dziwynik)
    dziwybor()
    
def dziwybor():
    dziwybor2 = eval(input("Wybierz 1 aby powrócić do menu lub 2 aby wyjść... "))
    if dziwybor2 == 1:
     menu()
    if dziwybor2 == 2:
     exit
    while not dziwybor2 in (1, 2):
        print ("Błąd... uruchamianie restartu")
        dziwybor()

def pierwiastkowanie():
    pieliczba = eval(input("Podaj liczbę: "))
    piewynik = cmath.sqrt(pieliczba)
    print ("Wynik: %s" % piewynik)
    piewybor()

def piewybor():
    piewybor2 = eval(input("Wybierz 1 aby powrócić do menu lub 2 aby wyjść... "))
    if piewybor2 == 1:
     menu()
    if piewybor2 == 2:
     exit
    while not piewybor2 in (1, 2):
        print ("Błąd... uruchamianie restartu")
        piewybor()

def potegowanie():
    potliczba1 = eval(input("Podaj pierwszą liczbę: "))
    potliczba2 = eval(input("Do potęgi?...: "))
    potwynik = potliczba1^potliczba2
    print ("Wynik: %s" % potwynik)
    potwybor()

def potwybor():
     potwybor2 = eval(input("Wybierz 1 aby powrócić do menu lub 2 aby wyjść... "))
    if potwybor2 == 1:
     menu()
    if potwybor2 == 2:
     exit
    while not potwybor2 in (1, 2):
         print ("Błąd... uruchamianie restartu")
         potwybor()

def menu():
    print ("Menu:")
    print ("1.Dodawanie")
    print ("2.Odejmowanie")
    print ("3.Mnożenie")
    print ("4.Dzielenie")
    print ("5.Pierwiastkowanie")
    print ("6.Potęgowanie")
    wybordzialania = eval(input("Wybierz działanie (1-6): "))
    if wybordzialania == 1:
        dodawanie()
    if wybordzialania == 2:
        odejmowanie()
    if wybordzialania == 3:
        mnozenie()
    if wybordzialania == 4:
        dzielenie()
    if wybordzialania == 5:
        pierwiastkowanie()
    if wybordzialania == 6:
        potegowanie()
    while not wybordzialania in (1, 2, 3, 4, 5, 6):
     print ("Błąd... uruchamianie restartu")
     menu()
     
def kalkulator():
 print ("=====================KALKULATOR=====================")
 print ("=====================================================")
 
def wpisuser():
 wybor = eval(input("Wybierz jedną z opcji (1 - Oblicz, 2 - Wyjście): "))
 if wybor == 1:
  menu()
 if wybor == 2:
  exit
 while not wybor in (1, 2):
     print ("Błąd... uruchamianie restartu")
     wpisuser()

kalkulator()
wpisuser()


