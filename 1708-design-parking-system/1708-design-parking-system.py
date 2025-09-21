class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.big_slots=big
        self.medium_slots=medium
        self.small_slots=small
        self.hashmap={1:self.big_slots, 2:self.medium_slots, 3:self.small_slots}

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if self.hashmap[carType]==0 :
            return False
        else :
            self.hashmap[carType]= self.hashmap[carType] - 1
            return True
        
        



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)