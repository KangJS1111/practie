
class VideoMaker:
    def make(self):
        print('추억용 여행 영상 제작')

class MailSender:
    def send(self):
        print('메일 발송')

class BlackBox:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class TravelBlackBox(BlackBox,VideoMaker,MailSender):
    def __init__(self,name,price,sd):
     super().__init__(name,price)
     self.sd = sd
    
     def set_travel_mode(self,min):
        print(str(min)+'분 동안 여행모드 ON')
b1 = TravelBlackBox('하양이', 100000, 64)
b1.make()
b1.send()