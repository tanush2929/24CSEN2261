#Function to add an number
def add_num(lst,num):
    lst.append(num)
    return lst

#Function to remove an number
def remove_num(lst,num):
    if num in lst:
        lst.remove(num)
    else:
        print("Element",num,"is not found in the list.")
    return lst
    
#Function to find maximun number
def max_num(lst):
    if len(lst)>0:
        return max(lst)
    else:
        return None

#Function to find minimum number
def min_num(lst):
    if len(lst)>0:
        return min(lst)
    else:
        return None

#Function to Calculate the sum
def sum_list(lst):
    return sum(lst)

#Function to sort the list in asceding order
def sort_list(lst):
    return sorted(lst)

#Function to Reverse the list
def reverse_list(lst):
    return lst[::-1]

#Function to count the occurrneces of an number
def count(lst,num):
    return lst.count(num)

#Function to find the index of an number
def index(lst,num):
    if num in lst:
        return lst.index(num)
    else:
        return -1



#Main Program
lst=[5,2,9,1,5,6,3,9,5,7]
print("Original List:",lst)
a=int(input("Enter number to be added:"))
lst=add_num(lst,a)
print("After Adding:",lst)

b=int(input("Enter number to be removed:"))
lst=remove_num(lst,b)
print("After Removing:",lst)

print("Maximum Number:",max_num(lst))

print("Minimum Number:",min_num(lst))

print("Sum of Numbers:",sum_list(lst))

print("Sorted List in Ascending order:",sort_list(lst))

print("Reversed List:", reverse_list(lst))

c=int(input("Enter number to be counted:"))
print("Count of",c,':',count(lst,c))

d=int(input("Enter number index you want to know:"))
print("Index of ",d,':',index(lst,d))
