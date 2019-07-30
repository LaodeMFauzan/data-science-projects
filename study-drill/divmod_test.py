def get_divmod(number):
    print(number[0] // number[1])
    print(number[0] % number[1])
    print(divmod(number[0],number[1]))

if __name__ == '__main__':
    input_ = list()
    for i in range(2):
        number = int(input())
        input_.append(number)
        
    get_divmod(input_)