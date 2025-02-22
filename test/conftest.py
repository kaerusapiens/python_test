import os
import pytest

# pytest에서 공통적으로 사용할 설정이나 fixture를 정의하는 파일입니다.
#이 파일을 프로젝트의 테스트 디렉토리에 배치하면 pytest가 자동으로 인식하여 적용됩니다.

#pytest_addoption 의 이름을 지켜야함
#테스트 실행 시 환경 변수를 쉽게 설정할 수 있도록 도와줍니다.
#コマンド例：pytest test_calculation.py --os-name=mac
#pytest test_calculation.py --help
def pytest_addoption(parser):
    parser.addoption('--os-name',default='linux',help='os name')



# @pytest.fixture는 뭘까?
# 테스트 실행 전 필요한 준비 작업을 할 때 사용함.
# 테스트 함수에서 고정된 설정값(예: DB 연결, 파일 생성 등)을 공유할 때 유용함.
# yield를 사용하면 테스트가 끝난 후 자동으로 정리(cleanup) 됨.
@pytest.fixture
def csv_file():
    with open(os.path.join("test.csv"),"w+") as c:
        """       
        これでcsv fileを閉じる必要はなくなる。
        """
        print("before test")
        # yield c
        print("after test")


# tmpdir은 어떻게 동작할까?
# tmpdir은 pytest가 자동으로 생성하는 임시 디렉토리임.
# 각 테스트 실행마다 새로운 임시 폴더를 만들어 사용함.
# 테스트가 끝나면 pytest가 임시 디렉토리를 삭제함.