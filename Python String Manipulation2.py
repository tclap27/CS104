#PYTHON STRING MANIPULATION CS104

#Algorithm for this problem:
#   1. Display the prompt and let the user input their data
#   2. Find the location of all commas in the input string
#   3. Break the input string into pieces and give each piece a variable name
#   4. Print out the pieces according to the specification
#
#----------------------------------------------------------

#   1. Display the prompt and let the user input their data
#last name, first name, favorite color, favorite animal, favorite team
#This is what I input> Eckert,Gil,blue,dog,Hawks. You will input your own information
#This line gets your input and stores it in a string called dataString

dataString = input("Please enter your last name, first name, your favorite color, your favorite animal, and your favorite team: ")

#----------------------------------------------------------

#   2. Find the location of all commas in the input string
#finds the location of the first comma in dataString and stores it in an integer variable 'firstcommaLocation' 
firstCommalocation = dataString.find(",")

#finds and stores the location of the second comma by going 1 character past the first comma
secondCommalocation = dataString.find(",",firstCommalocation+1)

#you do the next one by removing # in the line below and completing it
thirdCommalocation = dataString.find(",",secondCommalocation + 1)

#you do the next one by removing # in the line below and completing it
fourthCommalocation = dataString.find(",",thirdCommalocation + 1)

#-----------------------------------------------------------

#   3. Break the input string into pieces and give each piece a variable name
#use the comma locations to divide (slice) the dataString into pieces that we will store
#the line below extracts characters from dataString starting in location 0 up to the firstCommalocation character position
lastName = dataString [0:firstCommalocation]
firstName = dataString [firstCommalocation+1:secondCommalocation]

#you do the next one by removing # in the line below and completing it
favoriteColor = dataString [secondCommalocation+1: thirdCommalocation]

#you do the next one by removing # in the line below and completing it
favoriteAnimal = dataString [thirdCommalocation + 1: fourthCommalocation]

#you do the next one by removing # in the line below and completing it
favoriteTeam = dataString [fourthCommalocation + 1: fourthCommalocation + fourthCommalocation]

#------------------------------------------------------------

#   4. Print out the pieces according to the specification
#modify the print line by adding the other information to it.
#Your information will print differently. 
#My name is Gil Eckert, my favorite color is blue, my favorite animal is a dog, and my favorite team is the Hawks
print ("My name is "+ firstName+" "+lastName + ", my favorite color is " + favoriteColor + ", my favorite animal is a " + favoriteAnimal + ", my favorite team are the " + favoriteTeam)

      
