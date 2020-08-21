"""My Module """


# Question 1 
def array_challenge(nums):
    """This is my function"""
    for j in range(len(nums) - 2):
        if nums[j] == 1 and nums[j + 1] == 2 and nums[j + 2] == 3:
            return True
    return False


the_list1 = [1, 1, 2, 3, 1]
print(array_challenge(the_list1))


# Question 2
def string_bits(my_str):
    """This is my function"""
    for i in range(0, len(my_str), 2):
        print(my_str[i])  # Using a return statement will
        # only return 1 index


string_bits("Heeololeo")


# Question 3
def end_other(a):
    """This is a function"""
    for elements in range(len(a), -1):
        return a[elements]


end_other('Hiabc')
