# LOGIKA BOOLEAN
# NOT AND OR XOR

print("==========NOT==========")
x = False  # x adalah nilai boolean awal
z = not x  # z adalah hasil operasi NOT pada x
print("nilai z =", z)

# AND
print("==========AND==========")
x = False  # x adalah operand pertama
y = False  # y adalah operand kedua
nilai = x and y  # nilai adalah hasil AND antara x dan y
print(x, "and", y, "=", nilai)

x = False
y = True
nilai = x and y
print(x, "and", y, "=", nilai)

x = True
y = False
nilai = x and y
print(x, "and", y, "=", nilai)

x = True
y = True
nilai = x and y
print(x, "and", y, "=", nilai)

# OR
print("==========OR==========")
x = False  # x adalah operand pertama
y = False  # y adalah operand kedua
nilai = x or y  # nilai adalah hasil OR antara x dan y
print(x, "or", y, "=", nilai)
1    
x = False
y = True
nilai = x or y
print(x, "or", y, "=", nilai)

x = True
y = False
nilai = x or y
print(x, "or", y, "=", nilai)

x = True
y = True
nilai = x or y
print(x, "or", y, "=", nilai)

# XOR
print("==========XOR==========")
x = False  # x adalah operand pertama
y = False  # y adalah operand kedua
nilai = x ^ y  # nilai adalah hasil XOR antara x dan y
print(x, "xor", y, "=", nilai)

x = False
y = True
nilai = x ^ y
print(x, "xor", y, "=", nilai)

x = True
y = False
nilai = x ^ y
print(x, "xor", y, "=", nilai)

x = True
y = True
nilai = x ^ y
print(x, "xor", y, "=", nilai)