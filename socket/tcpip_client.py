import socket

HOST = '127.0.0.1'  # 서버 주소
PORT = 50007        # 서버 포트

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"서버 {HOST}:{PORT}에 연결 시도...")
    s.connect((HOST, PORT))
    print("서버 연결 성공!")

    message = "Hello, socket server"
    print(f"서버로 전송: {message}")
    s.sendall(message.encode())


#소켓을 통해 클라이언트 → 서버 또는 서버 → 클라이언트로 데이터가 전송될 때, 데이터를 읽는 함수
#s.recv(1024): 최대 1024바이트(1KB)까지 데이터를 수신
    data = s.recv(1024)
    print(f"서버 응답 수신: {data.decode()}")
