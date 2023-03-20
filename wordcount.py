"""Count words in file."""

# open the file
# strip and split the file
# we create a dictionary empty string
# we loop the new_file list
# if the words not in the new_file list, add to the dictionary
# we have a count to count the number of words.


# put your code here.
dict = {}
def count_words(filename):
    new_dict = {}
    newfile = open('test.txt')

    for line in newfile:
        line = line.rstrip()    
        text_data = line.split()
        print(text_data)
    
        for word in text_data:
            new_dict[word] = new_dict.get(word, 0) +1
            
            #if word not in new_dict:
            #    new_dict[word] = 0
            #new_dict[word] += 1
    
    #print(new_dict) ; print

    for word, count in new_dict.items():
        print(word, count)

    """
    for keys, values in text_data.items():
        if text_data not in new_dict.keys():
            new_dict[keys] = new_dict(values) + 1
    print(new_dict)
    """
    return new_dict
            
dict = count_words('test.txt')

print(dict)




