#   append..............

# l1 = [10, 20, 30, 40, 50, 60, 70]    
# # print(l1)           #  [10, 20, 30, 40, 50, 60, 70]

# # print(l1.append(90))

# # # print(l1.append(110),l1.append(120))

# print(l1)






#  insert............................

# l2 = [10, 20, 30, 40, 50, 60, 70]
# print(l2.insert(1, 100))

# print(l2.insert(2, 130), l2.insert(5, 150))


# print(l2.insert(-3, 500))


# print(l2.insert(-2, 300), l2.insert(-5, 600))

# print(l2.insert(-10, 700))

# print(l2)




# ..........................................
# ...........................................


#  comparation in list....................

# l3 = [1, 2, 3]
# l4 = [3, 2, 1]
# l5 = [2, 1, 3]
# l6 = [1, 2, 3]

# print(l3==l4)                  #  False
# print(l4==l5)                  #  False
# print(l5==l6)                  #  False
# print(l3==l6)                         #  True

# # == hone k eliye list ko bilkul same hona chahoye 
# #  iska return True ya False me aata h 

# l3 = ['ram', 'sita', 'laxman']               
# l4 = ['sita', 'ram', 'laxman']
# l5 = ['ram', 'sita', 'laxman']
# l6 = ['ram', 'sita', 'laxma']

# print(l3 == l4)                  # False
# print(l3 == l5)                     # True
# print(l3 == l6)                  #  False              laxman me last me n ka anter h 




# ...................................................
# ...............................................


# cancatenation .............
# .................................................



# l1 = ['ram', 'sita']
# l2 = ['laxman', 'urmila']

# print(l1+l2)             # ['ram', 'sita', 'laxman', 'urmila']

# l3 = ['ram' 'sita']
# print(l1)                  # ramsita  qki ram aur sita ke bich me , nhi lagaya

# print(l2+l3)                 #  ['laxman', 'urmila', 'ramsita']

# print(l1+l2+l3)            # ['ram', 'sita', 'laxman', 'urmila', 'ramsita']


# l3 = [1,5, 9]
# l4 = [2, 3, 1]
# l5 = l3+l4
# print(l5)
# print(l3+l4)



# .....................................
# repetition operater
# ......................
# multiply

# l6 = [1, 2, 3]
# print(l6*3)                   #  [1, 2, 3, 1, 2, 3, 1, 2, 3]

# print([1, 2,]*4)             #  [1, 2, 1, 2, 1, 2, 1, 2]



# ...................................................
# list of list            or            list in list
# ..............................................


# l1 = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]
# print(l1)             #  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(l1[0])           #  [1, 2, 3]

# print(l1[2])     #   [7, 8, 9]

# print(l1[0][1])          # 2 ,  l1 ki 0 index ke index 1 ki value = 2






# ..............................................................
# attribute Error.......
# .............................................................



# attribute = list clas ke ander jo bhi variables aur funtions bne hote h unko attribute kehte h 

# attribute Error  =  jb bhi koi object apni class ke kisi member ko . lga ke access krne ki kosis krta h 
# aur agr us nam ka member us class me h hi nhi tb attribute error aaegi

# l1 = [1, 2, 3,]
# print(l1.f1())          #  AttributeError: 'list' object has no attribute 'f1'

# l1 = [1, 2, 3, 4, 5]

# print(l1.)


# a = "rana raj singh"

# print(a.sort())                 #  AttributeError: 'str' object has no attribute 'sort'
                                # qki sort function str ka h hi nhi ye to list ka function h  









# print(a.capitalize())                # Rana raj singh         pehle letter capital ho jaega

# print(a.find('j'))           # 7     j 7th index no 7 pe h 


# print(a.count('a'))                #  3

# print(a.count('r'))                #  2
# print(a.count('g'))                #  1

































