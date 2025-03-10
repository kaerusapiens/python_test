import socket

HOST = '127.0.0.1'  # 서버 주소
PORT = 50007        # 서버 포트

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b'Hello, socket server', (HOST, PORT))
    print(f"서버 {HOST}:{PORT}에 데이터 전송")
    
    data, sever = s.recvfrom(1024)
    print(f"서버 응답 수신: {data.decode()} (from {sever})")