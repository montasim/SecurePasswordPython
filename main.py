#    useded for string function
import string
#    needed for random function
import random

def GeneratePassword():
        #   give ascii lowercase character from a-z sequentially
        asciiLowercase = string.ascii_lowercase
        #   print(asciiLowercase)

        #   give ascii uppercase character from a-z sequentially
        asciiUppercase = string.ascii_uppercase
        #   print(asciiUppercase)

        # give ascii digits from 1-9-0 sequentially
        asciiDigits = string.digits
        #   print(asciiDigits)

        # give ascii punctuation
        asciiPunctuation = string.punctuation
        #   print(asciiPunctuation)

        # give ascci lowercase + uppercase + digits + punctuation and make a group
        asciiPrintable = string.printable
        #   print(asciiPrintable)

        #   ask user for password length
        passwordLength = int(input("Enter Your Password Length: "))

        emptyString = []  # take an empty string

        #   add ascii lowercase elements to emptyString
        emptyString.extend(list(asciiLowercase))
        #   add ascii uppercase elements to emptyString
        emptyString.extend(list(asciiUppercase))
        #   add ascii digits elements to emptyString
        emptyString.extend(list(asciiDigits))
        #   add ascii punctuation elements to emptyString
        emptyString.extend(list(asciiPunctuation))

        #   print emptyString that has lowercase + uppercase + digits + punctuation elements
        #   print(emptyString)

        print("Your Password Is: ")

        #   method 1
        #   random.shuffle(emptyString) #   shuffle elements of emptyString
        #   print(emptyString)  #   prints random string that is shuffled
        #   print("".join(emptyString[0:passwordLength])) #   print random string according from emptyString that starts from length 0 to passwordLength

        #   method 2
        #   print random string according from emptyString that starts from length 0 to passwordLength
        #   join function join the elements with given delimeters
        print("".join(random.sample(emptyString, passwordLength)))


def SecureExistingPassword():
    #   make a tauple that contains a predefined list that will replace character
    SECURE = (('a', '@'), ('A', '@'), ('e', '3'), ('E', '3'), ('i', '!'),
              ('I', '!'), ('m', 'w'), ('M', 'W'), ('o', '0'), ('O', '0'), ('s', '$'), ('S', '$'), ('and', '&'),
              ('And', '&'), ('AND', '&'))

    #   take existing password as input
    existingPassword = input("Enter Your Existing Password: ")

    #   a = tauple first character
    #   b = tauple second character
    for a, b in SECURE:
        #   replace() is used to replace a with b
        existingPassword = existingPassword.replace(a, b)
    
    #   print secure password
    print(f"Your Secured Password is: {existingPassword}")

#   this main() function will ask for input
def main():
    print("What do you want to do?")
    print("1. Make a new password: ")
    print("2. Secure existing password")
    print("3. Exit")

    Input = int(input("Enter your choice: "))

    #   enter 3 for exit
    if (Input == 3):
        exit()
    #   enter 1 for password generation
    elif (Input == 1):
        GeneratePassword()
        afterRun()
    #enter 2 for secure existing password
    elif (Input == 2):
        SecureExistingPassword()
        afterRun()
    #   if 1, 2, 3 is not inserted ask again for input
    else:
        print("Invalid Input")
        main()

def afterRun():
        print("Run again?\n1. Yes\n2. No\nEnter your choice: ", end="")
        afterRun = input()
        #   enter 1 to re-run program
        if afterRun == '1':
            main()
        #   enter 2 to exit program
        if afterRun == '2':
            exit()
        #   if 1, 2 is not entered shows invalid input and ask for input again
        else:
            print("Invalid Input")
            main()

#   main program begeins here
if __name__== "__main__":
    main()
