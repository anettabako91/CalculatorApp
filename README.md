# CalculatorApp

## Descriere
\
Am creat proiectul calculator simplu, care reprezinta o aplicatie
de tip mini - calculator, implementata in limbajul de programare Python. 
Calculatorul la pornire afiseaza valoarea intiala, care este implicit 0,
dar acesta poate fi setata si prin intermediul unui parametru din linia 
de comanda. Apoi aplicatia asteapta o operatie de la utilizator si 
afiseaza rezultatul acestuia.\
Calculatorul permite efectuarea operatiilor simple de adunare, scadere, 
inmultire, impartire si setarea valorii curente.\
Pentru a iesi din aplicatie, putem introduce comanda "x", dupa care aplicatia
ne returneaza mesajul de "La revedere" si valoarea actuala al calculatorului.\
In cazul in care o comanda nu poate fi inteleasa sau executata, aplicatia ne
va returna un mesaj de eroare.

## Utilizarea aplicatiei
1. Ruleaza scriptul calculator_simplu.py intr-un mediu Python.
2. Introdu valoarea initiala,cand aceasta este solicitata.
3. Introdu comenzi aritmetice pentru a efectua operatii pe 
valoarea curenta a calculatorului.
4. Pentru a iesi din aplicatie, introdu comanda "x".


## Comenzi acceptate
- adunare: +număr - adună la valoarea curentă numărul respectiv
- scadere: -număr - scade din valoarea curentă numărul respectiv
- inmultire: *număr - înmulțește valoarea curentă numărul respectiv 
- impartire: /număr - împarte valoarea curentă la numărul respectiv
- setare valoare curenta: =număr - setează valoarea curentă cu numărul respectiv
- iesire din program: x

## Exemplu de utilizare

>Introduceți valoarea inițială (implicit 0): 0\
> +8\
valoarea actuala este : 8.0\
> -5\
valoarea actuala este : 3.0\
> *6\
valoarea actuala este : 18.0\
> /2\
valoarea actuala este : 9.0\
> =15\
valoarea actuala este : 15.0\
> x\
La revedere!\
valoarea actuala este : 15.0

## Structura proiectului

=> calculators - un Python Package, care contine 
fisierele:
- __ init __.py
- calculator_simplu.py => acesta este fisierul python unde 
am creat class CalculatorSimplu() și metodele necesare 
pentru operațiile de bază a unui calculator simplu, cum ar fi
operațiile aritmetice +, -, *, / , și metoda de afișare a 
rezultatului.

```python
class CalculatorSimplu: #cream clasa CalculatorSimplu
    def __init__(self, valoare_initiala): #setam constructorul - valoarea initiala care va fi egala cu valoarea actuala
        valoare_initiala = 0
        self.valoare_actuala = valoare_initiala

    def adunare(self, numar): #definim metoda de adunare
        self.valoare_actuala += numar

    def scadere(self, numar): #definim metoda de scadere
        self.valoare_actuala -= numar

    def inmultire(self, numar): #definim metoda de inmultire
        self.valoare_actuala *= numar

    def impartire(self, numar): #definim metoda de impartire
        self.valoare_actuala /= numar

    def seteaza_valoare_actuala(self, valoare): #definim metoda de setarea valorii actuale
        self.valoare_actuala = valoare

    def afisare_valoare_actuala(self): #definim metoda de afisare a valorii actuale
        print(f'valoarea actuala este : {self.valoare_actuala}')
```

=> main.py - fisierul principal Python, in care rulam aplicatia.
In acest fisier am facut urmatoarele comenzi:
- am importat clasa CalculatorSimplu
prin comanda: 
```python
from calculators.calculator_simplu import CalculatorSimplu
```
- am setat valoarea initiala printr-un input - 
un numar de la tastatura, care trebuie transformat in float
(numar zecimal) prin comanda: 
```python
valoare_initiala = float(input("Introduceți valoarea inițială (implicit 0): "))
```
- am cerut operatii de la utilizator printr-un input
```python
input_user = input('> ')
```
- pentru a obtine operatorul, desfacem inputul, 
indexul 0 al inputului va fi operatia, iar numarul va fi 
compus din caracterele aflate la indexul [1:] al inputului,
fara sa specificam end_pos,astfel extragem string-ul pana 
la ultimul caracter inclusiv
```python
operator_si_numar = input_user \
operator = operator_si_numar[0]\
numar = operator_si_numar[1:]
 ```
- rulam codul, in functie de valoarea operatorului
```python
           if operator == "x": # daca este x -> iesire din program
                 print("La revedere!")
           elif operator == "+": # daca este + -> se foloseste metoda de adunare
              calculator.adunare(float(numar))
           elif operator == "-": # daca este - -> se foloseste metoda de scadere
               calculator.scadere(float(numar))
           elif operator == "*": # daca este * -> se foloseste metoda de inmultire
               calculator.inmultire(float(numar))
           elif operator == "/": # daca este / -> se foloseste metoda de impartire
               calculator.impartire(float(numar))
           elif operator == "=": # daca este = -> se foloseste metoda de setare a valorii actuale
               calculator.seteaza_valoare_actuala(float(numar))
           else:
               print("Invalid operation") #daca inputul este gresit, apare mesajul de eroare "invalid operation"
               continue
```
- pentru a afisa rezultatul, folosim comanda: 
```python
calculator.afisare_valoare_actuala()
```
- in cazul in care comanda nu poate fi inteleasa sau executata,
se foloseste comanda de mai jos, in urma careia apare un mesaj de eroare: 
```python
except (ValueError, IndexError):
   print("Invalid operation")
```



