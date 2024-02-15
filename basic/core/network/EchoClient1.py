import socket, sys

HOST = sys.argv[1]  # 'localhost'
PORT = 9009

# python EchoClient1.py localhost
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:  # 자동 close
  sock.connect((HOST, PORT))  # 연결

  while True:
    msg = input('메시지 입력: ') # 입력 대기
  
    sock.sendall(msg.encode())  # 한글 -> 16진수 코드로 변환 -> 서버로 전송
    data = sock.recv(1024)      # 1024 byte 단위로 수신 대기
    print('에코 서버로부터 받은 데이터 [%s]' % data.decode())
