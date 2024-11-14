import pytest
import calculation
import os
is_release = False


class TestCal(object):

    @classmethod
    def setup_class(cls):
        """クラスの全てのテストを行う前に1回だけ実行される
        """
        print(">>>>>>>>>>>>>>setup_class")
        cls.cal = calculation.Cal()
        cls.test_file_name = "test.txt"

    @classmethod
    def teardown_class(cls):
        print(">>>>>>>>>>>>>>teardown_class")
        del cls.cal


    def setup_method(self,metod):
        """各テストの前に実行される処理
        """
        print("start_method={}".format(metod.__name__))
        self.cal = calculation.Cal()

    
    def teardown_method(self,method):
        """終わったら行う処理
        """
        print("end_method={}".format(method.__name__))
        del self.cal


    def test_simple_add_num_and_double(self):
        assert self.cal.add_num_and_double(1,1) == 4

    #fixtureテスト用
    # def test_add_num_and_double(self,request):
    #     os_name = request.config.getoption("--os-name")
    #     if os_name == "mac":
    #         print("ls")
    #     elif os_name == "windows":
    #         print("dir")
    #     assert self.cal.add_num_and_double(1,1) == 4

    def test_add_num_and_double(self,csv_file):
        print(csv_file)
        assert self.cal.add_num_and_double(1,1) == 4

    def test_save(self,tmpdir):
        self.cal.save(tmpdir,self.test_file_name)
        test_file_path = os.path.join(tmpdir,self.test_file_name)
        assert os.path.exists(test_file_path) is True

    
    #@pytest.mark.skip(reason="skip")
    @pytest.mark.skipif(is_release=False, reason="skip")
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double("1","1")


