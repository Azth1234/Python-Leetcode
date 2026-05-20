def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    l=s.split()
    return len(l[-1])