import socket

HOST = '127.0.0.1'  # 로컬 호스트
PORT = 50007        # 사용할 포트

# 소켓 생성 및 설정
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 포트 재사용 옵션 추가
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"서버가 {HOST}:{PORT}에서 대기 중...")

    while True:
        conn, addr = s.accept()
        print(f"클라이언트 연결됨: {addr}")

        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    print("클라이언트 연결 종료")
                    break

                print(f"수신 데이터: {data.decode()} (from {addr})")
                response = f"서버가 받음: {data.decode()}".encode()
                conn.sendall(response)
