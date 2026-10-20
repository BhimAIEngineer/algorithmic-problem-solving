class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        target = sorted(nums)
        
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
        
        total_sum = 0
        
        for k in divisors:
            valid = True
            for i in range(0, n, k):
                sub = nums[i:i+k]
                t_sub = target[i:i+k]
                
                if k == 1:
                    if sub != t_sub:
                        valid = False
                        break
                else:
                    drops = 0
                    drop_idx = -1
                    for j in range(k):
                        if sub[j] > sub[(j + 1) % k]:
                            drops += 1
                            drop_idx = j
                    
                    if drops > 1:
                        valid = False
                        break
                    elif drops == 1:
                        rotated = sub[drop_idx + 1:] + sub[:drop_idx + 1]
                        if rotated != t_sub:
                            valid = False
                            break
                    else:
                        if sub != t_sub:
                            valid = False
                            break
            
            if valid:
                total_sum += k
                
        return total_sum