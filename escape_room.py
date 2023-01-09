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

#kod do poprawy - lista resetuje się po przejściu cyklu + gazetę i latarkę można zabrać tylko wtedy kiedy jest się przy stoliku
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

    def spot(self, place):
        self.place = place
        text = []
        if place == "obraz" or 'stolik' or 'fotel':
            try :
                with open(path / (place+'.txt'), mode = 'r', encoding='utf-8') as file:
                    for line in file.readlines():
                        text.append(line)
                    print(text[0])
                with open(path / 'condition.txt', mode = 'w', encoding='utf-8') as file:
                    file.write(place)
            except:
                print('''
    Błędne miejsce!
    Dostępne miejsca do których można podejść:
    obraz
    fotel
    stolik
    ''')

def using(item):
    text = []
    if item == "gazeta":
        with open(path / "gazeta.txt", mode = 'r', encoding='utf-8') as file:
            for line in file.readlines():
                print(line, end='')
    elif item == "nóż":
        with open(path / "condition.txt", mode = 'r', encoding='utf-8') as file:
            if file.read() == "fotel":
                with open(path / 'fotel.txt', mode = 'r', encoding='utf-8') as file:
                    for line in file.readlines():
                        text.append(line)
                    print(text[3])
            else:
                print('Nie można tu użyć tego przedmiotu!')
    elif item == "latarka UV":
        with open(path / "condition.txt", mode = 'r', encoding='utf-8') as file:
            if file.read() == "obraz":
                with open(path / 'obraz.txt', mode = 'r', encoding='utf-8') as file:
                    for line in file.readlines():
                        text.append(line)
                    print(text[3])
            else:
                print('Nie można tu użyć tego przedmiotu!')

def action():
    choice = input('Wybierz akcje:')

    if choice == 'h':
        return help(), action()

    elif choice == 'p':
        return Inventory().__str__(), action()

    elif choice == 'z':
        item = input("Wybierz przedmiot do zabrania: ")
        return Inventory().get_item(item), action()

    elif choice == 'w':
        item = input("Wybierz przedmiot do wyrzucenia: ")
        return Inventory().throw_item(item), action()

    elif choice == "o":
        return Room().__str__(), action()

    elif choice == 't':
        print(f"Tik, tak, tik, tak zostało Ci... {remaining_time()}"), action()

    elif choice == 'm':
        place = input("Gdzie chcesz podejść: ")
        return Room().spot(place), action()

    elif choice == "u":
        item = input('Wybierz przedmiot do użycia: ')
        return using(item), action()

    elif choice == 'e':
        print("przegrałeś")

    else:
        print("Błędna akcja, spróbuj ponownie."), help(), action()
    
    
    
Room().__str__()
help()
action()