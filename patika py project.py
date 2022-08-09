import ast


# Flatten Function
def flatten(flist):
    for i in flist:
        if isinstance(i, list):
            flatten(i)
        else:
            alist.append(i)


# Reverse Function
def Reverse(list1):
    list1.reverse()
    list2 = list1.copy()
    for i in range(len(list1)):
        if isinstance(list1[i], list):
            Reverse(list1[i])
    return list2

# alist is the list after processing
alist = []
choice = int(input("Choose the process,please!(1: Flatten Function - 2: Reverse Function)\n"))
if choice == 1:
    # blist is the list before processing
    blist = ast.literal_eval(input("Enter the list like: ['a','b',['c','d']]\n"))
    flatten(blist)
    print(alist)
elif choice == 2:
    blist = ast.literal_eval(input("Enter the list like: [3,4,[5,'d']]\n"))
    alist = Reverse(blist)
    print(alist)