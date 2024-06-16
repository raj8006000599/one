
# python

# ...............................................
# built in function
# len()
# min()
# max()
# ............................................

# a = 'ram', 'sita', 'shyam','radha' 

# print(len(a))

# print(min(a))

# print(max(a))





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







# ................................................
# str functions
# ...........................................



# a = "raj is a good boy"
# # print(a.index("good "))

# print(a.find("i"))
# print(a.find("good"))
# print(a.find("a"))

# print(a.count("  "))

# print(a.endswith("boy"))
# a = "123"                                 #  True
# a = "13 raj is a good boy"               #  False   aisa  kyo
# print(a.isdigit())     # Truej

# print(a.islower())                          #  True    ek bhi letter upper hota to False aata

# print(a.isupper())                          #  false       ek bhi letter lower hota to False aata

# a = "Rana Raj Singh"

# print(a.lower())                          #  rana raj singh            lower me 1 copy bn jaegi

# but 
# print(a)                            #   Rana Raj Singh              but   og same rhega

# print(a.upper())                         #  RANA RAJ SINGH                upper me 1 copy bn jaegi

#   but
# print(a)                                #  Rana Raj Singh               but og same rhega



# print(help(str.replace))         isse hm kisi bhi function kause check kr skte h 



# a = "rana raj singh is a good boy"

# print(a.replace("j", "M"))

# print(a.replace("raj", "ram"))

# print(a)

# print(a.replace("a", "e"))

# print(a.replace("a", "e", 1))

# print(a.replace("a", "e", 2))


# a, b = 10, 20

# c = "sum of {} and {} is {}"

# print(c.format(a, b, a+b))


# c = "sum of {2} and {0} is {1}"

# print(c.format(a, b, a+b))



# a = "rana raj singh is a good boy"
# print(a.split(" "))            #  ['rana', 'raj', 'singh', 'is', 'a', 'good', 'boy']

# print(a.split(","))           # ['rana raj singh is a good boy']

# print(a.split("-"))                  #  ['rana raj singh is a good boy']

# print(a.split("*"))                   #  ['rana raj singh is a good boy']

# print(a.split("_"))                     #  ['rana raj singh is a good boy']

# print(a.split("."))                      #  ['rana raj singh is a good boy']

# print(a.split("="))                       #   ['rana raj singh is a good boy']



# a = "10,20,30,40,50,60,70"

# print(a.split(" "))                 #  ['10,20,30,40,50,60,70']

# print(a.split(","))                #   ['10', '20', '30', '40', '50', '60', '70']


# a = "10,20,30,40,50,60,70"

# print(a.split(","))                 #  ['10,20,30,40,50,60,70']
# print(a.split(" "))



 
# l =  ['10', '20', '30', '40', '50', '60', '70']

# print(",".join(l))                       #  10,20,30,40,50,60,70


# l2 =  ['rana', 'raj', 'singh', 'is', 'a', 'good', 'boy']

# print(" ".join(l2))             #  rana raj singh is a good boy

# print("-".join(l2))                 #  rana-raj-singh-is-a-good-boy

# print(",".join(l2))              # rana,raj,singh,is,a,good,boy

# print(", ".join(l2))               # rana, raj, singh, is, a, good, boy


# l2 =  ['rana','raj','singh','is','a','good','boy']
# print(",".join(l2))                    #  rana,raj,singh,is,a,good,boy



# print(a,b,c)
# print(" ".join(a,b,c))        # error    str.join() takes exactly one argument (3 given)

# d = a,b,c
# print(" ".join(d))                  #  rana raj singh

# e = a+b+c
# print(" ".join(e))           #  r a n a r a j s i n g h            space ke sath sbko ek sath jod dega





#  len

# a = "rana raj singh is a good boy"
# print(len(a))

b = "apple"
print(hash(b))




