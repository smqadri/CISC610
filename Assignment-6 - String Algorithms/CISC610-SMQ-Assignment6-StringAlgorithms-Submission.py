"""
Assignment 6: String Algorithms
Submission by Syed Mohiuddin Qadri, 10-Oct-2022

This program performs the following tasks:
1. Reads the text from the file
2. Performs the brute force search
3. Returns the words that have the following criteria:
    a. Longest Continual Substring of:
        i. Vowels
        ii. Consonants
    b. Longest Continual Prefix of:
        i. Vowels
        ii. Consonants
    c. Longest Continual Suffix of:
        i. Vowels
        ii. Consonants

If there are multiple words that tie in any criteria, it will return ALL words that tie. 

"""

def isVowel(x):             # This function checks if the character is a vowel or not
    if x in ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']:
        return True
    else:
        return False

def isConsonant(x):         # This function checks if the character is a consonant or not
    if x not in ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']:
        return True
    else:
        return False

def bruteForce(text, searchType, charType):        # This function performs the brute force search
    t1 = text.replace(".","")                # The text is replaced with a space
    word = t1.replace(",","")               # The text is replaced with a space
    l1 = len(word)      # The text which is to be checked for the existence of the pattern
    i = 0           # looping variables are set to 0
    
    substrings = ''

    while i < l1:       # iterating from the 0th index of text
        j = 0
        s = ''
        for j in range(i, l1):          # iterating from the ith index of text
            if ((charType =='vow' and isVowel(word[j]) == False) or (charType =='con' and isConsonant(word[j]) == False)):      # if the character is not a vowel or consonant
                if (len(s) != 0 and ((len(substrings) ==0) or len(s) > len(substrings))):                                   # if the substring is not empty and the length of the substring is greater than the length of the previous substring
                    substrings = s
                s = ''
                break       
            s = s + word[j]         # if the character is a vowel or consonant, then the character is added to the substring
            if (j == l1 -1):        # if the character is the last character of the text
                if (len(s) > len(substrings)):      # if the length of the substring is greater than the length of the previous substring
                    substrings = s
        i += 1
    #print(word)
    #print(substrings)
    max_len = -1
    res = ''
    ele = substrings 
    if (searchType == 'sub'):       # If the search type is 'sub', then the longest continual substring is returned
        if len(ele) > max_len:    # If the length of the substring is greater than the max length, then the substring is returned
            max_len = len(ele)      # The max length is set to the length of the substring
            res = ele               # The substring is returned
    
    elif (searchType == 'pre'):         # If the search type is 'pre', then the longest continual prefix is returned
        if word.startswith(ele) and len(ele) > max_len:     # If the word starts with the substring and the length of the substring is greater than the max length, then the substring is returned
            max_len = len(ele)                              # The max length is set to the length of the substring
            res = ele                                # The substring is returned
    
    elif (searchType == 'suf'):         # If the search type is 'suf', then the longest continual suffix is returned
        if word.endswith(ele) and len(ele) > max_len:       # If the word ends with the substring and the length of the substring is greater than the max length, then the substring is returned
            max_len = len(ele)                              # The max length is set to the length of the substring
            res = ele                                       # The substring is returned
    else:
        res = ''
    return (res,word)       # The substring is returned

def getLongestString(list_of_strings):          # This function returns the longest string from the list of strings
    max_len = -1
    res = list()                    # The list of strings is initialized
    for ele in list_of_strings:     # The list of strings is iterated
        if len(ele[0]) > max_len:       # If the length of the substring is greater than the max length, then the substring is returned
            max_len = len(ele[0])               # The max length is set to the length of the substring
            res = list()                        # The list of strings is initialized
            res.append(ele[1])                  # The substring is appended to the list of strings
        elif len(ele[0]) == max_len:    # Else If the length of the substring is equal to the max length, then the substring is appended to the list of strings
            res.append(ele[1])              # The substring is appended to the list of strings
    return res                      # The list of strings is returned



RaxTxtString = open('.\Assignment-6 - String Algorithms\lorem_ipsum.txt', 'r')          # The text file is opened
all_words = []              # The list of words is initialized
for word in RaxTxtString:       # The text file is iterated
    all_words = all_words + word.split()        # The words are split and appended to the list of words



# Finding the longest continual substring of vowels
sub_strs = list()
for i in all_words:         # The list of words is iterated
    sub_strs.append(bruteForce(i, 'sub', 'vow'))         # The longest continual substring of vowels is appended to the list of substrings
print ('Longest continual substring of vowels')
#print(sub_strs)
longest_str = getLongestString(sub_strs)            # The longest string is returned
print('Count: ', str(len(longest_str)))             # The count of the longest string is printed
print(getLongestString(sub_strs))                   # The longest string is printed
print('\n\n\n')


# Finding the longest continual substring of consonants
sub_strs = list()
for i in all_words:
    sub_strs.append(bruteForce(i, 'sub', 'con'))         # The longest continual substring of consonants is appended to the list of substrings
#print(sub_strs)
print ('Longest continual substring of consonants')     
longest_str = getLongestString(sub_strs)            # The longest string is returned
print('Count: ', str(len(longest_str)))             # The count of the longest string is printed
print(getLongestString(sub_strs))                   # The longest string is printed
print('\n\n\n')


# Finding the longest continual prefix of vowels
sub_strs = list()
for i in all_words:
    sub_strs.append(bruteForce(i, 'pre', 'vow'))         # The longest continual prefix of vowels is appended to the list of substrings
print('Longest continual prefix of vowels')
#print(sub_strs)
longest_str = getLongestString(sub_strs)            # The longest string is returned
print('Count: ', str(len(longest_str)))             # The count of the longest string is printed
print(getLongestString(sub_strs))                   # The longest string is printed
print('\n\n\n')


# Finding the longest continual prefix of consonants
sub_strs = list()
for i in all_words:     # The list of words is iterated
    sub_strs.append(bruteForce(i, 'pre', 'con'))         # The longest continual prefix of consonants is appended to the list of substrings
print('Longest continual prefix of consonants')
#print(sub_strs)
longest_str = getLongestString(sub_strs)            # The longest string is returned
print('Count: ', str(len(longest_str)))             # The count of the longest string is printed
print(getLongestString(sub_strs))                   # The longest string is printed
print('\n\n\n')


# Finding the longest continual suffix of vowels
sub_strs = list()
for i in all_words:
    sub_strs.append(bruteForce(i, 'suf', 'vow'))         # The longest continual suffix of vowels is appended to the list of substrings
print('Longest continual suffix of vowels')
#print(sub_strs)
longest_str = getLongestString(sub_strs)            # The longest string is returned
print('Count: ', str(len(longest_str)))             # The count of the longest string is printed
print(getLongestString(sub_strs))                   # The longest string is printed
print('\n\n\n')


# Finding the longest continual suffix of consonants
sub_strs = list()
for i in all_words:
    sub_strs.append(bruteForce(i, 'suf', 'con'))         # The longest continual suffix of consonants is appended to the list of substrings
print('Longest continual suffix of consonants')
#print(sub_strs)
longest_str = getLongestString(sub_strs)            # The longest string is returned
print('Count: ', str(len(longest_str)))             # The count of the longest string is printed
print(getLongestString(sub_strs))                   # The longest string is printed
print('\n\n\n')

RaxTxtString.close()




        
