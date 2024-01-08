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


