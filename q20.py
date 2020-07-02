# 20. Write a Python class to find the three elements that sum to zero
# from a list of n real numbers. Input array : [-25, -10, -7, -3, 2, 4, 8, 10] Output : [[-10, 2, 8], [-7, -3, 10]]

input_array = [-25, -10, -7, -3, 2, 4, 8, 10]


class Triplets :

    def calc_sum(self,arr):
        input_length = len(arr)
        triplets_list=[]
        for i in range(0, input_length-2):
            for j in range(i+1, input_length - 1):
                for k in range(j+1, input_length):
                    if arr[i] + arr[j] + arr[k] == 0:
                        triplets_list.append([arr[i], arr[j], arr[k]])
        return triplets_list


triplet_sum = Triplets().calc_sum(input_array)
print(f'The triplets are : \n{triplet_sum}')

# OUTPUT
# The triplets are :
# [[-10, 2, 8], [-7, -3, 10]]
