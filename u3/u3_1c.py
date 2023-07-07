#quicksort #########################

from random import randint
from math import floor
import time

def my_partition(array):
    global counter                            # counts comparisons
    i = -1
    n = len(array)-1
    pivot = array[n]
    for j in range(0, n):
        counter +=1                           # counts comparisons
        if array[j] <= pivot:
            i = i+1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[n] = array[n], array[i+1]
    return (i+1)

def my_quicksort(array):
    if len(array) <= 1:
        return array
    pivot = my_partition(array)
    #left = [array[i] for i in range(0,pivot-1)]
    #right = [array[i] for i in range(pivot+1,len(array))]
    left = array[:pivot]
    right = array[pivot+1:]
    return my_quicksort(left) + [array[pivot]] + my_quicksort(right) 

#quicksort end#############################


#creates a random list
def create_random_list (n,a,b):
    array = []
    for i in range(0,n):
        array += [randint(a,b)]
    return array
 
#for partition. 
#wont count the comparisons here
def find_position (A,x):
    for i in range(0,len(A)):
        if A[i]==x:
            return i
        
#partition for select
def my_partition_select(array,x):
    global counter                            # counts comparisons
    i = -1
    n = len(array)-1
    k = find_position(array,x)
    pivot = array[k]
    array[k], array[n] = array[n], array[k]
    for j in range(0, n):
        counter +=1                           # counts comparisons
        if array[j] <= pivot:
            i = i+1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[n] = array[n], array[i+1]
    ##########print("partition:",array,x)
    return (i+1)


#takes n log n time because of quicksort
def find_median(A):
    n = len(A)
    if n == 1:
        return A[0]
    A = my_quicksort(A)
    median = int(round(n/2.0))-1
    #print("find_median:",A,median)
    return A[median]


#just like in lecture with 2 exepctions.
def good_splitter (A,groups):
    #new terminate condition
    if(len(A) <= groups):       
        return find_median(A)

    #1.split A into groups of size of groups
    temp_list = []
    for i in range (0,len(A),groups):
        temp_list = temp_list + [A[i:i+groups]] 
    A = temp_list

    #2. find the median of each group 
    # will take n/k loops and (k log k) time for each loop
    M = []
    for i in A:
        median = find_median(i)
        M = M + [median]

    #3. find median of medians
    #print("select(",M, (int(floor(len(M)+1)/2.0) ,")"))
    m = select (M, int(floor(len(M)+1)/2.0),groups )

    return m

#just like in lecture
def select (A,k,groups): 
    global counter

    x = good_splitter(A,groups)
    size_of_L = my_partition_select(A,x)

    counter +=1
    if size_of_L == k-1:
        return x

    counter +=1
    if size_of_L >= k:
        L = A[:size_of_L]
        #print("left",size_of_L,k, "L:", L)
        return select(L,k,groups)

    counter +=1
    if size_of_L < k:
        R = A[size_of_L+1:]
        #print("right",size_of_L,k, "R:", R)
        return select(R,k-size_of_L-1,groups)

#main
counter = 0
length = 1000
tests = 100
print('Random array length=', length, '; number of tests=', tests)
for group_size in [3,5,7,9,11]:
    counter = 0
    begin = time.time()                 #measures time
    for i in range (0,tests):
        array = create_random_list(length,0,100)
        select(array,length/2,group_size)
        #print(find_median(array), k, find_median(array)==k )
    end = time.time()                   #measures time
    print('group_size:' ,group_size , ', Average_Comparisons:' , counter/tests , ', Exec_Time:' , end-begin)