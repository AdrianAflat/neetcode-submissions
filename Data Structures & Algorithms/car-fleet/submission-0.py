class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # position = [4,1,0,7], speed = [2,2,1,1]  target = 10
        #  3[4, 7]  never[1]  10[0]

        # fleets: (target - position) // speed

        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)

        fleets = 1
        prevTime = (target - pair[0][0]) / pair[0][1]
        for i in range(1, len(pair)):
            currCar = pair[i]
            currTime = (target - currCar[0]) / currCar[1]
            if currTime > prevTime:
                fleets += 1
                prevTime = currTime
            
        return fleets