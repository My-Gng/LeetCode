class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        result = []
        for hour in range(12):
            for minute in range(60):
                hr = bin(hour).count('1')
                min = bin(minute).count('1')

                total = hr + min

                if total == turnedOn:
                    time = str(hour) + ":" + str(minute).zfill(2)
                    result.append(time)

        return result

x = Solution()
y=x.readBinaryWatch(1)
print(y)


