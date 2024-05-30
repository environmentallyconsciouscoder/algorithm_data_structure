class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dict = {
            'a': False, 'b': False, 'c': False, 'd': False, 'e': False, 'f': False, 'g': False, 'h': False, 'i': False,
            'j': False, 'k': False, 'l': False, 'm': False, 'n': False, 'o': False, 'p': False, 'q': False, 'r': False,
            's': False, 't': False, 'u': False, 'v': False, 'w': False, 'x': False, 'y': False, 'z': False
        }

        for l in sentence:
            print("l", l)

            if l in dict:
                dict[l] = True

        all_true = all(dict.values())
        print("all_true", all_true)
        return all_true


    #faster
    def checkIfPangram(self, sentence: str) -> bool:
        # Initialize the dictionary with all letters set to False
        alphabet_dict = {char: False for char in 'abcdefghijklmnopqrstuvwxyz'}

        # Iterate through each character in the sentence
        for char in sentence:
            # If the character is in the dictionary, set its value to True
            if char in alphabet_dict:
                alphabet_dict[char] = True

            # If all values are True, return True early
            if all(alphabet_dict.values()):
                return True

        # After the loop, check if all values are True
        return all(alphabet_dict.values())