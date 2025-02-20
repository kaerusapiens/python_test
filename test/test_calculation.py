import unittest
import calculation

release_name = 'dev'
class TestCal(unittest.TestCase):
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
    @unittest.skipIf(release_name=='dev')
    def test_add_num_and_double_raise(self):
        """異常エラー:with文"""
        #cal = calculation.Cal() setUpで定義したため不要
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1','1')
    
