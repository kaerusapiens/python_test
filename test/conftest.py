import os
import pytest

@pytest.fixture
def csv_file(tmpdir):
    with open(os.path.join(tmpdir,"test.csv"),"w+") as c:
        """
        before test
        ->
       <_io.TextIOWrapper name='/tmp/pytest-of-minyoung/pytest-6/test_add_num_and_double0/test.csv' mode='w+' encoding='UTF-8'>
        ->
        .
        ->
        after test

        
        これでcsv fileを閉じる必要はなくなる。
        """
        print("before test")
        yield c
        print("after test")


def pytest_addoption(parser):
    parser.addoption('--os-name',default='linux',help='os name')