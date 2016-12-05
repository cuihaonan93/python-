#coding:utf-8

print(2**38)

print("-"*20)
for i in range(10):
    #python的注释非常简单，前面加一个“#”
    # 前面空了4格
    print("This is block1")
    print(i)
print("This is block2")

for letter in 'Python':     # First Example
   print('Current Letter :', letter)

print("-"*20)
list_1 = ["a","b","c,d,","e"]
for i in list_1:
    print(i)
print("-"*20)
answer = 2
for i in range(37):
    answer = answer*2
print(answer)

for i in range(37):
    answer = 2
    answer = answer*2
print(answer)
print("-"*20)
#print(help(str))
str_1= "2"*38
answer_2 = 1
for i in range(len(str_1)):
    two = int(str_1[i])
    answer_2 = two*answer_2
print(answer_2)
