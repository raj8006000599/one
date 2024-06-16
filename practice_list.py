

# l1 = [20, "ram", "sita", 5.2, True]
# print(l1)                            #  20, "ram", "sita", 5.2, True



# access by index ..........

# print(l1[0])               #  20

# print(l1[0])

# print(l1[1])                 #  ram

# print(l1[1][0])                 # r

# print(l1[1][1])                    #  a

# print(l1[1][2])                     # m

# print(l1[2][0])             #  s           

# print(l1[2][1])             # i 

# print(l1[2][2])             #  t

# print(l1[2][3])             #  a




# changes in list...............

# l2 = [20, 30, 10, 40, 50]
# print(l2)

# l2[0] = 60
# print(l2)

# l2[1],l2[2] = 70, 80
# print(l2)                      #   [20, 70, 80, 40, 50]

# print(l2[2],[0])                #   10 [0]

# print(l2[0],[1])                     #  20 [1]

# print(l2[0],l2[1])                    #  20 30

# print(l2[2],l2[1])                    # 10 30



#  list slicing.............

# l = [ "ram", "sita", "laxman","urmila"]

# print(l[0:1])      #  ram

# print(l[0:3])     # ram , sita , laxman

# print(l[1:4])                 # ['sita', 'laxman', 'urmila']

# print(l[0],l[2])          # ram laxman

# print(l[-2])                 #  laxman

# print(l[-4], l[-1])           # ram  urmila

# print(l[-4:-2])                  # ram sita




# packing   unpacking................

# packing........

# a, b, c, d = 1, 2, 3, 4

# l3 = [a, b, c, d]

# print(l3)                       # [1, 2,, 3, 4]


# unpacking.......

# l4 = [10, 20, 30, 40]

# a, b, c, d = l4

# print(a)
# print(b)
# print(c)
# print(d)


# ..............................................................................
#  list()   function
# ..............................................................................


# l4 = list()           # ye empty list h 
# l4 = []             # line 101 aur line 102 ka ek hi mtlb h  {l4 = list()} = {l4 = []} 

# ye bhi sahi h, ye list() function h  
# jisme bhi () hota h wo function hota h 
# pr l4 = list() function me hm bs ek value hi rakh skte h 
# wo value bhi iterable honi chahiye

# l4 = list()

# l4 = list(100)
# print(l4)                       # error ,  'int' object is not iterable

# l5 = list(3.5)
# print(l5)                   #  error      'float' object is not iterable



# l4 = list("rana")
# print(l4)                        #   ['r', 'a', 'n', 'a']


# l4 = list(range(5))
# print(l4)                       #  [0, 1, 2, 3, 4]

#  range ka mtlb hota h {first value : last value}
# agr range me kewal ek value hi di gyi h to use lst value mana jata h 
#  aur use last value mankr usse pehle ke value ko return kiya jata h 
#  last value - 1    ko return kiya jata h 



# l4 = list('ram', 'laxman')
# print(l4)                     # error    list() expected at most 1 argument, got 2

#   error h qki list funtion me kewal ek hi arguement pass kiya jata h aur yanha pr 2 aurguement h





