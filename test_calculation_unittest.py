# import unittest
# import calculation

# release_name = "lession"


# class TestCal(unittest.TestCase):
#     """実行の順番

#     setUp→test_add_num_and_double→tearDown→
#     setUp→test_add_num_and_double_raise→tearDown
#     """
#     def setUp(self):
#         print("setup")
#         self.cal = calculation.Cal()

#     def tearDown(self):
#         print("teardown")
#         del self.cal

#     #@unittest.skip("skip")
#     @unittest.skipIf(release_name=='lession', "skip")
#     def test_add_num_and_double(self):
#         self.assertEqual(
#             self.cal.add_num_and_double(1,1),4
#         )

#     def test_add_num_and_double_raise(self):
#         """ValueErrorの場合、例外が発生する
#         """
#         with self.assertRaises(ValueError):
#             self.cal.add_num_and_double("1","1")
        

# if __name__ == '__main__':
#     unittest.main()