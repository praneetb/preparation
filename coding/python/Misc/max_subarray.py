#
# find the sum of contiguous sub-array within a one-dimensional array
# of numbers which has the largest sum.
#

def max_sum_sub_array(nums_list):
    size = len(nums_list)
    max_so_far = curr_max = nums_list[0]
    for index in range(1, size):
        curr_max = max(nums_list[index], nums_list[index] + curr_max)
        max_so_far = max(max_so_far, curr_max)

    return max_so_far


a = [-2, -3, 4, -1, -2, 1, 5, -3]
print"Maximum contiguous sum is" , max_sum_sub_array(a)

a = [-2, -3, 2, -1, -2, 1, 5, -3]
print"Maximum contiguous sum is" , max_sum_sub_array(a)

a = [-2, -3, -4, -1, 2, -1, -5, -3]
print"Maximum contiguous sum is" , max_sum_sub_array(a)


