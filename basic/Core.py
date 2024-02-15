# 함수 선언
# 이자 2%, 세금 14%를 산출하는 함수
def calc(wonkum): # 데이터 처리 함수
    ija = int(wonkum * 0.02) # 2 % 이자
    mon = int(ija / 12)
    day = int(ija / 365)
    receive = int(day-(day*0.14)) # 세금 14% 제외
    
    return ija, mon, day, receive

# 출력
def display(wonkum, ija, mon, day, receive): # 출력 함수
    print('원금:', format(wonkum, ','), '원')
    print('년이자:', format(ija, ','), '원')
    print('월이자:', format(mon, ','), '원')
    print('오늘이자:', format(day, ','), '원')
    print('세후이자:', format(receive, ','), '원')
    print('-' * 25)

# 원룸 크기    
def oneroom(width, height):
    m2 = width * height
    py = m2 / 3.3
    
    return m2, py

# 신체질량지수 
def calc_bmi(height, kg):
    bmi = (kg / (height * height)) * 10000
    return bmi   

# 포인트 계산
def calc_book(grade, price):
    if grade == 'P'or grade == 'p':
        pay = price - (price * 0.07)
    elif grade == 'G'or grade == 'g':
        pay = price - (price * 0.06)  
    elif grade == 'S'or grade == 's':
        pay = price - (price * 0.05)  
    elif grade == 'F'or grade == 'f':
        pay = price - (price * 0.02)
    else:
        pay = price
        
    return pay

# 자릿수
def calc_position(score):
    if score >= 0 and score <= 9:
        msg = '1의 자리'
    elif score >= 10 and score <= 99:
        msg = '10의 자리'
    elif score >= 100 and score <= 999:
        msg = '100의 자리'
    elif score >= 1000:
        msg = '1000의 자리이상'

    return msg   

# 전기 사용량
def calc_elect(use):
    price=0
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
  
  