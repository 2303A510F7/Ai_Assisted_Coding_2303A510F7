#ask 3: Palindrome Check
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
# Test cases
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("race a car"))  # False