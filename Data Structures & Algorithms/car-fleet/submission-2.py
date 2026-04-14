class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # build cars array, each should be (position, car)
        cars = []
        for i in range(len(position)):
            car = (position[i], speed[i])
            cars.append(car)
        
        # Sort cars in descending order of position so we can be certain
        # about the speed of the one ahead of it
        cars.sort(reverse=True)

        # Stack representing fleet finishing time
        fleetTimes = []
        for car in cars:
            (carPos, carSpeed) = car
            time = (target - carPos) / carSpeed

            # If the time is less than the current top of stack, joins that fleet
            # If the time is greater than current top of stack, new fleet
            if len(fleetTimes) == 0 or fleetTimes[-1] < time:
                fleetTimes.append(time)
        
        return len(fleetTimes)
            

        