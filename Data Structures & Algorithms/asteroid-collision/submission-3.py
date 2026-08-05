class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        negatives = []
        for a in asteroids:
            if a > 0:
                s.append(a)
            if a < 0:
                destroyed = False
                while s:
                    val = s.pop()
                    if val > abs(a):
                        s.append(val)
                        break
                    elif val == abs(a):
                        destroyed = True
                        break
                    else:
                        continue
                if not s and destroyed == False:
                    negatives.append(a)
                
        
        return negatives + s

                
            
        