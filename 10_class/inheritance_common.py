'''
1. 일반 상속
클래스에서 상속이란, 물려주는 클래스(Parent Class, Super class)의 내용(속성과 메서드)을
물려받는 클래스(Child Class, sub Class)가 가지게 되는 것입니다.
예를 들어 국가라는 클래스가 있고, 그것을 상속받은 한국, 일본, 중국, 미국 등의 클래스를 만들 수 있으며,
국가라는 클래스의 기본적인 속성으로 인구라는 속성을 만들었다면, 항속 받은 한국, 일본, 중국 등등의 클래스에서
부모 클래스의 속성과 메서드를 사용할 수 있음을 말합니다.
기본적인 사용방법은 아래와 같습니다.
자식 클래스를 선언할 때 소괄호로 부모 클래스를 포함시킵니다.
그러면 자식 클래스에서는 부모 클래스의 속성과 메소드는 기재하지 않아도 포함이 됩니다.


class 부모클래스:
    ...내용...

class 자식클래스(부모클래스):
    ...내용...

'''

class Country:
    """Super Class"""

    name = '국가명'
    population = '인구'
    capital = '수도'

    def show(self):
        print('국가 클래스의 메서드 입니다.')

class Korea(Country):
    """ Sub Class """

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print('국가 이름은 :', self.name)

