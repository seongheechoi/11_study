class Country:
    """Super Class"""

    name = '국가명'
    population = '인구'
    capital = '수도'

    def show(self):
        print('국가 클래스의 메서드 입니다.')

class Province:
    Province_list = []

class Korea(Country, Province):
    """ Sub Class """

    def __init__(self, name, population, capital):
        super().show()
        self.name = name
        self.population = population
        self.capital = capital

    def show(self):
        print(
            """ 
            국가의 이름은 {} 입니다.
            국가의 인구는 {} 입니다.
            국가의 수도는 {} 입니다.
            """.format(self.name, self.population, self.capital)
        )