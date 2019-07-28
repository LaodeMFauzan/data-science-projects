def count_substring(string, sub_string):
    result = 0
    i = 0
    while i < len(string):
        if string[i:i+len(sub_string)].find(sub_string) == 0:
            result = result + 1
        i = i + 1
    return result

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)