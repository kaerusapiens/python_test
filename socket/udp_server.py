import socket

HOST = '127.0.0.1'  # 서버 주소
PORT = 50007        # 서버 포트

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 포트 재사용 옵션 추가
    s.bind((HOST, PORT))
    print(f"서버가 {HOST}:{PORT}에서 대기 중...")
    while True:
        data, addr = s.recvfrom(1024)
        print(f"수신 데이터: {data.decode()} (from {addr})")
        response = f"서버가 받음: {data.decode()}".encode()
        s.sendto(response, addr)