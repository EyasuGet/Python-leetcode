class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_num = max(candies)
        answer = []
        for i in candies:
            if i + extraCandies >= max_num:
                answer.append(True)
            else:
                answer.append(False)
        return answer