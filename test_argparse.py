import argparse

def main():
    # ArgumentParser 객체 생성
    parser = argparse.ArgumentParser(description="파일을 처리하는 프로그램입니다.")

    # 필수 인자 추가 (파일 이름)
    parser.add_argument("filename", help="입력 파일 이름을 지정하세요.")

    # 선택적 인자 추가 (-o 또는 --output)
    parser.add_argument("-o", "--output", required=True,help="출력 파일 이름을 지정하세요.")


    # verbose모드 추가
    parser.add_argument("-v", "--verbose", action="store_true", help="출력을 자세히 보여줍")

    # 입력값 파싱
    args = parser.parse_args()

    # 결과 출력
    if args.verbose:
        print("파일 처리 프로그램을 실행합니다.")

    print(f"입력 파일: {args.filename}")
    if args.output:
        print(f"출력 파일: {args.output}")

if __name__ == "__main__":
    main()