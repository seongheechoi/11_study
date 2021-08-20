class Human():
    '''사람'''

person1 = Human()
person2 = Human()

person1.language = '한국어'
person2.language = 'English'

person1.name = '서울시민'
person2.name = '영국인'

def speak(person):
    print("{}이 {}로 말을 합니다.".format(person.name, person.language))

# speak(person1)
# speak(person2)
Human.speak = speak
person1.speak()
person2.speak()

