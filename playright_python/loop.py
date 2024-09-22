## here we have to create a function 
def looping(input):
    list = []
    for i in input:
        list.append(i.text())
    print('flist',list)
    print()
    return list