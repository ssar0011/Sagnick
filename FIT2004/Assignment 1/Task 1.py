def searchPunct(key,lst):
    '''
    Method traverses through punct array to find if the key matches any items in the toRemove array, if there is a match then the key is
    replaced with an empty space, so as to say it is removed.
    :param key: word from final_string
    :param lst: punct list is the parameter for this method
    :return: key is returned either without being altered or as an empty space
    precondition:
        toRemove list must exist for method to be useful
        filtered string must exist from which the key arg is obtained
    postcondition:
        the key is found in the toRemove list and replaced with an empty space or it is left alone and returned
    time complexity:
        best case: O(len(punct)) = O(1)
        average case: O(len(punct)) = O(1)
        worst case: O(len(punct)) = O(1)
    space complexity:
        O(2) = O(1), variables remain the same, no new variable are stored after each each iteration
    exception:
        if the key is not a string then raise a ValueError message
    '''
    if type(key) != type("Hello"):
        my_error = ValueError("key is not a string")
        raise my_error
    for item in lst:
        if key == item:
            key = ''
            return key
    return key


def preprocess(file):
    '''
    Method reads from text file and concatenates each word into a final_string. The final_string is then filtered where punctuation is
    removed from the string. Finally words from filter_string are individually appended to a list and auxiliary verbs are removed. The final
    preprocessed list is returned.
    :param file: text file that is being read into (Writing.txt)
    :return: preprocessed list, words that are not auxiliary verbs and without punctuation.

    pre-condition:
        Text file must exist, and all characters in text file must be lowercase
    post-condition:
        auxiliary verbs and punctuation is removed from string and processed into a list which is returned
    time complexity:
        worst case: O(nm)
    space complexity:
        O(nm)
    exception:
        N/A
    '''
    wordList = []
    toRemove = ['am', 'is', 'are', 'was', 'were', 'has', 'have', 'had', 'been', 'will', 'shall', 'may', 'can', 'would','should', 'might', 'could','a','an','the','and']
    punct = ['.', ',', '?', '!', ':', ';', '"']
    # Read lines into a list
    text_string = ''
    with open(file, 'r') as f:
        for line in f:
            if line[-1] != '\n':
                line += '\n'
            text_string += line

        final_string = ''
        for c in text_string:
            if c == '\n':
                c = ' '
            final_string += c

        if len(final_string) == 0:
            return False

        filter_string = ''
        for index in range(len(final_string)):
            filter_string += searchPunct(final_string[index], punct)

        # Traverse through filter_string, the moment the method finds a space, it appends the word to a list
        counter1 = 0
        counter2 = 0
        words = []
        if filter_string[-1] != ' ':
            filter_string += ' '
        for char in range(len(filter_string)):
            counter2 = char
            if filter_string[char] == ' ':
                words.append(filter_string[counter1:counter2])
                counter1 = counter2 + 1

        # Traverses through word list and compares each item to items in toRemove, if there is no match then that item is appended to
        # preprocess list
        n = 0
        processed = []
        while n < len(words):
            for aux in toRemove:
                if words[n] == aux:
                    n += 1
            processed.append(words[n])
            n += 1

        return processed

########## TEST CASES ##########

file_name = input("Give a file name: ")

def read_file():
    try:
        data = preprocess(file_name)
        print("Words are preprocessed.....")
        print_data = input("Do I need to display the remaining words (Y/N): ")
        if print_data == "Y":
            if data == False:
                print("Writing.txt is empty")
            else:
                for word in data:
                    print(word)
        elif print_data == "N":
            exit()
        else:
            my_error = ValueError("Given input was not valid")
            raise my_error
    except IOError:
        print("Text file does not exist")

read_file()