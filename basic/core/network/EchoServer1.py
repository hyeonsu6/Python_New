import socket

HOST = '' # 서버임으로 생략, 자기 자신에게 연결
PORT = 9009

# python EchoServer1.py
def runServer():
  # sock 객체 생성, 실행 종료시 자동 close
  # socket.AF_INET: IP v4 32 bit
  # socket.SOCK_STREAM: TCP 통신 설정(일반적인 데이터 통신)
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    print('서버 타입:', type(sock)) # <class 'socket.socket'>
    sock.bind((HOST, PORT))  # 연결
    sock.listen(1)  # 최대 동시 연결 수 1

    while True:  # 무한 루틴
      print('접속 대기중...')
      conn, addr = sock.accept()  # client 접속 대기, Lock
      print(type(conn)) # <class 'socket.socket'>, 데이터 송수신
      print(type(addr)) # <class 'tuple'>

      with conn:
        print(f'{addr[0]}와 연결됨') # Client IP
        while True:
          data = conn.recv(1024)  # 1024 바이트 수신 대기
          if not data:  # Client와 연결이 종료되면 실행, not False -> True
              break;  # while 종료
          
          print('type(data):', type(data))
          print(f'메시지 수신: {data.decode()}') # 수신 데이터 출력, 한글 처리

          msg = "나의 서버: ".encode() + data
          conn.sendall(msg)  # client에게 다시 전송, 전송 완료후 None 리턴
          print(f'메시지 전송: {msg}') # 전송된 데이터 출력, 한글 처리
          
runServer()