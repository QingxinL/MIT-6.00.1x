import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self,shift):
        map_cipher = {}
        # string.ascii_lowercase
        # string.ascii_uppercase
        # the key is the origin letter
        # the value is the letter after
        letters = string.ascii_uppercase + string.ascii_lowercase
        for char in letters:
            map_cipher[char] = ''
        for key, value in map_cipher.items():
            pos = letters.find(key)
            after = pos + shift

            if after > 25:
                after -= 26
            if key in string.ascii_uppercase:
                map_cipher[key] = letters[after]
            if key in string.ascii_lowercase:
                map_cipher[key] = letters[after].lower()
        return map_cipher





    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shift_down = ""
        map = self.build_shift_dict(shift)

        message_text = self.get_message_text()
        for char in message_text:
            try:
                after_shift = map[char]
            except KeyError:
                after_shift = char
            shift_down+=after_shift
        return shift_down



class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        Message.__init__(self,text)
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self,shift)
        self.message_text_encrypted = Message.apply_shift(self,shift)




    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()


    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self,shift)
        self.message_text_encrypted = Message.apply_shift(self,shift)



class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self,text)


    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''

        # try every possible shift value by for loop
        # store the real word number for each shift value
        # compare the real word numbers and find the maximum - 26-shift would be the best value
        # return the tuple: (best shift value + decrypted message)
        max_real_word_number = 0
        best_shift=0
        for shift in range(26):
            before_shift = Message.apply_shift(self, 26 - shift)
            before_shift_list = before_shift.split()
            count_of_real_word = 0
            for before in before_shift_list:
                if is_word(self.valid_words,before)==True:
                    count_of_real_word+=1

            if count_of_real_word>max_real_word_number:
                max_real_word_number=count_of_real_word
                best_shift = 26-shift
        decrypted = Message.apply_shift(self,best_shift)
        if best_shift==26:
            best_shift=0
        result = []
        result.append(best_shift)
        result.append(decrypted)
        return tuple(result)








        # count_of_real_word = 0
        # max_of_real_word = 0
        # final_list = []
        # best_shift=0
        # true_message = ""
        #
        # for shift in range(26):
        #     before_shift = Message.apply_shift(self,26-shift)
        #     # if is_word(self.valid_words,before_shift)==True:
        #     #     count_of_real_word+=1
        #     before_shift = before_shift.split()
        #     for before in before_shift:
        #         if is_word(self.valid_words, before) == True:
        #             count_of_real_word+=1  # need to find the number of real words with this shift
        #             true_message+=before
        #             true_message += " "
        #     if count_of_real_word>max_of_real_word:
        #         max_of_real_word=count_of_real_word
        #         best_shift = 26-shift
        #
        #
        # final_list.append(best_shift)
        # final_list.append(true_message)
        # return tuple(final_list)





def decrypt_story():
    encrypted = get_story_string()
    encrypted_obj = CiphertextMessage(encrypted)
    result = encrypted_obj.decrypt_message()
    return result









#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())
