class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool]
        
        WORKS BUT TOO SLOW
        
        # base
        if (not s and not p):
            return True
        elif not s and p[0] == '*':
            return self.isMatch(s, p[1:])
        elif not s or not p:
            return False
        
        # general
        if s[0] == p[0] or p[0] == '?':
            return self.isMatch(s[1:], p[1:])
        elif p[0] == "*":
            return self.isMatch(s[1:], p) or self.isMatch(s, p[1:])
        
        return False
        """
        
        def recursive_check(s_cur, p_cur, last_match, star_pos):
            
            # base
            if s_cur == len(s):
                while p_cur < len(p) and p[p_cur] == '*':
                    p_cur += 1
                if p_cur == len(p):
                    return True
                else: 
                    return False
        
            # general
            if p_cur < len(p) and (s[s_cur] == p[p_cur] or p[p_cur] == '?'):
                s_cur, p_cur =  s_cur+1, p_cur+1 
                return recursive_check(s_cur, p_cur, last_match, star_pos)
            elif p_cur < len(p) and p[p_cur] == '*':
                last_match, star_pos = s_cur, p_cur
                p_cur += 1
                return recursive_check(s_cur, p_cur, last_match, star_pos)
            else:
                if (star_pos!=-1):
                    p_cur = star_pos+1
                    last_match = last_match+1
                    s_cur = last_match
                    return recursive_check(s_cur, p_cur, last_match, star_pos)
                return False
        
        return recursive_check(0,0,0,-1)
        
        