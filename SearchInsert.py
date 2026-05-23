def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    if target in nums:
        return nums.index(target)

    else:
        j=0
        for i in nums:
            if i < target:
                j+=1
        return j