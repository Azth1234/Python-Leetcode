def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """

    if x<0:
        return False
    rev=0
    num=x
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    return x==rev