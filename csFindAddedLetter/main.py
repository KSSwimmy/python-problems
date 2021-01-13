# You are given two strings, str_1 and str_2, where str_2 is generated by randomly suffling str_1 and then adding one letter at the random position

# Write a function that returns the letter that was add to str_2

def csFindAddedLetter(str_1, str_2):

    '''
    We use a for loop to go through the strings, then compare str_1
    to str_2. This comparison counts the occurance of each letter
    , and from that determines which string is longer.
    '''

    for i in str_2:
        if str_2.count(i) != str_1.count(i):
            return i


str_1 = "bcde"
str_2 = "bcdef"
print(csFindAddedLetter(str_1, str_2))


#2 
def csFindAddedLetter(str_1, str_2):
    
    s1_list = list(str_1)
    s2_list = list(str_2)
    
    for i in s1_list:
        s2_list.remove(i)
    return s2_list[0]
    
    
str_1 = "xqmxtheyvpdqounqmfyaqdqxwe"
str_2 = "xqmxtheyvpdqounqmfyaqxdqxwe"
print(csFindAddedLetter(str_1, str_2))


#3 
'''
ord() returns the unicode number of a given character
so str_2 will add the number to result, giving us one huge number.
Then str_1 will subtract numbers giving us a balance number.  
Notice the return takes the unicode number and turns
it back into a letter via chr()
'''
def csFindAddedLetter(str_1, str_2):
    
    result = 0
    
    for i in str_2:
        result += ord(i)
    for i in str_1:
        result -= ord(i)
        
    return chr(result)
    
    
str_1 = "xqmxtheyvpdqounqmfyaqdqxwe"
str_2 = "xqmxtheyvpdqounqmfyaqxdqxwe"
print(csFindAddedLetter(str_1, str_2))