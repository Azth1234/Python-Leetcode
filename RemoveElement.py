def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """

    l=[]
    k=0
    for i in nums:
        if i==val:
            continue
        l.append(i)
        k+=1