class Calculator: # class의 선언
    def __init__(self, su1, su2):  # 생성자: 전역 변수 초기화, self: 전역 변수에 접근하는 객체
        self.su1 = su1  # self.su1: 전역 변수 <- su1: 지역 변수의 값
        self.su2 = su2
       
    def add(self): # self 생략 불가능
        return self.su1 + self.su2
   
    def sub(self):
        return self.su1 - self.su2
   
    def mul(self):
        return self.su1 * self.su2
   
    def div(self):
        return self.su1 / self.su2
   
# 웹을 통하여 입출력하는 클래스는 데이터 처리가 주요 기능으로 구현됨.
class Elect:
    def __init__(self): # 생략 가능
        pass  # 로직이 없는 경우
   
    def calc(self, use):
        price=0  # self 생략시 지역 변수, 메소드간(함수)에 공유 불가능, 함수 안에서만 사용 가능한 변수
        basic=0
        if use <= 200:
            price = 99.3
            basic = 910
        elif use >= 201 and use <= 400:
            price = 187.9
            basic = 1600
        else: # elif use > 400:
            price = 280.6
            basic = 7300
            
        tot = int((use * price) + basic)
        
        return price, basic, tot
   
    