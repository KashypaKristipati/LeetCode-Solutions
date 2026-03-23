def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    else:
        reversed_num = 0
        original_num = x
        while x != 0:
            remainder = x % 10
            reversed_num = (reversed_num * 10) + remainder
            x = x // 10
        if reversed_num == original_num:
            return True
        else:
            return False

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(isPalindrome(121))  # Expected: True
    print(isPalindrome(-121))  # Expected: False