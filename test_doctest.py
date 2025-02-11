class Cal(object):
    """test eample
    
    Args:
        object : the first parameter
    
    Retruns:
        None
    """
    def add_num_and_double(self, x,y):
        """Add and double

        >>> cal = Cal()
        >>> cal.add_num_and_double(1,1)
        4

        
        >>> cal.add_num_and_double("2","2")
        Traceback (most recent call last):
        ValueError: Both arguments must be integers.
        """
        if type(x) is not int or type(y) is not int:
            raise ValueError("Both arguments must be integers.") 
        result = x + y
        result *= 2
        return result
    

if __name__ == '__main__':
    print(Cal.__doc__)
    import doctest
    
    #testmod이용 파일 전체의 docstring을 테스트 .기본 Ture가 아니나, True를 설정하면 결과값을 볼 수 있음음
    doctest.testmod(verbose=True) 

    #별도의 테스트 파일을 만들어서 실행
    doctest.testfile("test_cal.txt", encoding="utf-8", verbose=True)

    # 특정 함수의 docstring 테스트 실행
    cal = Cal()
    doctest.run_docstring_examples(cal.add_num_and_double, globals(), verbose=True)