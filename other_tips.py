

#백슬래시를 사용하여 장문의 글을 줄일 수 있음음
long_string = "이 문자열은 매우 길어서 한 줄에 다 쓸 수 없을 때 " \
              "백슬래시를 사용하여 여러 줄에 걸쳐 쓸 수 있습니다."
print(long_string)


# == 랑 is를 주의. 값이 일치하는지의 개념은 ==임
print(1 == True) #True
print(1 is True) #False

#is는 주로 이하의 방법으로 사용
is_empty= None
if is_empty is None:
    print("None!")
