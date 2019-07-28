def swap_case(s):
    result = ""
    for i in range(len(s)):
        if s[i].islower():
            result = result + s[i].upper()
        else : 
            result = result + s[i].lower()

    return result

if __name__ == '__main__':