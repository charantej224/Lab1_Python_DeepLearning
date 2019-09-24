'''
Question1 :
Write a program to find a longest substring without repeating characters from a given string input from the console.
Sample Input: ‘ababcdxa’
Sample Output: abcdx
'''


class StringOperations:
    def longest_substring(self, input_string):
        char_list = []
        temp_string = ''
        longest_substring = ''
        for a in input_string:
            if a in char_list:
                char_list.clear()
                if len(longest_substring) < len(temp_string):
                    longest_substring = temp_string
                temp_string = ''
            if a not in char_list:
                char_list.append(a)
                temp_string += a

        print(longest_substring)
