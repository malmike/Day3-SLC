def find_max_min(numbers):
    #Verify that the variable inserted is a list
    if isinstance(numbers, list):
        numbers_types = (int, float, complex)
        #Verify that all the values in the list are numbers
        if all(isinstance(x, numbers_types) for x in numbers):
            #Sort the values in the list
            numbers.sort()
            #Check whether the max and min numbers are equal and 
            #if so return a list containing the length of the list
            if numbers[0] is numbers[len(numbers)-1]:
                print ([len(numbers)])
                return [len(numbers)]
            #Else return a list containing the min and max value 
            #i.e the first and last value in the sorted list
            else:
                min_max = [numbers[0], numbers[len(numbers)-1]]
                print (min_max)
                return min_max
        else:
            print ('List contains non integers')
    else:
        raise TypeError