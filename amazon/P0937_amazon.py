class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        lets = []
        dits = []
        for log in logs:
            t = log.split()
            if ''.join(t[1:]).isdigit():
                dits.append(log)
            else:
                lets.append((t[1:],t[0],log))        
        return [log for a,b,log in sorted(lets)] + dits