
######################
##### *args #######
######################
# *args  인수를 추가적으로 더 넣는 것이 가능
def say_something(word,*args):
    print('word = ', word)
    for arg in args:
        print(arg)


say_something("Hi!", "Hello,", "World!")

# tuple을 언패킹
t = ("Blue","Sky")
say_something("Hi!", *t)

######################
##### **kwargs #######
######################

# --------------------------------------------
def menu(entree="beef",drink="wine"):
    print(entree, drink)

menu(entree="beef",drink="coffee") #beef coffee

def menu_kwargs(**kwargs):
    print(kwargs)

menu_kwargs(entree="beef",drink="coffee") # {'entree': 'beef', 'drink': 'coffee'}

#-------------------

def handling_menu(**kwargs):
    for k , v in kwargs.items():
        print(k)

d = {
    "entree":"beef",
    "drink":"ice coffee",
    "dessert":"ice"
}
handling_menu(**d)



#-------------------------
# args는 튜플, kwrags는 딕셔너리로 취급됨.
def multiple_menu(food,*args,**kwargs):
    print(food)
    print()
    print(args)
    print()
    print(kwargs)

multiple_menu("banana","apple","orange",en="beef",dr="coffee")