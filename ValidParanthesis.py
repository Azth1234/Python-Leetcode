def isValid( s):
    """
    :type s: str
    :rtype: bool
    """
    d = {
        ')': '(',
        ']': '[',
        '}': '{'
    }


    stack=[]
    for i in s:
        if i in "[{(":
            stack.append(i)
        else:
            if len(stack)==0:
                return False
            if stack.pop()!=d[i]:
                return False

    return len(stack)==0