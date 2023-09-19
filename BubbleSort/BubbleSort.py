# this is the simple explanation of BubbleSort Algorithms 
 
# how does it work is explained below
 
# let x = [ 5,4,3,2,1]

# we have two kind of loops one inside one which execute almost n square times
# where as one that is outside will execute only n times 

# things that happened in the actual code 
# result after the execution of outside loop
# [4,3,2,1,5]
# [3,2,1,4,5]
# [2,1,3,4,5]
# [1,2,3,4,5]

my_list = [9,6,4,1,3,6,8];

#doing iteration to n - 1 times 
# if we correct the postion of 4 items amoung the five then the fifth one will also be corrected
for i in range(len(my_list)-1):
    # the largest is always kept at the last so no need to do extra one comparision
    for j in range(len(my_list) - i-1):
        if ( my_list[j] > my_list[j + 1]):
            # swapping the both number
            my_list[j] , my_list[j+1] = my_list[j+1] , my_list[j];
print(my_list) 