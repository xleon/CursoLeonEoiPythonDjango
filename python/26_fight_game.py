from colorama import init, Fore, Back, Style
from libs import swapi_client
import msvcrt
import random

init()


class Player:
    def __init__(self, player_id, name, gender, power, lives, gems=0):
        self.player_id = player_id
        self.name = name
        self.gender = gender
        self.power = power
        self.lives = lives
        self.gems = gems


class FightGame:
    DEFAULT_LIVES = 2
    DEFAULT_POWER = 10
    
    def __init__(self, author):
        self.author = author
        self.swapi = swapi_client.Swapi()
        self.players = []
        self.last_player_id = 0

    def run(self):
        print(Fore.CYAN + """___________.__       .__     __      ________                       
\_   _____/|__| ____ |  |___/  |_   /  _____/_____    _____   ____  
 |    __)  |  |/ ___\|  |  \   __\ /   \  ___\__  \  /     \_/ __ \ 
 |     \   |  / /_/  >   Y  \  |   \    \_\  \/ __ \|  Y Y  \  ___/ 
 \___  /   |__\___  /|___|  /__|    \______  (____  /__|_|  /\___  >
     \/      /_____/      \/               \/     \/      \/     \/  by {}""".format(self.author))
        print(Fore.WHITE)
        self.__get_players()
        print('Pulsa 0 para obtener ayuda')

        while True:
            option = msvcrt.getch()
            # print(option)

            if option == b'\x1b': # esc
                break
            if option == b'0':
                self.__menu()
            elif option == b'1':
                self.__add_player()
            elif option == b'2':
                self.__status()
            elif option == b'3':
                self.__fight()

    def __menu(self):
        print("\n\nAyuda:\n")
        print("0. Mostrar ayuda")
        print("1. Añadir jugador")
        print("2. Status")
        print("3. Luchar")
        print("Esc. Salir\n")

    def __add_player(self):
        name = ''
        while len(name) < 1:
            name = input('\n\nEscribe nombre del jugador: ')
        gender = ''
        while len(gender) < 1:
            gender = input('\nElige sexo: (male | female): ')

        self.last_player_id += 1

        player = Player(
            player_id=self.last_player_id,
            name=name,
            gender=gender,
            power=FightGame.DEFAULT_POWER,
            lives=FightGame.DEFAULT_LIVES
        )
        self.players.append(player)
        print(Fore.YELLOW + '{} ha sido añadido'.format(name) + Fore.WHITE)

    def __status(self):
        print(Fore.WHITE + 'Id'.ljust(4), 'Nombre'.ljust(21), 'Sexo'.ljust(9), 'Vidas'.ljust(6), 'Power'.ljust(6),
              'Gemas')
        print('----------------------------------------------------------------------------')
        sorted_players = sorted(self.players, key=lambda x: x.power, reverse=True)
        sorted_players = sorted(sorted_players, key=lambda x: x.lives, reverse=True)
        for p in sorted_players:
            color = Fore.RED if p.lives <= 0 else Fore.WHITE
            print(color + '{}{}{}{}{}{}'.format(
                '{}.'.format(p.player_id).ljust(5),
                p.name.ljust(22),
                p.gender.ljust(10),
                str(p.lives).ljust(7),
                str(p.power).ljust(7),
                str(p.gems).ljust(7)))

    def __fight(self):
        current_players = [x for x in self.players if x.lives > 0]

        # hay más de un jugador?
        if len(current_players) < 2:
            print(Fore.RED + 'No hay suficientes jugadores')
            return

        fighters = random.sample(current_players, k=2)
        player1 = fighters[0]
        player2 = fighters[1]
        damage = random.randint(1, 6)
        player2.power -= damage
        print(Fore.CYAN + '==> {} ha zurrado a {}'.format(player1.name, player2.name) + Fore.WHITE)

        if player2.power <= 0:
            player2.lives -= 1
            player2.power = FightGame.DEFAULT_POWER if player2.lives > 0 else 0

            if player2.lives > 0:
                print(Fore.YELLOW + '{} ha perdido una vida'.format(player2.name) + Fore.WHITE)
            else:
                print(Fore.RED + '{} ha muerto'.format(player2.name) + Fore.WHITE)

            player1.gems += 1
            print(Fore.LIGHTGREEN_EX + '{} ha ganado una gema. Ahora tiene {} en total'.format(player1.name,
                                                                                               player1.gems) + Fore.WHITE)

            # cada 3 gemas le damos una vida
            if player1.gems == 3:
                player1.lives += 1
                player1.gems = 0
                print(Fore.MAGENTA + '{} ha ganado una vida!'.format(player1.name) + Fore.WHITE)

            # comprobar si hay ganador (un solo jugador con vida)
            if len([x for x in self.players if x.lives > 0]) == 1:
                print("\n\n+============================================+");
                print("+============================================+");
                print("+============================================+");
                print("      {} HA GANADO".format(player1.name));
                print("+============================================+");
                print("+============================================+");
                print("+============================================+");

    def __get_players(self):
        print('Obteniendo jugadores desde la api de star wars...')
        people = self.swapi.get_people()
        for person in people:
            self.last_player_id += 1
            player = Player(
                player_id=self.last_player_id,
                name=person[0],
                gender=person[1],
                power=FightGame.DEFAULT_POWER,
                lives=FightGame.DEFAULT_LIVES
            )
            self.players.append(player)
        print('Lista de jugadores preparada!')
        self.__status()


FightGame('Diego').run()
