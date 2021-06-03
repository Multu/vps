def is_palindrome(s):
    if len(s) == 0:
        return True
    elif s[0] == s[-1]:
        trimmed_str_chars = []
        for i in range(1, len(s) - 1):
            trimmed_str_chars.append(s[i])
        trimmed_str = ''.join(trimmed_str_chars)

        return is_palindrome(trimmed_str)
    else:
        return False
