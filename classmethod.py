class Example(object):
    value = 0
    def __init__(self):
        self.value = 10

    def sample(self):
        print(self.value)

    @staticmethod
    def static_method():
        # Cannot access `cls` or `self`
        print("Static Method")

    @classmethod
    def class_method(cls):
        # Can access and modify `cls.value`
        cls.value += 1
        print(f"Class Value: {cls.value}")

a = Example()
a.sample()
b = Example
b.class_method() #b.sample()は objectが生成されていないため呼び出すことができない