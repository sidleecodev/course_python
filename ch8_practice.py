# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 09:11:53 2026

@author: user
"""

# =============================================================================
# class Pet():
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#     def speak(self):
#         return '我是寵物'
# 
# pet1 = Pet("小白", "狗")
# pet2 = Pet("咪咪", "貓")
# pet3 = Pet("啾啾", "鳥")
# 
# print(f'寵物名：{pet1.name}, 種類：{pet1.species}')
# print(f'說「{pet1.speak()}」')
# print(f'寵物名：{pet2.name}, 種類：{pet2.species}')
# print(f'寵物名：{pet3.name}, 種類：{pet3.species}')
# 
# 
# class RobotDog(Pet):
#     def __init__(self, name, battery):
#         super().__init__('機器'+name, '機器狗')
#         self.battery = battery
#     def speak(self):
#         return '汪！我是機器狗，服務至上'
#     def charge(self):
#         self.battery += 30
#         print(f'{self.name}正在充電，剩餘電量：{self.battery}%')
#         
#         
# robot = RobotDog("小白", battery = 50)
# print(f'寵物名：{robot.name}, 種類：{robot.species}')
# print(f'說「{robot.speak()}」')
# robot.charge()
# 
# 
# pet4 = Pet("小黑", "狗狗")
# pet5 = Pet("啾啾", "小鳥")
# pet6 = Pet("泡泡", "金魚")
# 
# class Dog():
#      def __init__(self, name):
#          self.name = '狗狗' + name
# 
#      def introduce(self):
#          return self.name
#      def perform(self):
#          return '汪汪叫！'
# 
# class Bird():
#      def __init__(self, name):
#          self.name = '小鳥' + name
# 
#      def introduce(self):
#          return self.name
#      def perform(self):
#          return '高空飛行！'
# 
# class Fish():
#      def __init__(self, name):
#          self.name = '金魚' + name
# 
#      def introduce(self):
#          return self.name
#      def perform(self):
#          return '假裝死...'
# 
# def talent_show(animal):
#     print(f'我是{animal.introduce()}！現在來表演：{animal.perform()}')
#     
# a = Dog('小黑')
# talent_show(a)
# b = Bird('啾啾')
# talent_show(b)
# c = Fish('泡泡')
# talent_show(c)
# =============================================================================

# =============================================================================
# class Wizard():
#     def __init__(self, name, real_name):
#         self.name = name
#         self.__real_name = real_name;
#     def reveal(self):
#         return self.__real_name;
# 
# w = Wizard("哈利波特", "哈利‧詹姆士‧波特")
# print(f'名字是 {w.name}，真名是 {w.reveal()}')
# =============================================================================

# =============================================================================
# class Character():
#     def __init__(self, name, id_code):
#         self.__name = name
#         self.__id_code = id_code
# 
#     def __eq__(self, other):
#         return (self.__name == other.__name
#                 and self.__id_code == other.__id_code
#                 )
#     
# char1 = Character("哈利", "001")
# char2 = Character("哈利", "001")
# print(char1 == char2)
# =============================================================================

# =============================================================================
# class Arm():
#     def __init__(self, type, function):
#         self.type = type
#         self.function = function
# 
# class Robot():
#     def __init__(self, name, arm):
#         self.name = name
#         self.arm = arm
#     def show_arm(self):
#         print(f'{self.name}擁有一隻{self.arm.type}的手臂，功能是{self.arm.function}')
# 
# arm = Arm("鐵製", "舉重")
# bot = Robot("RX-78", arm)
# bot.show_arm()
# =============================================================================

# =============================================================================
# class zooCounter():
#     total_animals = 0
#     def __init__(self):
#         zooCounter.total_animals += 1
#     @classmethod
#     def show_count(cls):
#         print(f"現在有{cls.total_animals}隻動物")
#     @staticmethod
#     def announcement():
#         print("\n動物園正在廣播...")
#         
# zooCounter.announcement()
# a = zooCounter()
# zooCounter.show_count()
# b = zooCounter()
# zooCounter.show_count()
# =============================================================================

class TooWeakException(Exception):
    pass

class Creature():
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def check_power(self):
        if self.power < 50:
            raise TooWeakException(f"{self.name} 力量太低，只有{self.power}，攻擊失敗!")

    def attack(self):
        print(f"{self.name} 發動攻擊!")
        self.check_power()

class Dragon(Creature):
    def __init__(self, name, power):
        super().__init__(name, power)
    def attack(self):
        print(f"{self.name} 噴出龍焰!")
        self.check_power()
        
class Phoenix(Creature):
    def __init__(self, name, power):
        super().__init__(name, power)
    def attack(self):
        print(f"{self.name} 釋放鳳凰烈焰!")
        self.check_power()

class Trainer:
    count = 0
    def __init__(self, name):
        self.name = name
        self.pets = []
        
    def add_pet(self, pet):
        self.pets.append(pet)
    
    def train_all(self):
        for pet in self.pets:
            try:
                pet.attack()
            except TooWeakException as e:
                print(e)
            else:
                print(f"{pet.name} 攻擊成功!")
                Trainer.count += 1

    @classmethod
    def show_trained_count(cls):
        return cls.count
    
    @staticmethod
    def show_tip():
        print("攻擊會消耗魔力，小心使用!")

pet1 = Dragon("小火龍", 50)
pet2 = Phoenix("鳳凰", 40)

trainer = Trainer("哈利")
trainer.add_pet(pet1)
trainer.add_pet(pet2)

trainer.show_tip()

trainer.train_all()

print(f"成功訓練的寵物數：{Trainer.show_trained_count()}")






