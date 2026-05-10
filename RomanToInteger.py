def romanToInt( s):
    """
    :type s: str
    :rtype: int
    """
    d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total=0
    for i in range(len(s)-1):
        if d[s[i]]<d[s[i+1]]:
            total-=d[s[i]]
        else:
            total+=d[s[i]]
    total+=d[s[-1]]
    return total

    #another method
    # total+=d[s[-1]]
    # for i in range(-2,-len(s)-1,-1):
    #     if d[s[i]]<d[s[i+1]]:
    #         total-=d[s[i]]
    #     else:
    #         total+=d[s[i]]
    
    # return total