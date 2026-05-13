def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l=[]
    k=0
    for i in nums:
        if i not in l:
            l.append(i)
            k+=1
    nums[:]=l
    return k