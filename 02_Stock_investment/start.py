from blockchain import exchangerates
import timeit

''' 비트코인 가격
tk = exchangerates.get_ticker()
print('1 bitcoin = ', tk['KRW'].p15min, 'KRW')
'''
# import keyword
# print(keyword.__file__)

# import calendar
# print(calendar.month(2020,9))
#
# from datetime import datetime as dt
#
# print(dt.now())
#
# class MyFirstClass:
#     clsVar = 'The best way to predict the future is to invent it'
#
#     def clsMethod(self):
#         print(MyFirstClass.clsVar + '\t- Alan Curtis Kay -')
#
# mfc = MyFirstClass()
#
# print(mfc.clsVar)
# print(mfc.clsMethod())

class A:
    def methodA(self):
        print("Calling A's methodA")
    def method(self):
        print("Calling A's method")

class B:
    def methodB(self):
        print("Calling B's methodB")

class C(A, B):
    def methodC(self):
        print("Calling C's methodC")
    def method(self):
        print("Calling C's overridden method")
        super().method()

c = C()
print(c.methodA())
print(c.methodB())
print(c.methodC())
print(c.method())