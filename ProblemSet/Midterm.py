# Problem 4
def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    result = 0
    if k==1:
        return True
    for i in range(k):
        result += i
        if result == k:
            return True
    return False


# Problem 5
def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    result = ''
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for char in s:
        if char not in vowels:
            result += char
    print(result)



# Problem 6
def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """

    temp = {}
    for num in L:
        temp[num]=0  # initialize the dict to have all 0s

    # update the dict to be - {num: number of occurrence}
    for num in L:
        for key in temp.keys():
            if num==key:
                temp[key]+=1

    largest = 0
    for key,value in temp.items():
        if value%2!=0 and key > largest:
            largest = key
    if largest==0:
        return None
    else:
        return largest


# Problem 7
def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''

    # Take care of the empty dict - Exception
    if len(d)==0:
        return {}


    key_list = []
    for value in d.values():
        key_list.append(value)
    key_set = set(key_list)


    inverted = {}
    value_list=[]
    temp_key=key_list[0]

    for key,value in d.items():
        for key_set_value in key_set:
            if value == key_set_value:
                if key_set_value!=temp_key:
                    value_list=[]
                value_list.append(key)
                inverted[key_set_value]=sorted(value_list)
                temp_key = key_set_value
    return inverted


# print(dict_invert({1:10,2:20,3:30}))
# print(dict_invert({1:10, 2:20, 3:30, 4:30}))
# print(dict_invert({}))


# Problem 8
def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """

    k = len(L)

    def poly(x):
        result = 0
        for i in range(0,k):
            result += L[i]*(x**(k-1-i))
        return result
    return poly

#print(general_poly([1, 2, 3, 4])(10))

# Problem 9
def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    '''

    if len(L1)==len(L2)==0:
        return (None,None,None)

    set_L1 = set(L1)
    set_L2 = set(L2)
    dict_L1 = {}
    dict_L2 = {}

    for item in L1:
        for set_item in set_L1:
            if set_item not in dict_L1.keys():
                dict_L1[set_item]=0
            if item == set_item:
                dict_L1[set_item]+=1


    for item in L2:
        for set_item in set_L2:
            if set_item not in dict_L2.keys():
                dict_L2[set_item]=0
            if item == set_item:
                dict_L2[set_item]+=1


    is_permutation = (dict_L1==dict_L2)

    if is_permutation==False:
        return False
    else:
        largest_times = max(dict_L1.values())
        for key in dict_L1:
            if dict_L1[key]==largest_times:
                element = key

        return (element,largest_times,type(element))





#
# print(is_list_permutation(L1=[1, 'b', 1, 'c', 'c', 1], L2=['c', 1, 'b', 1, 1, 'c']))
#
# print(is_list_permutation([],[]))