def number_swap(list_of_nums, index1, index2):
    list_of_nums[index1] = list_of_nums[index2]

mylist = [1,2,3,4,5]
number_swap(mylist, 1, 2)
print(mylist)