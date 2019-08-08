class TrieNode(object):

    def __init__(self, char: str):
        self.character = char
        self.finished = False
        self.children = []
        self.records = []

def buildTrie(root,word,index):
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

def findPrefix(root,prefix):
    node = root
    if not root.children:
        return []

    for char in prefix:
        char_not_found = True
        # Search through all the children of the present `node`
        for child in node.children:
            if child.character == char:
                # We found the char existing in the child.
                char_not_found = False
                # Assign node as the child containing the char and break
                node = child
                break
        # Return False anyway when we did not find a char.
        if char_not_found:
            return False, 0

    return node.records

def query(filename, id_prefix, last_name_prefix):
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

    id_list = findPrefix(root_id, id_prefix)
    last_name_lst = findPrefix(root_last_name, last_name_prefix)

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
    '''
    with open(filename, 'r') as f:
        text_string = ''
        for line in f:
            if line[-1] != '\n':
                line += '\n'
            text_string += line

        record = []
        start = 0
        for c in range(len(text_string)):
            if text_string[c] == ' ' or text_string[c] == '\n':
                end = c
                record.append(text_string[start:end])
                start = end+1

        id = []
        last_name = []
        k1 = 1
        k2 = 3
        while k1 < len(record) and k2 < len(record):
            id.append(record[k1])
            last_name.append(record[k2])
            k1 += 6
            k2 += 6

        data = []
        for i in range(len(id)):
            data.append([i,id[i],last_name[i]])
    
    #print(data)
    # Now we must build our TRIE
    #root_id = TrieNode('*')
    for id in range(len(data)):
        buildTrie(root_id, data[id][1], id)
    #root_last_name = TrieNode('*')
    for last_name in range(len(data)):
        buildTrie(root_last_name, data[last_name][2], last_name)

    id_list = findPrefix(root_id, id_prefix)
    last_name_lst = findPrefix(root_last_name, last_name_prefix)

    output = []
    temp = set(id_list)
    output = [value for value in last_name_lst if value in temp]
    return output
    '''

if __name__ == "__main__":
    #root_id = TrieNode('*')
    #root_last_name = TrieNode('*')
    print("Final output: {}".format(query("database.txt","123","Wil")))
    print("Final output: {}".format(query("database.txt", "285", "Ne")))
    print("Final output: {}".format(query("database.txt", "92", "D")))
