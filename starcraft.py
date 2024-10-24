class Unit :
    def __init__(self, name, attack_power, health):
        self.name = name
        self.attack_power = attack_power
        self.health = health    


    def attack(self, target):
        target.health -= self.attack_power
        if target.health <= 0:
            print(f"{self.name} has defeated {target.name}!")

    def move(self, direction):
        print(f"{self.name} moved {direction}.")


    def damaged(self, damage):
        if self.health <= damage:
            self.health -= damage
            print(f"{self.name}가 \
                  {damage}만큼의 피해를 입었습니다.")
        else:
            print(f"{self.name} 파괴 되었습니다.")
            self.health = 0
        

class AttackUnit(Unit):
    def __init__(self, name, attack_power, health, attack_range):
        super().__init__(name, attack_power, health)
        self.attack_range = attack_range

    def attack(self, target):
        target.damaged(self.attack_power)
        print(f"{self.name}가 {target.name}을 공격.")



class Marine(AttackUnit):
    def __init__(self, name, attack_power, health, attack_range, position):
        super().__init__(name, attack_power, health, attack_range)
        self.position = position

    def stimpack(self):
        if self.health > 20 :
            self.health -= 20
            print(f"{self.name} 스팀팩 사용")
        else:
            print(f"{self.name} 체력이 부족해서 스팀팩을 사용 할 수 없음")


class Tank(AttackUnit):
    def __init__(self, name, attack_power, health, attack_range, position):
        super().__init__(name, attack_power, health, attack_range)
        self.position = position
        self.siege = False
        self.siege_mode = False


    def set_siege_mode(self, siege_mode):
        if self.siege_mode == True:
            print(f"{self.name} siege mode 가 이미 개발되어져 있습니다.")
        else:
            self.siege_mode = siege_mode
            self.siege = False
            print(f"{self.name} siege mode {self.siege_mode}!")

    def set_seige(self):
        if self.siege_mode == False:
            print(f"{self.name} siege mode 가 개발 되지 않았습니다.")
        else: 
            print(f"{self.name} siege mode {self.siege}!")



    def siege_mode(self):
        if self.siege == False:
            self.siege = True
        else:
            self.siege = False


# Unit Test

marine1 = Marine("marine1", 10, 100, 2, "1-1")
marine2 = Marine("marine2", 10, 100, 2, "1-2")

tank1 = Tank("tank1", 10, 100, 2, "1-1")
tank2 = Tank("tank2", 10, 100, 2, "1-2")
tank1.set_siege_mode(True)
tank2.set_seige()
tank1.set_seige()
tank1.attack(tank2)


marine1.attack(marine2)
marine2.damaged(20)


    
