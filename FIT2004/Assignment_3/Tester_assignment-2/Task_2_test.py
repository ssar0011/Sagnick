class TrieNode(object):

    def __init__(self, char: str):
        self.character = char
        self.children = []
        # Is it the last character of the word.`
        self.word_finished = False
        self.idx = []
        self.substr = []


def addSuffix(root, word):
    counter = 0
    while counter < len(word)-1:
        node = root
        for char in range(counter, len(word)):
            in_child = False
            for child in node.children:
                if child.character == word[char]:

                    node = child
                    in_child = True
                    break
            if in_child == False:
                new_node = TrieNode(word[char])
                node.children.append(new_node)
                node = new_node

        node.word_finished = True
        counter += 1


def addPrefix(root,word):
    substrings = []
    counter = len(word)-2
    while counter >= 0:
        node = root
        for char in range(counter, len(word)):
            in_child = False
            for child in node.children:
                if child.character == word[char]:
                    if char - counter >= 1:
                        #child.substr.append([word[counter:char + 1], counter])
                        #substrings.append([word[counter:char + 1], counter])
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

def findPrefix(root,prefix):
    node = root
    if not root.children:
        return []

    for char in prefix:
        found = False
        # Search through all the children of the present `node`
        child_length = len(node.children)
        k = 0
        while k < child_length:
            child = node.children[k].character
            if child == char:
                found = True
                node = node.children[k]
                break
            else:
                k += 1

        if found == False:
            return False, 0

    return node.records


def reverseSubstrings(filename):
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
    #print(suffix_array)
    reverse_string = string[::-1]
    counter = len(string) - 2
    while counter >= 0:
        prefix_array.append(reverse_string[counter:len(string)])
        counter -= 1

    root = TrieNode('*')
    addSuffix(root,string)

    return addPrefix(root,reverse_string)

if __name__ == "__main__":
    print(reverseSubstrings("string.txt"))