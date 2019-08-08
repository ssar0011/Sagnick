class Decipher:

    def __init__(self):
        self.message = ''

    def messageFind(self,file_name):
        '''
        The following function finds the longest common subsequence between two strings provided in the encrypted text file. A dynamic
        programming approach was used where a table was formed of size nm where n and m are the sizes of the first and second string
        respectively. Every time there is a match b/w two letters, the value at DP_table[row-1][col-1] is incremented by 1 and inserted
        into DP_table[row][col]. Then loop has reached the end of the table, the algorithm backtracks recursively to find LCS.

        Time complexity: O(nm)
        Space complexity: O(nm)
        Error handling:
        Return: None
        Parameter: file_name - User provides encrypted text file to find LCS
        Pre-requisite: encrypted text file must be provided in order to find LCS
        '''
        with open(file_name, 'r') as f:
            array = f.readlines()
        string1 = array[0]
        string2 = array[1]
        n = len(string1)
        m = len(string2)

        DP_table = [[0 for k in range(m+1)] for l in range(n+1)]

        for i in range(n+1):
            for j in range(m+1):
                if i == 0 or j == 0:
                    DP_table[i][j] = 0
                elif string1[i-1] == string2[j-1]:
                    DP_table[i][j] = DP_table[i-1][j-1] + 1
                else:
                    DP_table[i][j] = max(DP_table[i-1][j],DP_table[i][j-1])
        self.message = self.backTrack(DP_table,string1,string2,len(string1),len(string2))
        self.message = self.message[::-1]

    def backTrack(self,table,seq1,seq2,i,j):
        '''
        Once the DP_table is full, the backTrack algorithm starts at at the last cell of the table, and travels back up the table. When
        the length decreases, it indicates that there must have been a common element b/w the two strings, and that character is added
        to the string.

        Time complextiy: O(nm)
        Space complextiy: O(nm)
        Error handle:
        :return: longest common subsequence b/w seq1 and seq2
        :param table: DP_table solution
        :param seq1: first sequence of characters
        :param seq2: second sequence of characters
        :param i: seq1[i]
        :param j: seq2[j]
        Pre-requisite: self.messageFind function must be present in program in order to formulate the DP_table required for backtracking
        '''
        if i == 0 or j == 0:
            return ''
        if seq1[i-1] == seq2[j-1]:
            return seq1[i-1] + self.backTrack(table,seq1,seq2,i-1,j-1)
        elif table[i][j-1] > table[i-1][j]:
            return self.backTrack(table,seq1,seq2,i,j-1)
        return self.backTrack(table,seq1,seq2,i-1,j)


    def dictContains(self, word, dictionary):
        '''
        Finds if the substring is present in the dictionary text file provided, if it is return the index at which it is found within
        the dictionary.

        Time complexity: O(N)
        Space Complexity: O(N)
        Error Handle: None
        Return:
            if substring in dictionary, (True, index at which it is found)
            if not found, False
        :param word - substring found in dp table
        :param dictionary - dictionary text file provided
        :param size
        Pre-requisite: dictionary text file must be present as well as a substring from dp table
        '''
        i = 0
        while i < len(dictionary):
            if word == dictionary[i]:
                return True, (i + 1)
            else:
                i += 1
        return False

    def wordBreak(self, dict):
        '''
        The following function retrieves the Longest Common Subsequence and partitions the string into separate words in accordance to
        the words found in the dictionary text file provided by the user. The solution involved a dynamic programming table of size kM.
        The function traversed down the columns of the dp table, checking for substrings of size 1 to M. When there is a valid substring
        found, the cell at which the substring corresponds to on the table is replaced with the index at which the substring is found in
        the dictionary file. Once the table is filled, the program traverses through the M'th row in the dictionary to print out the
        full string.

        Time complexity: O(kM*NM)
        Space complexity: O(kM*NM)
        Error handle:
        Return: None
        Parameter: dict - User provides a dictionary text file
        Pre-requisite: dictionary text file and longest common subsequence found in self.MessageFind function
        '''
        text_string = ''
        with open(dict, 'r') as f:
            text_string = ''
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

            # Traverse through final_string, the moment the method finds a space, it appends the word to a list
            counter1 = 0
            counter2 = 0
            my_dict = []
            if final_string[-1] != ' ':
                final_string += ' '
            for char in range(len(final_string)):
                counter2 = char
                if final_string[char] == ' ':
                    my_dict.append(final_string[counter1:counter2])
                    counter1 = counter2 + 1

        max_index = 0
        for i in range(1, len(my_dict)):
            if len(my_dict[i]) > len(my_dict[max_index]):
                max_index = i

        m = len(self.message)
        max_word = my_dict[max_index]
        n = len(max_word)

        wb_table = [[0 for k in range(m + 1)] for c in range(n + 1)]

        new_string = " " + self.message
        matched_index = 0
        match_counter = 0
        row_match = 0

        for col in range(m + 1):
            row = 0

            while row <= n:
                if row == 0 or col == 0:
                    wb_table[row][col] = 0
                    row += 1
                elif (col - (row)) >= 0:
                    substr = new_string[col:col + row]
                    if row > 1:
                        if row <= row_match and match_counter > 0:
                            if row == row_match:
                                wb_table[row][col] = matched_index
                                match_counter -= 1
                                row += 1
                            else:
                                wb_table[row][col] = matched_index
                                row += 1

                        else:
                            in_dict = self.dictContains(substr, my_dict)
                            if in_dict != False:
                                wb_table[row][col] = in_dict[1]
                                matched_index = in_dict[1]
                                match_counter = len(substr)-1
                                row_match = row
                                row += 1
                            else:
                                wb_table[row][col] = wb_table[row - 1][col]
                                row += 1
                    else:
                        in_dict = self.dictContains(substr, my_dict)
                        if in_dict != False:
                            wb_table[row][col] = in_dict[1]
                            row += 1
                        else:
                            wb_table[row][col] = wb_table[row - 1][col]
                            row += 1

                elif ((row - 1) + col) > m:
                    wb_table[row][col] = wb_table[row][col - 1]
                    row += 1
                elif (col - row) < 0:
                    substr = new_string[col:col + row]
                    if row > 1:
                        if row <= row_match and match_counter > 0:
                            if row == row_match:
                                wb_table[row][col] = matched_index
                                match_counter -= 1
                                row += 1
                            else:
                                wb_table[row][col] = matched_index
                                row += 1
                        else:
                            in_dict = self.dictContains(substr, my_dict)
                            if in_dict != False:
                                wb_table[row][col] = in_dict[1]
                                matched_index = in_dict[1]
                                match_counter = len(substr)-1
                                row_match = row
                                row += 1
                            else:
                                wb_table[row][col] = wb_table[row - 1][col]
                                row += 1
                    else:
                        in_dict = self.dictContains(substr, my_dict)
                        if in_dict != False:
                            wb_table[row][col] = in_dict[1]
                            row += 1
                        else:
                            wb_table[row][col] = wb_table[row - 1][col]
                            row += 1

        # Once dp table is full, traverse through last row and partition subsequence into respective words relative to that of the
        # dictionary text file.th
        if len(my_dict) == 0:
            self.message = self.message
        else:
            if wb_table[n][m] == 0:
                message = ''
                value = m
            else:
                message = my_dict[wb_table[n][m] - 1]
                value = m-1
            while value >= 0:
                if wb_table[n][value] == 0:
                    if value != 0:
                        sub_message = ''
                        #sub_message += self.message[value-1]
                        v = value
                        while wb_table[n][v] == 0:
                            if v == 0:
                                break
                            sub_message = self.message[v-1] + sub_message
                            v-=1
                        message = sub_message + ' ' + message
                        value = v
                    else:
                        self.message = message
                        break
                elif wb_table[n][value] == wb_table[n][value + 1]:
                    value -= 1
                else:
                    message = my_dict[wb_table[n][value] - 1] + ' ' + message
                    value -= 1



    def getMessage(self):
        return self.message




if __name__ == '__main__':
    decipher = Decipher()
    while True:
        try:
            encrypt = input("The name of the file, containes two encrypted texts: ")
            decipher.messageFind(encrypt)
            break
        except FileNotFoundError:
            print("Error: File does not appear to exist.")
            print("Please enter name of the encrypted file again")
            continue
    while True:
        try:
            dictionary = input("The name of the dictionary file: ")
            print("Deciphered message is: {}".format(decipher.getMessage()))
            decipher.wordBreak(dictionary)
            print("True message is: {}".format(decipher.getMessage()))
            break
        except FileNotFoundError:
            print("Error: File does not appear to exist.")
            print("Please enter name of the dictionary file again")
            continue
