import socket, sys

HOST = sys.argv[1]  # 'localhost'
PORT = 9009

# python ExamClient1.py 127.0.0.1
# python ExamClient1.py 192.168.12.168
# python ExamClient1.py 192.168.12.166
if HOST != '':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:  # 자동 close
        sock.connect((HOST, PORT))  # 연결
        data = sock.recv(1024)  # 수신 대기

    values = data.decode().split('/')
    print(type(values))  # <class 'list'>

    count = len(values) # 배열의 길이
    print('len(values): ' + str(count))  # 4
    print('▷ ' + values[0])  # 영화 추천
    print('-----------------------------')
    # 이미테이션 게임/월터의 상상은 현실이된다./악마는 프라다를 입는다.
    for index in range(1, count):  
        print(values[index])

else:
    print('사용법: python ExamClient1.py 192.168.12.168')