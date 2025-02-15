animal = "cat"

def local_func():
    animal = 'dog'
    print('local func animal vairalbe :',animal ) # dog
    print('関数内で宣言されている変数: ', locals())


local_func()
print('gloabl animal variable : ' , animal) # cat
print('gloabl varialbe : ' ,globals())
