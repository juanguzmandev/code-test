def longest(s):
    if(len(s) <= 1):
        return 'Longest substring is: ' + str(len(s))
    
    substring = ''
    length = 1

    for c in s:
        if c not in substring:
            substring = substring + c
            print(substring)
            length = max(length, len(substring))

        else:
            substring = substring.split(c)[1] + c    
            print(substring)

    return 'Longest substring is: ' + str(length)

if __name__ == '__main__':
    print(longest('abcabcdbb'))