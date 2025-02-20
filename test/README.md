
# unittest における assert の種類


# `unittest` のアサーション一覧

Python の `unittest` で使用する主なアサーションをまとめました。

## **1. 値の比較**
| アサーション | 説明 | 使用例 |
|-------------|------|--------|
| `assertEqual(a, b)` | `a == b` であることを確認 | `assertEqual(2 + 2, 4)` |
| `assertNotEqual(a, b)` | `a != b` であることを確認 | `assertNotEqual(2 + 2, 5)` |
| `assertGreater(a, b)` | `a > b` であることを確認 | `assertGreater(5, 3)` |
| `assertGreaterEqual(a, b)` | `a >= b` であることを確認 | `assertGreaterEqual(5, 5)` |
| `assertLess(a, b)` | `a < b` であることを確認 | `assertLess(3, 5)` |
| `assertLessEqual(a, b)` | `a <= b` であることを確認 | `assertLessEqual(3, 3)` |

## **2. 真偽値のチェック**
| アサーション | 説明 | 使用例 |
|-------------|------|--------|
| `assertTrue(x)` | `bool(x) is True` であることを確認 | `assertTrue(1 < 2)` |
| `assertFalse(x)` | `bool(x) is False` であることを確認 | `assertFalse(2 < 1)` |

## **3. `None` のチェック**
| アサーション | 説明 | 使用例 |
|-------------|------|--------|
| `assertIsNone(x)` | `x is None` であることを確認 | `assertIsNone(None)` |
| `assertIsNotNone(x)` | `x is not None` であることを確認 | `assertIsNotNone(1)` |

## **4. 型のチェック**
| アサーション | 説明 | 使用例 |
|-------------|------|--------|
| `assertIsInstance(obj, cls)` | `obj` が `cls` のインスタンスであることを確認 | `assertIsInstance(5, int)` |
| `assertNotIsInstance(obj, cls)` | `obj` が `cls` のインスタンスでないことを確認 | `assertNotIsInstance(5, str)` |

## **5. 例外のチェック**
| アサーション | 説明 | 使用例 |
|-------------|------|--------|
| `assertRaises(exc, func, *args, **kwargs)` | `func(*args, **kwargs)` が `exc` を発生させることを確認 | `assertRaises(ZeroDivisionError, lambda: 1 / 0)` |
| `assertRaisesRegex(exc, regex, func, *args, **kwargs)` | 例外メッセージが `regex` に一致することを確認 | `assertRaisesRegex(ValueError, "invalid", int, "a")` |

## **6. コレクションのチェック**
| アサーション | 説明 | 使用例 |
|-------------|------|--------|
| `assertIn(a, b)` | `a in b` であることを確認 | `assertIn(3, [1, 2, 3])` |
| `assertNotIn(a, b)` | `a not in b` であることを確認 | `assertNotIn(4, [1, 2, 3])` |

## **7. オブジェクトの同一性チェック**
| アサーション | 説明 | 使用例 |
|-------------|------|--------|
| `assertIs(a, b)` | `a is b` であることを確認 | `assertIs(None, None)` |
| `assertIsNot(a, b)` | `a is not b` であることを確認 | `assertIsNot([], [])` |

## **8. 出力のチェック**
| アサーション | 説明 | 使用例 |
|-------------|------|--------|
| `assertLogs(logger, level)` | `logger` が `level` 以上のログを記録することを確認 | `assertLogs('my_logger', 'INFO')` |
| `assertWarns(warning, func, *args, **kwargs)` | `func(*args, **kwargs)` が `warning` を発生させることを確認 | `assertWarns(DeprecationWarning, my_func)` |

---

## **サンプルコード**
```python
import unittest

class TestExample(unittest.TestCase):
    def test_assert_methods(self):
        self.assertEqual(2 + 2, 4)
        self.assertNotEqual(2 + 2, 5)
        self.assertTrue(1 < 2)
        self.assertFalse(2 < 1)
        self.assertIsNone(None)
        self.assertIsNotNone(1)

if __name__ == "__main__":
    unittest.main()


#　pytest
```
import pytest
import test.calculation as calculation
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


```