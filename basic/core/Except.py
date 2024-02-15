# python Except.py
# (base) C:\kd\ws_python\core>python Except.py
while True:
  try: 
      # 예외 발생 예상 코드
      tot = int(input('총점을 입력하세요: '))
      cnt = int(input('과목수를 입력하세요: '))
      
      if cnt == 9999:
        break
      
      avg = tot / cnt
      
      print(f'총점: {tot}')
      print(f'과목수: {cnt}')
      
  except Exception as e:  # 예외 발생
      print(e) # 예외 원인 출력
      
  else: # 예외가 발생하지 않은 경우
      # {0:.1f}: 실수형으로 소수 첫째자리까지 출력, 반올림 처리됨.
      print('평균은 {0:.1f} 입니다.'.format(avg))
      
  finally: 
      print('무조건 실행...') # IO 파일 닫기, DBMS, Socket 닫기
      
print('정상적으로 작동중...')  
  