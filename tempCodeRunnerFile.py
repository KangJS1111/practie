
class BlackBox:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class TravelBlackBox(BlackBox): #상속 받을 클래스의 괄호안에 상속해줄 클래스를 작성하면 된다
    def set_travel_mode(self,min):
        print(str(min)+'분 동안 여행모드 ON')
    # __init__ 메소드를 기본 블랙박스 클래스에서 상속받았기 때문에 작성하지 않아도 됨
b1 = TravelBlackBox('하양이',100000)#하양이와 가격이 부모 클래스에 존재하는 init메소드의 name과 price라는 멤버변수로 설정됨
print(b1.name,b1.price)
b1.set_travel_mode(20)