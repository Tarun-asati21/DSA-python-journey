class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        from  collections import defaultdict
        from heapq import heappush, heappop, heapify
        
        # 3 hashmaps 
        self.food_rating_map={}
        self.food_cuisine_map={}
        self.cuisine_food_map=defaultdict(list)

        size=len(foods)
        for i in range(size) :
            self.food_rating_map[foods[i]]=ratings[i]
            self.food_cuisine_map[foods[i]]=cuisines[i]
            heappush(self.cuisine_food_map[cuisines[i]],(-ratings[i], foods[i]))
            # negative sign is inserted because heapq uses min heap, but we want max heap
        

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        # update
        self.food_rating_map[food]= newRating
        # insert
        cuisineName = self.food_cuisine_map[food]
        heappush(self.cuisine_food_map[cuisineName],(-newRating, food))

        
    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        # # way-1 -> efficient, since we are already using priority queue, but little tricky
        highest_rated = self.cuisine_food_map[cuisine][0]
        while highest_rated[0] != -self.food_rating_map[highest_rated[1]] :
            heappop(self.cuisine_food_map[cuisine])
            highest_rated = self.cuisine_food_map[cuisine][0] 
        return highest_rated[1]

        # # way-2 -> simple, but has little more complexity
        # heap=self.cuisine_food_map[cuisine]
        # while heap : # while heap != 0 :
        #     rating, food = heap[0]
        #     if self.food_rating_map[food] == - rating :
        #         return food
        #     heappop(heap)

        
# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
