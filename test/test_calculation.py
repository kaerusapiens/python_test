import unittest
import calculation
import pytest
import os 
release_name = 'dev'

# unnittestの場合のクラス。
class CalTest(unittest.TestCase):
    """
    """
    def setUp(self):
        """各テスト実行前に呼び出されるメソッドで、テスト環境を設定する役割"""
        print('setup')
        self.cal = calculation.Cal()
    
    def tearDown(self):
        """テスト実行後に後処理を行うメソッドで、setUp() の反対の役割を持つ。"""
        print('clean up')
        del self.cal

    #@unittest.skip('skipされました') skipをしたい場合
    def test_add_num_and_double(self):
        """正常 - 同じ値なのか
        """
        #cal = calculation.Cal() setUpで定義したため不要
        self.assertEqual(self.cal.add_num_and_double(1,1),4)

    #@unittest.skipIf(release_name=='dev','skip!') 特定条件の場合、Skipしたい場合
    def test_add_num_and_double_raise(self):
        """異常エラー:with文"""
        #cal = calculation.Cal() setUpで定義したため不要
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1','1')

# pytyestの場合
class TestCal(object):
    def setup_method(self,method):
        print('method={}'.format(method.__name__))
        self.cal = calculation.Cal()

    def teardown_method(self,method):
        print('method={}'.format(method.__name__))
        del self.cal

    #@pytest.mark.skip(reason='skip!') skipをしたい場合
    def test_add_num_and_double(self):
        #cal= calculation.Cal() setup_methodを宣言したので不要
        assert self.cal.add_num_and_double(1,1) == 4
    
    #@pytest.mark.skipIf(release_name=='dev',reason='skip!') 特定条件の場合、Skipしたい場合
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            #cal = calculation.Cal()  setup_methodを宣言したので不要
            self.cal.add_num_and_double('1','1')

class TestCalculation(object):
    @classmethod
    def setup_class(cls):
        cls.cal = calculation.Cal()
        cls.test_file_name = "test.txt"
        cls.test_dir = "/./tmp/test_dir"

    @classmethod
    def teardown_class(cls):
        """test_save 테스트가 끝난 후 실제 파일 삭제"""
        test_file_path = os.path.join(".", cls.test_file_name)
        if os.path.exists(test_file_path):
            os.remove(test_file_path)

        """test_save_no_dir 테스트가 끝난 후 실제 파일 삭제"""
        import shutil
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir) #shutil.rmtree()는 디렉터리와 그 안의 모든 파일을 재귀적으로 삭제하는 함수입니다. 


    def test_add_num_and_double(self):
        #cal= calculation.Cal() setup_classを宣言したので不要
        assert self.cal.add_num_and_double(1,1) == 4
    
    def test_save(self):
        """실제 디렉토리에 파일을 저장하는 테스트"""
        self.cal.save(".", self.test_file_name)
        test_file_path = os.path.join(".",self.test_file_name)
        assert os.path.exists(test_file_path) is True

    #test_save메서드 작성후, teardonw을 아래에 실시하여 테스트파일을 직접 삭제해주었으나, 
    # tmp_path 내장 fixture를 사용했다면 코드는 더욱더 간단해짐짐( pytest에서 기본 제공하는 fixture)
    # def test_save(self, tmp_path):
    #     test_file_path = tmp_path / self.test_file_name  # tmp_path 내부에 저장
    #     self.cal.save(tmp_path, self.test_file_name)
    #     assert test_file_path.exists()

    def test_save_no_dir(self):
        self.cal.save(self.test_dir,self.test_file_name)
        test_file_path = os.path.join(self.test_dir,self.test_file_name)
        assert os.path.exists(test_file_path) is True





# pytestは関数形でテストができる
# conftest.pyで指定したpytest_addoptionのデータを取得
def test_add_num_and_double():
    cal= calculation.Cal()
    assert cal.add_num_and_double(1,1) == 4


##########################
######conftest study######
##########################

#------- reqeust.config.getiptionでfixture を定義しメソッド作成
@pytest.fixture
def os_name(request):  # request を引数に取る
    return request.config.getoption("--os-name")  # コマンドラインオプションを取得

# test_os で fixture `os_name` を使用
def test_os_use_fixture(os_name):  
    assert os_name in ["linux", "windows", "mac"]  # 取得した値がリストに含まれるかチェック

#------- pytestconfig.getiptionでfixture を定義
def test_os(pytestconfig):
    os_name = pytestconfig.getoption("--os-name")
    assert os_name in ["linux", "windows", "mac"]

#-----------------------------conftestのfixture利用
def test_csv_file(csv_file):
    csv_file.write("id,name,age\n1,Alice,30\n2,Bob,25\n")
    csv_file.seek(0)
    content = csv_file.read()
    assert "Alice" in content
    assert os.path.exists(csv_file.name)