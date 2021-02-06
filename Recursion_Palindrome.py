def palindrom(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrom(s[1:-1])

s = input('Write something for check palindrom or not palindrome')
resoult = palindrom(s)
if resoult == True:
    print(s,'Palindrome')
else:
    print(s,'not Palindrome')    