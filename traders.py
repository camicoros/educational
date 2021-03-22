"""
Монетная кооперация

link: https://pythonist.ru/monetnaya-kooperacziya/?utm_source=telegram&utm_medium=pythonist

В стену вмонтирован специальный аппарат, выдающий монетки. 
За стеной с каждой стороны стоит человек. 
Оба они могут взаимодействовать с аппаратом.

Если бросить монетку в аппарат, человек, стоящий за стеной, 
получит 3 монетки. И наоборот.

Иллюстрация пользования аппаратом. Зеленый человечек тратит монетку, 
а красный - нет. Красный получает 3 дополнительные монетки.
Если оба человека будут честно тратить свои монетки, 
чтобы второй получил прибыль (т.е. делиться, share), 
оба они будут получать по 2 монетки прибыли по очереди.

Но всегда есть вероятность, что кто-то поступит эгоистично (steal): 
не захочет тратить свои монетки, но с радостью заберет 3 монетки прибыли, 
если второй поделится.

Задание
Допустим, у каждого человека есть по 3 монетки. 
Создайте функцию, которая будет высчитывать прибыль обоих людей. 
На вход функция будет принимать два списка строк. 
Списки будут представлять поведение этих людей (слова share и/или steal)

Примечания
В «минус» никто не уйдет, так что числа всегда будут положительными.
Слова будут передаваться в нижнем регистре.
"""


class Player:
    def __init__(self, name):
        self.balance = 3
        self.name = name

    def spend(self):
        print('{} ({}) -> 1 to bank'.format(self.name, self.balance))
        self.balance -= 1

    def get(self):
        print('{} ({}) <- 3 from bank'.format(self.name, self.balance))
        self.balance += 3

    def check_balance(self):
        if self.balance > 0:
            return True
        else:
            return False


class MoneyMachine:
    def __init__(self, player1, player2):
        print('\nNew traders joined the battle game!\n')
        self.player1 = player1
        self.player2 = player2

    def get_coin_balances(self, list1, list2):
        rounds = zip(list1, list2)
        for i, round in enumerate(rounds, 1):
            print('ROUND #', i, round)
            self.make_deal(round)
        print('\nRESULT: ', self.player1.balance, self.player2.balance)

    def make_deal(self, commands):
        command1 = commands[0]
        command2 = commands[1]
        if command1 == command2:
            if command1 == 'steal':
                print('---both stealers---')
            elif command1 == 'share':
                print('---both sharers---')
                check1 = self.player1.check_balance()
                check2 = self.player2.check_balance()
                if check1:
                    self.player1.spend()
                    self.player2.get()
                if check2:
                    self.player2.spend()
                    self.player1.get()
        else:
            print('---sharer vs stealer---')
            if command1 == 'share':
                if self.player1.check_balance():
                    self.player1.spend()
                    self.player2.get()
            else:
                if self.player2.check_balance():
                    self.player2.spend()
                    self.player1.get()
        print('\n')


p1 = Player('mike')
p2 = Player('paul')
m = MoneyMachine(p1, p2)
m.get_coin_balances(["share"], ["share"])

p1 = Player('mike')
p2 = Player('paul')
m = MoneyMachine(p1, p2)
m.get_coin_balances(["steal"], ["share"])

p1 = Player('mike')
p2 = Player('paul')
m = MoneyMachine(p1, p2)
m.get_coin_balances(["steal"], ["steal"])

p1 = Player('mike')
p2 = Player('paul')
m = MoneyMachine(p1, p2)
m.get_coin_balances(["share", "share", "share", "share", "share", "share"],
                    ["steal", "share", "steal", "steal", "share", "steal"])
