# s1 = {10,20,30}
# print(s1)

# s2 = (10,20,30)
# print(s2)


# s3 = set(10,20,30)
# print(s3)             #  set expected at most 1 argument, got 3

# s3= set([10,20,30])
# print(s3)               # {10,20,30}


# s4 = set([10])
# print(s4)            #  {10}


# s5 = {10,20,30,40,50,60,70}
# print(next(s5))             #  'set' object is not an iterator


# s5 = [10,20,30,40,50,60,70]
# print(next(s5))     # 'list' object is not an iterator

# s5 = [10,20,30,40,50,60,70]
# a = iter(s5)
# print(next(a))      #  10
# print(next(a))             #  20
# print(next(a))             #  30
# print(next(a))              #  40

# s5 = [10,20,30,40,50,60,70]
# print(next(iter(s5)))             #  10
# print(next(iter(s5)))             #  10
# print(next(iter(s5)))             #  10
# print(next(iter(s5)))             #  10
# print(next(iter(s5)))             #  10

#  aisa q




# s5 = [10,20,30,40,50,60,70]
# a = iter(s5)
# print(next(a))             #  10
# print(next(a))             #  20
# print(next(a))             #  30
# print(next(a))             #  40
# print(next(a))             #   50 
# print(next(a))             #  60
# print(next(a))             #  70
# print(next(a))             #  StopIteration
# # qki jitne bhi value thi utni bar print ho gya jese loop chal gya h 
# # ab jyada bar iteration chalaenge to wo bolega ki ab stop kro










# if  else 


handsome = input('enter likking')

good_salary  = input('how is your salary')


if handsome == 'True' and good_salary == 'True':
    print ("you will marry with a super model")

elif handsome != 'True' and good_salary == 'True':
    print ("you will marry with a super model")

elif handsome == 'True' and good_salary != 'True':
    print ("you will marry with a super model")

else:
    print('bhagwan jo krega achha krega')










































































































