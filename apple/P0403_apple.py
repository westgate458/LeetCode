class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        steps = defaultdict(set)
        stone_set = set(stones)
        steps[0] = set([0])
        
        for stone in stones:
            for step in steps[stone]:
                for next_step in [step-1,step,step+1]:
                    if next_step > 0:
                        next_stone = stone + next_step
                        if next_stone == stones[-1]:
                            return True
                        elif next_stone in stone_set:
                            steps[next_stone].add(next_step)
        return False