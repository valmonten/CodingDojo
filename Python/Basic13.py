# NUMBER 1
# def print_to_255():
#     for number in range(1,256):
#         print number
# print_to_255()

# NUMBER 2
# def print_int_sum():
#     tot=0
#     for number in range (1,256):
#         tot+= number
#         print number
#         print tot
# print_int_sum()

# NUMBER 3
# def print_max(array):
#     supermax = array[0]
#     for number in array:
#         if number>supermax:
#             supermax=number
#     print supermax
# print_max([9, 10.4, 9, 875, 291.08, 59,0])

# NUMBER 4
# def oddarray():
#     array = []
#     for number in range (1,256,2):
#         array.append(number)
#     print array
# oddarray()

# NUMBER 5
# def greater_than_y(thingy,y):
#     count =0
#     for things in thingy:
#         if things > y: 
#             count+=1
#     print count
# greater_than_y([6,2,4,8,9,76,3],7)

# NUMBER 6
# def max_min_avg(arr):
#     smax=arr[0]
#     smin=arr[0]
#     ssum=0
#     for number in arr:
#         if smax< number:
#             smax=number
#         if smin> number:
#             smin=number
#         ssum+=number
#     print "Average is "
#     print ssum/len(arr)
#     print "Max is "
#     print smax
#     print "Min is "
#     print smin
# max_min_avg([1,2,3,4,5,6,7,19,0])

# NUMBER 7 
# def swap_neg_zero(arr):
#     for num in range(len(arr)):
#         if arr[num]<0:
#             arr[num] = 0
#     print arr
# swap_neg_zero([0,1,-1,8,-4])

# NUMBER 8
# def print_odds():
#     for number in range (1,256,2):
#         print number
# print_odds()

# NUMBER 9
# def print_list(list):
#     for number in list:
#         print number
# print_list([1,2,3,4,5,9])

# NUMBER 10
# def get_avg(numbers):
#     ssum=0
#     for number in numbers:
#         ssum+=number
#     print ssum/len(numbers)
# get_avg([1,7])

# NUMBER 11
# roots=[4,6,9]
# def be_square(li):

#     for num in range(len(li)):
#         li[num] = li[num]*li[num]
#     print li
# be_square(roots)

# NUMBER 12
# def swap_neg_dojo(arr):
#     for num in range(len(arr)):
#         if arr[num]<0:
#             arr[num] = 'Dojo'
#     print arr

# swap_neg_dojo([0,1,-1,8,-4])

# NUMBER 13
# def shift_left(arr):
#     for num in range(len(arr)-1):
#         arr[num]=arr[num+1]
#     arr[len(arr)-1]= 0
#     print arr
# shift_left([1,2,3,4,5,6])

