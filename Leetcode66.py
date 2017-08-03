class Solution(object):
    def plusOne(self, digits):
        index = len(digits)-1
        digit = digits[index] + 1
        if digit < 10:
            digits[index] = digit
            return digits
        else:
            carry = 1
            digits[index] = 0
            index -= 1
            while index >= 0:
                digit = digits[index] + carry
                if digit == 10:
                    carry = 1
                    digits[index] = 0
                else:
                    digits[index] = digit
                    return digits
                index -= 1
            if index < 0 and carry == 1:
                digits[0] = 0
                return [1] + digits