def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    k=0
    num=0
    for i in digits[::-1]:
        num=num+i*(10**k)
        k+=1
    num+=1
    s=str(num)
    l=[int(i) for i in s]

    digits[:]=l

    return digits