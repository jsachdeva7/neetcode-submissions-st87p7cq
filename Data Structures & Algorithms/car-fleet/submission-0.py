class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(reverse=True)

        stack = []

        # create stack of fleets
        # each member of stack is the finishTime of each fleet
        for car in cars:
            (carPos, carSpeed) = car
            time = (target - carPos) / carSpeed
            if len(stack) == 0 or time > stack[-1]:
                stack.append(time)

        return len(stack)