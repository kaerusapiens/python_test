# parent class
class Person(object):

    # __init__ (コンストラクター作成)
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)
        
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
    
# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary=5000,post=None):
        self.salary = salary
        self._post =post
        #ーーーーーー
        #親クラスのコンストラクタを呼び出す方法
        #①Person.__init__(self, name, idnumber)
        #②⇓
        super().__init__(name, idnumber)

    @property
    def post(self):
        return self._post
        
    #override : 親クラスのメソッドを上書きする
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))


a = Employee('Rahul', 886012, 200000,"intern") #postはNoneではなく、intern
#a.post=500 #これはsetterを設定してなかったので、実行されない
a.display()
a.details()