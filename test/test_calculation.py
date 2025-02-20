import unittest
import calculation
import pytest

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

# pytestは関数形でテストができる
def test_add_num_and_double():
    cal= calculation.Cal()
    assert cal.add_num_and_double(1,1) == 4