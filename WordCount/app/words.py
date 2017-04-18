def words(sentence):
    #Check that the variable provided is a string
    if isinstance(sentence, str): 
        #Split each value in the string and assign to variable value
        values = sentence.split()
        #Create a dictionary word_dicts that will store the word count
        words_dict = {}
        #Loop through each item in values
        for i in values:
            #Check if the string is a digit and convert to an integer if so
            if i.isdigit():
                i = int(i)
            #Check if i is a key in words_dict and increment it's value by 1 if so
            if i in words_dict.keys():
                words_dict[i] += 1
            #Add i as a key in words_dict and it holds a value 1
            else:
                words_dict[i] = 1
        #Return words_dict
        return words_dict
    else:
        return TypeError