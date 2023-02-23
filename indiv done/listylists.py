i1 = input("input 1 ")
i2 = input("input 2 ")
i3 = input("input 3 ")
i4 = input("input 4 ")
i5 = input("input 5 ")

def listmaker(input1,input2,input3,input4,input5):
    mylist = [input1, input2, input3, input4, input5]
    return mylist

print(listmaker(i1, i2, i3, i4, i5))

l1 = ['Never', 'gonna', 'give', 'you', 'up']
l2 = ['a', 'b', 'c', 'd', 'e']
l3 = [1, 2, 3, 4, 5]
l4 = ['z', 'y', 'x', 'w', 'v']
l5 = [i1, i2, i3, i4, i5]

def listolists(list1,list2,list3,list4,list5):
    newlist = [list1, list2, list3, list4, list5]
    return newlist

print(listolists(l1, l2, l3, l4, l5))

k1 = input("first key ")
k2 = input("second key ")
k3 = input("third key ")
dictlistlist = []
x = 0

while x == 0:
    mod_1_item = input("matches first key ")
    dictlistlist.append(mod_1_item)
    mod_2_item = input("matches second key ")
    dictlistlist.append(mod_2_item)
    mod_3_item = input("matches third key ")
    dictlistlist.append(mod_3_item)
    yn = input("done? (Y/N) ")
    if yn.lower() == 'y':
        x = 1
    elif yn.lower() == 'n':
        print()

def dictlist(key1,key2,key3,list):
    dictionary = {
        key1:[],
        key2:[],
        key3:[]
    }
    count = 0
    for i in list:
        if count == 0:
            dictionary[key1].append(i)
            count+=1
        elif count == 1:
            dictionary[key2].append(i)
            count+=1
        else:
            dictionary[key3].append(i)
            count = 0
    return dictionary

print(dictlist(k1, k2, k3, dictlistlist))

finallist = listmaker(i1, i2, i3, i4, i5)

def indexlist(listA):
    result_string = ""
    for i, item in enumerate(listA):
        result_string += f"{item} is at Index {i} in the list. "
    return result_string

print(indexlist(finallist))