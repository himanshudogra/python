print("Hello!")
word1 = input("Enter something: ")
word2 = input("Enter another thing: ")
word3 = input("Enter a third thing: ")
word4 = input("And yet another thing: ")

print("You entered " + word1 + ", " + word2 + ", " + word3 + " and " + word4 + ".")

print('You entered {}, {}, {} and {}.'.format(word1,word2,word3,word4))
print('You entered %s, %s, %s and %s.'% (word1,word2,word3,word4))
print(f"You entered {word1}, {word2}, {word3} and {word4}.")