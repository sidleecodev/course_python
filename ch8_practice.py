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

class Arm():
    def __init__(self, type, function):
        self.type = type
        self.function = function

class Robot():
    def __init__(self, name, arm):
        self.name = name
        self.arm = arm
    def show_arm(self):
        print(f'{self.name}擁有一隻{self.arm.type}的手臂，功能是{self.arm.function}')

arm = Arm("鐵製", "舉重")
bot = Robot("RX-78", arm)
bot.show_arm()
