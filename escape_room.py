from datetime import datetime, timedelta
from pathlib import Path

start_time = datetime.now()
time_for_escape = timedelta(seconds= 600)
path = Path(__file__).absolute().parent
filepath = path / 'room.txt'
player_location = 'room'
items = ['nóż']

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
def list_to_string(s):

    return (",".join(s))
    
def remaining_time():
    end_time = start_time + time_for_escape
    return str(end_time -datetime.now())

class Inventory:

    def __init__(self, capacity=6):
        self.capacity = capacity

    def __str__(self) -> str:
        print(f'W twoim plecaku znajdują się {list_to_string(items)}. Zapełnienie plecaka {len(items)}/{self.capacity}')

    def get_item(self, item):
        self.item = item
        if item not in items:
            if len(items) + 1 <= self.capacity:
                if player_location == "stolik" and (self.item == "gazeta" or self.item == 'latarka UV'):
                    items.append(self.item)
                    print(f"Włożyłeś do plecaka przedmiot {self.item}. Zapełnienie plecaka {len(items)}/{self.capacity}")
                else:
                    print ('Nie ma tu takiego przedmiotu do zabrania')
            else:
                print("Masz już zbyt wiele rzeczy musisz się czegoś pozbyć")
        else:
            print(f'{self.item} już znajduje się w twoim plecaku')

    def throw_item(self, item):
        self.item = item
        if item in items:
            items.remove(item)
            print(f"Pozbyłeś się {self.item}. Zapełnienie plecaka {len(items)}/{self.capacity}")
        else:
            print(f'{self.item} nie znajduje się w twoim plecaku')


class Room:

    def __init__(self, name='stary salon'):
        self.name = name

    def __str__(self) -> str:
        with open(filepath, mode = 'r', encoding='utf-8') as file:
            for line in file.readlines():
                print(line, end='')
                
def change_location(place):
    text = []
    global player_location
    player_location = place
    if place == "obraz" or 'stolik' or 'fotel' or 'drzwi':
        try :
            with open(path / (place+'.txt'), mode = 'r', encoding='utf-8') as file:
                for line in file.readlines():
                    text.append(line)
                print(text[0])
        except:
            print('''
    Błędne miejsce!
    Dostępne miejsca do których można podejść:
    obraz
    fotel
    stolik
    drzwi
    ''')

def using_item(item):
    text = []
    if item == "gazeta" and item in items:
        with open(path / "gazeta.txt", mode = 'r', encoding='utf-8') as file:
            for line in file.readlines():
                print(line, end='')
    elif item == "nóż" and player_location == 'fotel' and item in items:
        with open(path / 'fotel.txt', mode = 'r', encoding='utf-8') as file:
            for line in file.readlines():
                text.append(line)
            print(text[3])
            items.append('szkatułka')
    elif item == "latarka UV" and player_location == 'obraz' and item in items:
        with open(path / 'obraz.txt', mode = 'r', encoding='utf-8') as file:
            for line in file.readlines():
                text.append(line)
            print(text[3])
    elif item == 'szkatułka' and item in items:
        code = input("podaj 4 cyfry kodu (pisane ciągiem)")
        if code == '2112':
            print('Otworzyłeś szkatułke w środku znajduję się klucz, wkładasz go do kieszeni')
            items.append('klucz')
        else:
            print('Kłódka ani drgnie, kod mus być inny')
    elif item == "klucz" and player_location == 'drzwi' and item in items:
        code = input('Klucz pasuje, teraz należy wpisać 4 cyfrowy kod: ')
        if code == '1297':
            with open(path / 'drzwi.txt', mode = 'r', encoding='utf-8') as file:
                for line in file.readlines():
                    text.append(line)
                print(text[3])
                print(f"Graulacje! Twój czas pozostały do końca to {remaining_time()}")
                quit()
        else:
            print("Kłódka ani drgnie, to chyba nie ten kod...")
    else:
        if item not in items:
            print("Nie posiadasz takiego przedmiotu")
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
        return change_location(place), action()

    elif choice == "u":
        item = input('Wybierz przedmiot do użycia: ')
        return using_item(item), action()

    elif choice == 'e':
        print("przegrałeś")

    else:
        print("Błędna akcja, spróbuj ponownie."), help(), action()
    
    
    
Room().__str__()
help()
action()