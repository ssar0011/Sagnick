class TrieNode(object):

    def __init__(self, char):
        self.character = char
        self.children = []
        self.word_finished = False
        self.idx = []
        self.substr = []
        self.records = []
        self.query_count = 0


### TASK 1 ####



def buildTrie(root, word, index):
    '''
    Functionality of buildTrie function is to build Trie data structure usiing given input. Each character in the input represents a node
    in the Trie, if the current node does not have a child that is the same as the character, it creates a new node and adds it to Trie
    data structure. If child == character, then save index at which character is and move to next one.
    Time complexity:
        Best: O(T)
        Worst: O(T)
    Space complexity:
        Best: O(T + NM)
        Worst: O(T + NM)
    Error handle:
    Return: None
    Parameter:
        root: root of the Trie data structure
        word: word that is being added to Trie
    Precondition: root must be provided and word to add to data structure
    '''
    node = root
    for char in word:
        in_child = False
        for child in node.children:
            if child.character == char:
                child.records.append(index)
                node = child
                in_child = True
                break
        if in_child == False:
            new_node = TrieNode(char)
            new_node.records.append(index)
            node.children.append(new_node)
            node = new_node

    node.finished = True




def query(filename, id_prefix, last_name_prefix):
    '''
    The functionality of query is to provide the indexes at which the given id_prefix and last_name_prefix can be found within database.txt.
    This is done by creating two separate Tries. One for ID numbers and the other for last names. The id_prefix is searched in the
    ID Trie and a list of matching indexes is returned, the same is done for last name Trie. Then the items in each of these lists are
    compared and the intersecting values are returned.
    Time complexity:
        Best: O(k + l) if no matches for either were found
        Worst: O(k + l + N(k) + N(l))
    Space complexity:
        Best: O(k + l + NM)
        Worst: O(k + l + NM)
    Error handle: check if filename exists
    Return: intersection of id_list and last_name_lst
    Parameter:
        filename: database.txt
        id_prefix: prefix of identification number
        last_name_prefix: prefix of last name
    Precondition: database file must exist, and prefixes shoud be provided for ID number and last name
    '''

    with open(filename, 'r') as f:
        root_id = TrieNode('*')
        root_last_name = TrieNode('*')
        with open(filename) as f:
            lines = f.readlines()
            for i in range(len(lines)):
                lines[i] = lines[i][:-1]
                lines[i] = lines[i].split(' ')
                #print(lines)
                buildTrie(root_id,lines[i][1],int(lines[i][0]))
                buildTrie(root_last_name,lines[i][3],int(lines[i][0]))

    id_list = findPrefix(root_id, id_prefix,True)
    last_name_lst = findPrefix(root_last_name, last_name_prefix,True)

    #print(id_list)
    #print(last_name_lst)
    output = []
    i = 0
    j = 0
    while i < len(id_list) and j < len(last_name_lst):
        if id_list[i] == last_name_lst[j]:
            output.append(id_list[i])
            i += 1
            j += 1
        elif id_list[i] > last_name_lst[j]:
            j += 1
        elif id_list[i] < last_name_lst[j]:
            i += 1

    return output

### TASK 2 ###

def addSuffix(root, word):
    '''
    The following function adds the suffixes of the string to the Trie data structure
    Time complexity:
        Best: O(K^2)
        Worst: O(K^2)
    Space complexity:
        Best: O(K^2)
        Worst: O(K^2)
    Error handle: None
    Return: None
    Parameter:
        root: root node of Trie
        word: string of which its suffixes will be added
    Precondition: provide a root node and string
    '''
    counter = 0
    while counter < len(word) - 1:
        node = root
        for char in range(counter, len(word)):
            in_child = False
            for child in node.children:
                if child.character == word[char]:
                    child.idx.append(counter)
                    node = child
                    in_child = True
                    break
            if in_child == False:
                new_node = TrieNode(word[char])
                new_node.idx.append(counter)
                node.children.append(new_node)
                node = new_node

        node.word_finished = True
        counter += 1


def addPrefix(root, word):
    '''
    The following function adds the prefixes of the string to the already existing Trie data structure. If the characters of the word
    already exist in Trie then append the prefix to substrings list.
    Time complexity:
        Best: O(K^2)
        Worst: O(K^2)
    Space complexity:
        Best: O(K^2)
        Worst: O(K^2)
    Error handle: None
    Return: list of substrings of which their reverses exist.
    Parameter:
        root: root node of Trie
        word: string of which its prefixes will be added
    Precondition: provide a root node and string
    '''
    substrings = []
    counter = len(word) - 2
    while counter >= 0:
        node = root
        for char in range(counter, len(word)):
            in_child = False
            for child in node.children:
                if child.character == word[char]:
                    if char - counter >= 1:
                        # child.substr.append([word[counter:char + 1], counter])
                        # substrings.append([word[counter:char + 1], counter])
                        substrings.append(word[counter:char + 1])
                    node = child
                    in_child = True
                    break
            if in_child == False:
                new_node = TrieNode(word[char])
                node.children.append(new_node)
                node = new_node

        node.word_finished = True
        counter -= 1

    return substrings


def findPrefix(root,prefix,Task_1):
    '''
    Functionality of findPrefix is to find the given prefix within the Trie data structure. If present, return the index at which it occurs
    and if not the return False.
    Time complexity:
        Best: O(n), n = length of prefix
        Worst: O(n), n = length of prefix
    Space complexity:
        Best: O(n), n = length of prefix
        Worst: O(n), n = length of prefix
    Error handle: check if root node has children
    Return: if it is Task 1, return index of database, if Task 2 then return the prefix with index at which it occurs
    Parameter:
        root: root node of Trie
        prefix: prefix that is being searched within Trie
    Precondition: Trie data structure must exist, also parameters must be provided
    '''
    node = root
    if not root.children:
        return False

    for char in prefix:
        char_not_found = True
        # Search through all the children of the present `node`
        for child in node.children:
            index = node.idx
            if child.character == char:
                # We found the char existing in the child.
                char_not_found = False
                # Assign node as the child containing the char and break
                node = child
                index = node.idx
                break
        # Return False anyway when we did not find a char.
        if char_not_found:
            return False
    if Task_1:
        return node.records
    return [prefix, index]


def reverseSubstrings(filename):
    '''
    The following funtion first finds the suffixes of the string and creates a Trie data structure, then finds the prefixes of the string
    and adds these on top of the suffix trie. The intersecting nodes are saved and later returned as reverse substrings.
    Time complexity:
        Best: O(K^2 + P)
        Worst: O(K^2 + P)
    Space complexity:
        Best: O(K^2)
        Worst: O(K^2)
    Error handle: check if filename exists
    Return: susbtrings with reverse present in string and their indexes
    Parameter:
        filename: text file with string
    Precondition: provide a valid text file with string that consists of all lowercase characters
    '''
    with open(filename, 'r') as f:
        string = ''
        for line in f:
            string += line
    suffix_array = []
    prefix_array = []
    suffix = 0
    while suffix < len(string) - 1:
        suffix_array.append(string[suffix:len(string)])
        suffix += 1
    reverse_string = string[::-1]
    counter = len(string) - 2
    while counter >= 0:
        prefix_array.append(reverse_string[counter:len(string)])
        counter -= 1

    root = TrieNode('*')
    addSuffix(root, string)

    matches = addPrefix(root, reverse_string)

    filter_matches = []
    for w in matches:
        if w[::-1] in matches:
            filter_matches.append(w)

    output = []
    for word in filter_matches:
        word = word[::-1]
        if findPrefix(root, word,False) != False and findPrefix(root,word,False) not in output:
            output.append(findPrefix(root,word,False))

    last_output = []
    for item in output:
        if len(item[1]) > 1:
            for i in range(len(item[1])):
                last_output.append([item[0], [item[1][i]]])
        else:
            last_output.append(item)

    for item in last_output:
        item[1] = item[1][0]

    return last_output


if __name__ == "__main__":

    while True:
        try:
            file = input("Enter the file name of the query database: ")
            idPrefix = input("Enter the prefix of the Identification number: ")
            LastNamePrefix = input("Enter the prefix of the last name: ")
            records = query(file, idPrefix, LastNamePrefix)
            if records == False:
                print("No records were found")
                proceed = input("Would you like to continue query to database? (Y/N) ")
                if proceed == "Y":
                    print('\n')
                    continue
                else:
                    print('\n')
                    break
            print("{} record(s) found".format(len(records)))
            for i in range(len(records)):
                print("Index number: {}".format(records[i]))
            proceed = input("Would you like to continue query to database? (Y/N) ")
            if proceed == "Y":
                print('\n')
                continue
            else:
                print('\n')
                break
        except FileNotFoundError:
            print("Error: File does not appear to exist.")
            print("Please enter file name of the query database again")
            print('\n')
            continue

    while True:
        try:
            file = input("Enter the file name for searching reverse substring: ")
            result = reverseSubstrings(file)
            final_output = ''
            for value in result:
                final_output += value[0] + '({}), '.format(str(value[1]))
            # print(final_output)
            break
        except:
            print("Error: File does not appear to exist.")
            print("Please enter the file name again")
            print('\n')
            continue