class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        if mass < min(asteroids):
            return False
        if mass + sum(asteroids) < max(asteroids) :
            return False
            
        asteroids = sorted(asteroids)
        arr1 = []
        arr2 = []
        for i in range(len(asteroids)) :
            if asteroids[i] > mass :
                arr2.append(asteroids[i])
            else :
                arr1.append(asteroids[i])
        
        start = mass+sum(arr1)
        for i in range(len(arr2)) :
            if arr2[i] > start :
                return False 
            start += arr2[i]
        return True