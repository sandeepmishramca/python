#List functions example
#find last index of given string
def find_last_index(list, element):
    if list.count(element)==0:
        return None
    else:
        return len(list)-1-list[::-1].index(element)

#find element is present in list
def is_present(list, element):
    if list.count(element)==0:
        return False
    else:
        return True

def count_and_print_numbers(list, element):
    if list.count(element)==0:
        return False
    else:
        return list.count(element)

def first_and_last_elements_of_list(list):
    l=[]
    l.append(list[0])
    l.append(list[len(list)-1])
    return l

#remove duplicates from list
def remove_duplicates(list):
    #return set(list)
    duplicatlist=[]
    for element in list:
        if element not in duplicatlist:
            duplicatlist.append(element)
    return duplicatlist





l= ['a','b','c','d','a','c','d','c']
#print find_last_index(l,'d')
#print is_present(l,'m')
#print count_and_print_numbers(l,'c')
#print first_and_last_elements_of_list(l)
#print remove_duplicates(l)
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print [x for x in a if x%2==0]




