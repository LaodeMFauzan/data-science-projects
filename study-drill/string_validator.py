def string_validator(s):
    is_alnum,is_alpha,is_aldigit,is_lower,is_upper = False,False,False,False,False
    for i in range(len(s)):
        if(s[i].isalnum()):
            is_alnum = True
        if(s[i].isalpha()):
            is_alpha = True
        if(s[i].isdigit()):
            is_aldigit = True
        if(s[i].islower()):
            is_lower = True
        if(s[i].isupper()):
            is_upper = True    
    print(str(is_alnum)+"\n"+str(is_alpha)+"\n"+str(is_aldigit)+"\n"+str(is_lower)+"\n"+str(is_upper))
if __name__ == '__main__':
    s = input()
    string_validator(s)
