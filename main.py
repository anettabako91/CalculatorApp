from calculators.calculator_simplu import CalculatorSimplu
#importam clasa CalculatorSimplu
if __name__ == "__main__": # daca numele coraspunde, rulam codul

    valoare_initiala = float(input("Introduceți valoarea inițială (implicit 0): "))
    #setam valoarea initiala printr-un input - un numar de la tastatura, care trebuie transformat in float (numar zecimal)

    calculator = CalculatorSimplu(valoare_initiala)

    while True:
        input_user = input('> ')
        #input de la utilizator, care va incepe cu semnul > -
        # utilizatorul trebuie sa introduca operatorul(+,-,*,/,=) si numarul
        operator_si_numar = input_user
        operator = operator_si_numar[0]
        numar = operator_si_numar[1:]
        #ca sa obtinem operatorul, trebuie sa desfacem inputul, indexul 0 al inputului va fi operatia
        #numarul va fi compus din caracterele aflate la indexul [1:] al inputului, fara sa specificam end_pos
        #astfel extragem string-ul pana la ultimul caracter inclusiv

        try:
            #incercam sa rulam urmatorul cod, in functie de valoarea operatorului
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

            calculator.afisare_valoare_actuala()
            #se afiseaza valoarea actuala

        except (ValueError, IndexError):
            print("Invalid operation")
            #se executa acest rand cand apare o exceptie - comanda nu poate fi inteleasa sau executata
            #apare un mesaj de eroare