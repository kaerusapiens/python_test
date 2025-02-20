import unittest
import calculation

release_name = "lession"


class TestCal(unittest.TestCase):
    """実行の順番

    setUp→test_add_num_and_double→tearDown→
    setUp→test_add_num_and_double_raise→tearDown
    """

    def test_add_num_and_double(self):
        """add_num_and_dobuleメソッドテスト
        """
        cal = calculation.Cal()
        #正常
        self.assertEqual(cal.add_num_and_double(1,1),4)