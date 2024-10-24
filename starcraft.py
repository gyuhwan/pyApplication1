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
           
        if abs(self.position - target.position) <= self.attack_range:
            super().attack(target)
        else:
            print(f"{self.name} cannot attack {target.name} outside of its attack range.")



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

    def set_s

    
