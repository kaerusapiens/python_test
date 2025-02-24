import salary
import unittest
from unittest.mock import MagicMock, patch
from unittest import mock

class TestSalary(unittest.TestCase):

    #-----------------MagicMock을 이용하는 방법
    def test_calculation_salary(self):
        s = salary.Salary(year=2022)
        s.bonus_api.bonus_price = MagicMock(return_value=1) #특정 개체안의 매서드 변경

        self.assertEqual(s.calculation_salary(),101)
        s.bonus_api.bonus_price.assert_called()
        s.bonus_api.bonus_price.assert_called_once()
        s.bonus_api.bonus_price.assert_called_once_with(year=2022)
    
    def test_calculation_no_salary(self):
        s = salary.Salary(year=2026)
        s.bonus_api.bonus_price = MagicMock(return_value=0)

        self.assertEqual(s.calculation_salary(),100)
        s.bonus_api.bonus_price.assert_not_called() #self.year <2025설정 검증

    #-----------------pathcer을 이용하는 방법
    @mock.patch('salary.ThirdPartyBonusRestApi.bonus_price',return_value=1)
    def test_calculation_no_salary_path(self,mock_bonus):
        """mock_bonus라는 가짜함수가 mock.patch에서 작성된 함수를 대체하여 실행됨됨"""
        s = salary.Salary(year=2022)
        self.assertEqual(s.calculation_salary(),101)
        mock_bonus.assert_called()

    #decorater가 아니라 with함수 안에서 실행하는 방법
    def test_calculation_no_salary_path_sample2(self):
        """mock_bonus라는 가짜함수가 mock.patch에서 작성된 함수를 대체하여 실행됨됨"""
        with mock.patch('salary.ThirdPartyBonusRestApi.bonus_price',return_value=1) as mock_bonus:
            s = salary.Salary(year=2022)
            self.assertEqual(s.calculation_salary(),101)
            mock_bonus.assert_called()
    



    #-----------------pathcer을 이용하는 방법
    def setUp(self): #Camelケース守る必要あり
        self.patcher = mock.patch('salary.ThirdPartyBonusRestApi.bonus_price')
        self.mock_bonus = self.patcher.start()

    def tearDown(self): #Camelケース守る必要あり
        self.patcher.stop()
    
    def test_calculation_no_salary_pather(self):
        """patcher를 사용하는 방법의 예시"""
        self.mock_bonus.return_value = 1

        s = salary.Salary(year=2022)
        self.assertEqual(s.calculation_salary(),101)
        self.mock_bonus.assert_called()

    #----------sideeffectで関数形で書き換えることも可能
    def test_calculation_no_salary_sideeffect(self):
        """sideeffect를 사용하는 방법의 예시 조건에 따른 테스트 가능""" #
        def f(year):
            if year < 2025:
                return 1
            else:
                return 0
        
        self.mock_bonus.side_effect = f

        s = salary.Salary(year=2022)
        self.assertEqual(s.calculation_salary(),101)
        self.mock_bonus.assert_called()

        s = salary.Salary(year=2026)
        self.assertEqual(s.calculation_salary(),100)
        self.mock_bonus.assert_called()

    def test_calculation_no_salary_sideeffect_exceptionhandling(self):
        """sideeffect를 사용하는 예외에러 처리 방법의 예시"""
        self.mock_bonus.side_effect = ConnectionRefusedError

        s = salary.Salary(year=2022)
        self.assertEqual(s.calculation_salary(),100)
        self.mock_bonus.assert_called()

    def test_calculation_no_salary_sideeffect_multiplecase(self):
        """sideeffect를 사용하여 여러패턴을 테스트"""
        self.mock_bonus.side_effect = [1,2,3,ValueError]

        # 1番目
        s = salary.Salary(year=2020)
        self.assertEqual(s.calculation_salary(),101)
        self.mock_bonus.assert_called()
        
        #2番目
        s = salary.Salary(year=2021)
        self.assertEqual(s.calculation_salary(),102)
        self.mock_bonus.assert_called()
        
        #3番目
        s = salary.Salary(year=2022)
        self.assertEqual(s.calculation_salary(),103)
        self.mock_bonus.assert_called()
        s = salary.Salary(year=200)

        #4番目
        with self.assertRaises(ValueError):
            s.calculation_salary()
        self.mock_bonus.assert_called()


    #-----------------spec사용
    @mock.patch('salary.ThirdPartyBonusRestApi',spec=True) #클래스를 Mock 객체로 바꾸는 것
    def test_calculation_no_salary_path(self,mock_rest):
        """mock_bonus라는 가짜함수가 mock.patch에서 작성된 함수를 대체하여 실행됨"""
        mock_rest = mock_rest.return_value #인수 mock_rest는 hirdPartyBonusRestApi의 모크화된 클래스. 그것을 인스턴스화 하는 방법이 이것.
        mock_rest.bonus_price.return_value = 1

        s = salary.Salary(year=2022)
        self.assertEqual(s.calculation_salary(),101)
        mock_rest.bonus_price.assert_called()