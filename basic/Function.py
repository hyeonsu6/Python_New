# %% [markdown]
# #### 함수
# - 데이터를 전달 받는다. -> 전달받은 데이터를 처리한다. -> 처리 결과를 리턴한다.
# - 한번의 코딩으로 반복적인 데이터 처리가 가능하다.

# %%
# 함수 선언, 코드 실행시 함수가 메모리에 저장됨, 함수 실행은 아님
def login():
  print('로그인 처리됬습니다.')

def logout():
  print('-' * 30)
  print('로그아웃 처리됬습니다.')  

# %%
login()
logout()

# %%
def login(id):
  print(f'{id}님 로그인 처리됬습니다.')

def logout(id):
  print('-' * 30)
  print(f'{id}님 로그아웃 처리됬습니다.')  

# %%
login('user1')
logout('user1')

# %%
def login(id, password):
  if id == 'user1' and password == '1234':  
    print(f'{id}님 로그인 성공')
  else:
    print(f'{id}님 로그인 실패')    

# %%
login('user1', '1234')

# %%
def login(id, password):
  if id == 'user1' and password == '1234':  
    return True
  else:
    return False

# %%
sw = login('user1', '1234')
print(sw)
if sw == True:
  print('로그인 성공')
else:
  print('로그인 실패')

# %%
if sw == True:
  print('댓글 쓰기')
else:
  print('댓글 쓰기 불가능')

# %%
if login('user1', '1111'):
  print('댓글 쓰기')
else:
  print('댓글 쓰기 불가능')

# %%
if False:
  print('댓글 쓰기')
else:
  print('댓글 쓰기 불가능')

# %%
11/3

# %%
def add(a, b):  # 함수
  tot = a + b
  return tot

def sub(a, b):
  su = a - b
  return su

def mul(a, b):
  su = a * b
  return su

def div(a, b):
  su = a / b
  return su

def mok(a, b):
  su = a // b
  return su

def nam(a, b):
  su = a % b
  return su

# %%
print(add(3, 5))
print(sub(4, 3))
print(mul(4, 5))
print(div(11, 3))
print(mok(11, 3))
print(nam(10, 3))

# %%
def calc(a, b):  # 함수
  tot = a + b
  sub = a - b
  mul = a * b
  div = a / b
  mok = a // b
  nam = a % b
  
  return tot, sub, mul, div, mok, nam

# %%
tot, sub, mul, div, mok, nam = calc(10, 3)
print(tot)
print(sub)
print(mul)
print(div)
print(mok)
print(nam)

# %%
# m²/ 3.3 = 평

# 원룸의 width를 입력하세요:6
# 원룸의 height를 입력하세요:4
# 원룸의 크기: 24 m²7.272727272727273 평
width = int(input('원룸의 width를 입력하세요:'))
height = int(input('원룸의 height를 입력하세요:'))
m2 = width * height # 함수 대상
py = m2 / 3.3       # 함수 대상
print(f'원룸의 크기: {m2}m² {py} 평')

# %%
# 함수 기반으로 변경
def calc(width, height):
  m2 = width * height
  py = m2 / 3.3
  
  return m2, py

width = int(input('원룸의 width를 입력하세요:'))
height = int(input('원룸의 height를 입력하세요:'))

m2, py = calc(width, height)

print(f'원룸의 크기: {m2}m² {py} 평')

# %%
# 신체질량지수(BMI) = (몸무게(kg) / 신장의 제곱) * 10000

# 몸무게(kg):64
# 키(신장, cm):167
# BMI: 22.948115744558788

def calcbmi(cm, kg):
    bmi = kg / (cm**2) * 10000
    return bmi

cm = int(input("키를 입력하세요 :"))
kg = int(input("몸무게를 입력하세요:"))

bmi= calcbmi(cm, kg)
print(f'BMI: {bmi}')

# %%
# global 전역 변수의 사용
# 여러개의 함수가 값을 공유할 때 사용

tot=0 # 젼역 변수

def ibgo(cnt):
    global tot # 전역 변수 사용 선언, 생략시 에러 발생, local variable 'tot' referenced before assignment
    tot = tot + cnt # 
    print('입고 {0} -> 재고 {1}'.format(cnt, tot))

def chulgo(cnt):
    global tot
    tot = tot - cnt
    print('출고 {0} -> 재고 {1}'.format(cnt, tot))

# %%
ibgo(1)
ibgo(2)
ibgo(3)

# %%
chulgo(3)
chulgo(2)
chulgo(1)

# %%
import random

data=[-3, -2, -1, 1, 2, 3]  # -1: 출고, 1: 입고

su = random.choice(data)
print(su)


# %%
tot=0 # 젼역 변수

def ibgo(cnt):
    global tot # 전역 변수 사용 선언, 생략시 에러 발생, local variable 'tot' referenced before assignment
    tot = tot + cnt # 

def chulgo(cnt):
    global tot
    tot = tot - cnt
    
for i in range(50):
  su = random.choice(data)
  
  if su < 0:
    chulgo(su*-1)
  else:
    ibgo(su)
    
print(tot)    


