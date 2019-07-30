# Enter your code here. Read input from STDIN. Print output to STDOUT
def get_result(number):
    print(number[0]**number[1])
    print(pow(number[0],number[1],number[2]))

if __name__ == '__main__':
    input_ = list()
    for i in range(3):
        number = int(input())
        input_.append(number)
        
    get_result(input_)
