class Person(object):
    def __init__(self,age=1):
        self.age=age
    
    def drive(self):
        if self.age >= 18:
            print('ok')
        else:
            raise Exception('No drive')
        

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

class Adult(Person):
    def __init__(self, age=18):
        if age>=18:
            super().__init__(age) #18살이라는 값을 person에 인자로 넘겨주어, self.age를 설정할수 있도록 함함
        else:
            raise ValueError


class Car(object):
    def __init__(self):
        pass
    def ride(self, person):
        person.drive()


if __name__ == "__main__":
    baby = Baby()
    adult = Adult()
    car = Car()
    car.ride(adult) # ok , baby가 들어가있을 경우 ValueError