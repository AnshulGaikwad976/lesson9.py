my_tuple = ()
print(my_tuple)

#tuple having integers
my_tuple = (1 ,2,3)
print(my_tuple)

#tuple with mixed datatypes
my_tuple = (20 , "shaurya" , "shivik" ,  30)

#nested tuple
my_tuple = (20 , [20 , 30 , 40 ] , [1 , 2 , 3])
print(my_tuple)

#accessing tuple elements using indexing
my_tuple = ('p','q','r','s')
print(my_tuple[0])
print(my_tuple[3])

#nested tuple
n_tuple = ("mouse" , [0 ,4 ,6 ,8], [1,2,3])
print(n_tuple[1][2])

#slicing
print("sliced :", my_tuple[1:4])

#iterating throug tuple
for letter in (my_tuple):
  print("hello" , letter)
