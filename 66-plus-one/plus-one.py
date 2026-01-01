class Solution(object):
    def plusOne(self, digits):
        total = 0
        for i in range(len(digits)):
            total += digits[i] * pow(10,len(digits)-i-1)
        total += 1
        digit_list = []
        for x in str(total):
            digit_list.append(int(x))
        return digit_list
                
        