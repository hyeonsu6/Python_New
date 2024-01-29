'''
파일명: Ex01-makeFile.py

파일 입출력(I/O - input/output)
     입력(input) 기존 파일 읽어들이는 것을 말한다.
     출력(output) 파일생성, 내용 추가를 말한다.
'''

'''
file = open('./Python_New/Day01/myFile.txt', 'wt')
print('myFile.txt 파일이 생성되었습니다.')
# close 필수!
file.close()
'''
# with 문 - 자동으로 close()를 해준다.
with open('myFile.txt', 'wt', encoding='UTF-8') as file:
    print('myFile.txt 파일이 생성되었습니다.')
