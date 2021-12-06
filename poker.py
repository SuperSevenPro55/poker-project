def game_begining(gamers, score, a):
    gamers=int(input('Введите количество игроков: ')) # определяем игроков
    score=int(input('Введите количество фишек у игроков: '))# раздаем фишки
    a=list() #вспомогательный список
    for i in range(gamers):
        a.insert(999999999, score)# костыли для раздачи фишек игрокам
        
def dealer_choose(dealer):
    dealer=input('Выберите дилера(номер игрока): ') # определяем дилера 
