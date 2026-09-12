class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits==[9]:
            return [1,0]
        num=0
        for i in digits:
            num=(num*10)+i
        num+=1
        digits = [*map(int, str(num))]
        return digits
