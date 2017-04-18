def find_max_min(numbers):
    if isinstance(numbers, list):
        numbers_types = (int, float, complex)
        if all(isinstance(x, numbers_types) for x in numbers):
            numbers.sort()
            if numbers[0] is numbers[len(numbers)-1]:
                print ([len(numbers)])
                return [len(numbers)]
            else:
                min_max = [numbers[0], numbers[len(numbers)-1]]
                print (min_max)
                return min_max
        else:
            print ('List contains non integers')
    else:
        raise TypeError