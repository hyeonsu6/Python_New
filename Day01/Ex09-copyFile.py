'''
파일명 : Ex09-copyFile.py
파일복사
    원본 -> 버퍼 변수(Memory) -> 복사본

open 함수 모드
    b(binary mode) : 해당 파일의 데이터를 바이너리 파일로 인식하고 입출력
'''
buffer_size = 1024 # 1024byte -> 1KB 의미, 2^10
with open('./Python_New/Day01/hello.txt', 'rb') as source:
    with open('./Python_New/Day01/hello2.txt', 'wb') as copy:
        while True:
            buffer = source.read(buffer_size)
            if not buffer:
                break
            copy.write(buffer)
print('hello2.txt 파일이 복사 되었습니다.')