def sum_0(data): 
    # Implement here

    return_pair = [0, 0]

    i = 0
    j = len(data)-1
    min_num = 100000000
    while i < j :
        if min_num > abs(data[i]+data[j]) :
            min_num = abs(data[i]+data[j])
            return_pair[0] = data[i]
            return_pair[1] = data[j]
        if abs(data[i]+data[j-1]) > abs(data[i+1]+data[j]) :
            i = i+1
        else :
            j = j-1

    return return_pair

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    given_data = input()

    data = [int(v.strip()) for v in given_data.split()]

    print (*sum_0(data)) 

if __name__ == "__main__":
    main()
