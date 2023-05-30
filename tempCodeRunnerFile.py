
class BlackBox:
    pass #pass는 구현해야 하는 부분을 잠시 미뤄두기 위해서 사용
b1 = BlackBox() # 변수를 선언하듯 객체 b1을 작성하고 = 뒤에 클래스명 작성
b1.name = '까망이' #변수 선언 b1이라는 객체에 name이라는 변수를 선언함
print(b1.name)
#b1 객체가 BlackBox의 인스턴스가 맞는지 확인하려면
print(isinstance(b1, BlackBox))