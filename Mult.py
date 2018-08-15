#the alogorithm will multiply every digit together
nums1 = [int(x) for x in list(input())]
nums2 = [int(x) for x in list(input())]

def multiply(list1, list2):
    results=[]
    carry=0
    for x in range(len(list2)-1,-1,-1):
        quickTally=0
        for y in range(len(list1)-1,-1,-1):
            quickTally+=((list2[x]*list1[y]+carry)%10)*10**(len(list1)-y-1)
            carry=(list2[x]*list1[y]+carry)//10
            #print(list2[x],list1[y], carry, quickTally)
        quickTally+=carry*10**len(list2)
        #print("   ",quickTally)
        carry=0
        results.append(quickTally*10**(len(list2)-1-x))
        quickTally=0
    #print(results)
    answer=0
    for item in results:
        answer+=item
    return answer
print(multiply(nums1, nums2))
