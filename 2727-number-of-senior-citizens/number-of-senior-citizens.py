class Solution(object):
    def countSeniors(self, details):
        count = 0
        for age in details:
            if int(age[11:13]) > 60:
                count += 1

        return count