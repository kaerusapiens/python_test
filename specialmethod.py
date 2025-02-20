class Word:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

    def __repr__(self):
        return f"Word('{self.text}')"

w = Word('hello')

print(w)    # hello
print([w])  # [Word('hello')]  ← __repr__ の出力
