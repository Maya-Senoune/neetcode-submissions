class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        arrays = [[pos, sp] for pos, sp in zip(position, speed)]

        arrays.sort(reverse = True)
        stack= []

        for pos, sp in arrays:
            t = (target - pos)/sp

            stack.append(t)
        
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
