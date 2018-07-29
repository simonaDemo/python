word = input ("Please, enter a word: ")
word = str(word)
rvs  = word[::-1] #from the beginning to the end of a word go backwards
if word == rvs:
    print ("This word is a palindrome")
else:
    print ("This word is not a palindrome")
         
    
        
