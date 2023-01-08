from datetime import datetime, timedelta
from pathlib import Path

start_time = datetime.now()
time_for_escape = timedelta(seconds= 600)
path = Path(__file__).absolute().parent
filepath = path / 'room.txt'

def help():
    print('''
    Dostępne akcje:
    h - pomoc
    p - sprawdź plecak
    z - zabierz przedmiot
    u - użyj przedmiot
    w - wyrzuć przedmiot
    o - rozejrzy się do okoła
    t - pozostały czas
    m - podejdz w wybrane miejsce
    e - zakończ grę (poddaj się)
    ''')

def remaining_time():
    end_time = start_time + time_for_escape
    return str(end_time -datetime.now())


class Inventory:

    def __init__(self, capacity=6):
        self.capacity = capacity
        self.items = ['latarka', 'nóż']

    def __str__(self) -> str:
        print(f'W twoim plecaku znajdują się {self.items}. Zapełnienie plecaka {len(self.items)}/{self.capacity}')

    def get_item(self, item):
        self.item = item
        self.items.append(self.item)

        print(f"Włożyłeś do plecaka przedmiot {self.item}. Zapełnienie plecaka {len(self.items)}/{self.capacity}")

    def throw_item(self, item):
        self.item = item
        self.items.remove(item)

        print(f"Pozbyłeś się {self.item}. Zapełnienie plecaka {len(self.items)}/{self.capacity}")


class Room:

    def __init__(self, name='stary salon'):
        self.name = name

    def __str__(self) -> str:
        with open(filepath, mode = 'r', encoding='utf-8') as file:
            for line in file.readlines():
                print(line, end='')

    def spot():
        pass


def action():
    choice = input('Wybierz akcje:')
    if choice == 'h':
        return help()

    elif choice == 'p':
        return Inventory().__str__()

    elif choice == 'z':
        item = input("Wybierz przedmiot do zabrania: ")
        return Inventory().get_item(item)

    elif choice == 'w':
        item = input("Wybierz przedmiot do wyrzucenia: ")
        return Inventory().throw_item(item)

    elif choice == "o":
        return Room().__str__()

    elif choice == 't':
        print(f"Tik, tak, tik, tak zostało Ci... {remaining_time()}")

    elif choice == 'm':
        spot = input("Gdzie chcesz podejść: ")
        return Room().spot(spot)

    elif choice == 'e':
        print("przegrałeś")
    else:
        print("Błędna akcja, spróbuj ponownie.")
    
    return action()
    
    
action()
