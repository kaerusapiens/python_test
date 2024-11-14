class Cal(object):
    def add_num_and_double(self, x,y):
        """Add and double

        >>> cal = Cal()
        >>> cal.add_num_and_double(1,1)
        4

        
        >>> cal.add_num_and_double("2","2")
        Traceback (most recent call last):
        ...
        ValueError
        """
        if type(x) is not int or type(y) is not int:
            raise ValueError
        result = x + y
        result *= 2
        return result
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()