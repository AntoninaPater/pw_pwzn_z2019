"""
Część 1 (1 pkt): Uzupełnij klasę Calculator
tak by obsługiwała podstawowe operacje (podane jako string)
oraz pamięć (memory, atrybut klasy) z interfejsem: dodaj do pamięci , wyczyść pamięć.
Atrybut memory ma być nienadpisywalny.
Część 2 (1 pkt): jeżeli drugi argument działania nie jest podany (None)
użyj wartość z pamięci kalkulatora. Obsłuż przypadki skrajne.
"""

# property nie powinno zmieniac właściwości obiektu
# memory nie edytowanie w prosty sposób (własnością)

class Calculator:
    def __init__(self):
        self.memory = None
        # Podpowiedz: użyj atrybutu do przechowywania wyniku
        # ostatniej wykonanej operacji, tak by metoda memorize przypisywała
        # wynik zapisany w tym atrybucie
        self._short_memory = None

    def run(self, operator, arg1, arg2="Nic"):
        """
        Returns result of given operation.

        :param operator: sign of operation to perform
        :type operator: str
        :param arg1: first argument, must be a numeric value
        :type arg1: float
        :param arg2: optional, second argument, must be a numeric value
        :type arg2: float
        :return: result of operation
        :rtype: float
        """
        if arg2 == "Nic":
            arg2 = self.memory
        if arg2 == None:
            print("brak drugiego argumentu")
            result = None
        else:
            if operator == "+":
                result = arg1 + arg2
            elif operator == "-":
                result = arg1 - arg2
            elif operator == "*":
                result = arg1 * arg2
            elif operator == "/":
                result = arg1 / arg2

        self._short_memory = result
        return result




    def memorize(self):
        """Saves last operation result to memory."""
        self.memory = self._short_memory


    def clean_memory(self):
        """Cleans memorized value"""
        self.memory = None

    def in_memory(self):
        """Prints memorized value."""
        if self.memory == None:
            print("Nie ma nic w pamięci")
        else:
            print(f"Zapamiętana wartość: {self.memory}")


if __name__ == '__main__':
    calc = Calculator()
    b = calc.run('+', 1, 2)
    calc.memorize()
    calc.in_memory()
    c = calc.run('/', 9)
    assert c == 3