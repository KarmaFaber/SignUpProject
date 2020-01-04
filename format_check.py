import re 
#-all requirements-------------
def formar_cheker_all(str):
    pass


#-empty---------------------------
def empty_check(str):
    empty=""
    str = "    \n  \r  \t   "
    if not str.strip(): # The String Is Only Spaces!
        return empty==True

#-size-----------------------------
def size_check(str):
    return len(str)


#letters: lower and upper-----------
def lov_check(str):
    str_lo = 0
    for i in str:
        if i.islower():
            str_lo += 1
    #print("The number of lowercase letters in your phrase is:", str_lo)
    return str_lo

def cap_check(str):
    str_up = 0
    for i in str:
        if i.isupper():
            str_up += 1
    #print("The number of uppercase letters in your phrase is:", str_up)
    return str_up

#numbers ----------------   
def num_check(str):
    str_num =0
    for i in str:
        if i.isnumeric():
            str_num += 1
    #print("The number of numbers in your phrase is:", str_num)
    return str_num
 
#-characters ----------------------
def char_check_1(str): 
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
     
    if(regex.search(str) == None): 
        print("String is not accepted") 
    else: 
        print("String is accepted.") 


""" # Driver Code 
if __name__ == '__main__' : 

    # Enter the string 
    string = "Geexj*-ks"

    # calling run function  
    char_check(str)  """

#special char checker #_2
from string import ascii_letters, digits
def char_check_2(str): 
    if set(str).difference(ascii_letters + digits):
        print("has special char")
    else:
        print("not special char")






#isupper() ---------------------> 
#string.isupper()
#Returns :
#1.True- If all characters in the string are uppercase.
#2.False- If the string contains 1 or more non-uppercase characters.

#islower()------------------------>
#string.islower()
#Returns :
#1.True- If all characters in the string are lower.
#2.False- If the string contains 1 or more non-lowercase characters.
