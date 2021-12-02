

def sorteddi(lst1,lst2):
    if len(lst1)<5 |len(lst2):
        diff=[]
        for el1 in lst1:
            if el1 not in lst2 and el1 not in diff:
                diff.append(el1)
        for el2 in lst2:
            if el2 not in lst1 and el2 not in diff:
                diff.append(el2)
        return diff

    else:
        if len(lst1)>len(lst2):
            subnum=len(lst1)//5
        else:
            subnum=len(lst2)//5
            new_list1 = lst2[0:subnum]
            new_list2 = lst2[subnum:subnum*2]
            new_list3 = lst2[subnum*2:subnum*3]
            new_list4 = lst2[subnum*3:subnum*4]
            new_list5 = lst2[subnum*4:len(lst2)]
            for elemen in lst1:
                if len <subnum:
                    if elemen is not 

#Another approach could be to find which list is shorter and with it we compare each element 
#with the other list. But because we know that both of them are sorted each time that the algorithim sees that 
#one element is in both lists we will remove the previous one and if the list finds an element that is bigger to the current element we also delete the previous ones. Let's see an example.
#We have these to lists a=[2,8,9,24,45] and b=[1,5,8,22,23,24,40,41,45] the algorithim will detect 
#which list is shorter,in this case is a. And for each element of it will iterate through the
#other list. First we have 2 and when it goes through the other list it will find the value 5 and because 5 is bigger than 2 the previous number will be deleted that is the one
# After it will move to the number 8 and will go through 5 and 8 and once it reaches 8 it will stop and delete 8 and 5 from list b. As we can see the 8 is the third element of list b
#so the algorithim will go through each element of b and once it finds it will delete all the elements that were before it.




