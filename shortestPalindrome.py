def shortestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        from collections import deque
        orig = list(s)
        rev = orig[::-1]
        val = []
        out = deque([])
        out.extend(s)
        
        if orig == rev:
            return orig
        
        for i in range(len(orig)):
            out.appendleft(rev.pop())
            one = str(''.join(out))
            newr = one[::-1]
            if one == newr:
                return one
      
        return ""

print shortestPalindrome('abcd')