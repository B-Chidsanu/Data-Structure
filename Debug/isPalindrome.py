def isPalindrome(str):
    if len(str) <= 1:  # base case
        return True
    elif str[0] != str[-1]:  # base case
        return False
    else:  # recursive cases
        return isPalindrome(str[1:-1])


checklist = ["abcdcba", "atoyota", "kmitl",
             "manassanan", "programming", "fundamental"]
for i in checklist:
    print(isPalindrome(i))