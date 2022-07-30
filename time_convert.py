class Solution:
    def get_diff(self, current, correct):
        hour_diff = int(correct.split(":")[0]) - int(current.split(":")[0])
        minute_diff = int(correct.split(":")[1]) - int(current.split(":")[1])
        return hour_diff * 60 + minute_diff

    def convertTime(self, current: str, correct: str) -> int:
        time_diff = self.get_diff(current, correct)
        #print(time_diff)
        options = [60, 15, 5, 1]
        count = 0
        for option in options:
            rem = time_diff % option
            count += int(time_diff / option)
            time_diff = rem
            #print(f"{option}: Count {count}, rem: {rem}")
            if rem == 0:
                return count
    
print(Solution().convertTime("02:30", "04:35"))