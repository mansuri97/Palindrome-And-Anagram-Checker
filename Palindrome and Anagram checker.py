
#### ADAM MANSURI

#### Menu
menu = ["1) Enter a word","2) Checks number of times a letter occurs","3) Palindrome check","4) Anagram check","5) Exit"]

position = 0
while position<len(menu):
   print(menu[position])
   position=position+1

userMenu = input("Please select an option from 1-5: ")

### stage1 - putting word entered by user into a list
while userMenu == "1":
   userWord = input("Please enter a word: ").lower()
   list1=list(userWord)

# print list1
   position=0
   while position<len(menu):
      print(menu[position])
      position=position+1

   userMenu = input("Please select an option from 1-5: ")

### stage2 - checking how many times entered letter is in the word from stage 1
   if userMenu == "2" and userMenu != "5":
      userLetter = input("Please enter a letter to search: ")
      index = 0
      occurrence = 0
      while index<len(userWord):
         while userLetter == userWord[index]:
            occurrence = occurrence+1
            index=index+1
            break

         else:
             index=index+1
      print(userLetter, "occurs",occurrence, " times in the word",userWord)

      position=0
      while position<len(menu):
         print(menu[position])
         position=position+1
      userMenu = input("Please select an option from 1-5: ")


### stage3 - Palindrome, checks if word entered in stage 1 is a palindrome or not
   if userMenu == "3" and userMenu!="5":
      index=0
      while index<len(userWord)/2 +1:
         if userWord[index]!=userWord[-index-1]:
            print("This is not a palidrome")

            break
         index=index+1
      else:
         print("This is a palidrome!")

      position=0
      while position<len(menu):
         print(menu[position])
         position=position+1
      userMenu = input("Please select an option from 1-5: ")


### stage4 - Anagram
if userMenu == "4" and userMenu!="5":
   secondWord= input("Please enter a word to check if its an anagram of the first word: ")
   list2 = list(secondWord)

def isAnagram(userWord, secondWord):
    userWord = sorted(userWord)
    secondWord = sorted(secondWord)

counter=0
while counter<len(list):
   counter+=1

while counter<len(list2):
   counter+=1

if userWord == secondWord:
   print("This is an anagram")
else:
   print("This is not an anagram")
   position=0
   while position<len(menu):
      print(menu[position])
      position=position+1
   userMenu = input("Please select an option from 1-5: ")


### stage 5 - EXIT
if userMenu == "5":

   print("Exit")
