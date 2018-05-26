#Object ID


# 변경 불가능한 타입의 객체는 내용이 같으면
# 같은 ID를 갖는다
i1 = 10
i2 = 10

print(hex(id(i1)), hex(id(i2)))

i1 = 300
i2 = 300
print(hex(id(i1)), hex(id(i2)))


# 변경 가능한 타입의 객체는 내용이 같아도
# 다른 ID를 갖는다
l1 = [1,2,3]
l2 = [1,2,3]

print(hex(id(l1)), hex(id(l2)))

s1 = 'hello'
s2 = 'hello'

print(hex(id(s1)), hex(id(s2)))

print(i1 is i2)
print(s1 is s2)
print(l1 is l2)