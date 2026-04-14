class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        # stack for temperatures, pop when finding a temperature higher than it
        # until no more that are colder than the current day
        for day in range(len(temperatures)):
            temperature = temperatures[day]
            dayTemp = (day, temperature)

            while len(stack) > 0 and temperature > stack[-1][1]:
                (dayPopped, tempPopped) = stack.pop()
                result[dayPopped] = day - dayPopped

            stack.append(dayTemp)

        return result