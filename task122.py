import time
from threading import Thread

class Knight_combat(Thread):
    def __init__(self, name, skill, *args, **kwargs):
        super(Knight_combat, self).__init__(*args, **kwargs)
        self.name = name
        self.skill = skill

    def run(self):
        enemy_army = 100
        k = 0
        print(f'{self.name}, на нас напали!')
        time.sleep(1)
        while True:
            if enemy_army != 0:
                enemy_army -= self.skill
                k += 1
                print(f'{self.name}, сражается {k} день(дня), осталось {enemy_army} воинов.')
                time.sleep(1)
            else:
                print(f'{self.name} одержал победу спустя {k} дней!')
                if enemy_army == 0:
                    break
knight1 = Knight_combat(name="Sir Lancelot", skill=10)
knight2 = Knight_combat(name="Sir Galahad", skill=20)

knight1.start()
knight2.start()
knight1.join()
knight2.join()
print('Все битвы закончились!')
