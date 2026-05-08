def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    shortest=min(strs, key=len)
    for i in range(len(strs)+1):
        for s in strs:
            if not s.startswith(shortest):
                shortest=shortest[0:len(shortest)-1]
                break
    
    return shortest