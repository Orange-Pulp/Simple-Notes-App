#This thing is used for checking file directories and some other stuff
import os.path

print("")
print("|-----------------------------------------------------------------------------|")
print("|After typing enter (save) in parenthisis to save to a text file in the       |")
print("|same directory as this application. Enter (exit) in parenthisis to quit      |")
print("|-----------------------------------------------------------------------------|")
print("")

Writing = True

while Writing:
    Textinput = input()
    data = (Textinput)
    if "(save)" in Textinput:
        Save_text = Textinput.replace("(save)", "") # This removes the "(save)" so that it won't appear in the save file
        if os.path.exists("Writting file.txt"): # This allows the program to append the save file, so that it doesn't open a new file every time you save.
            with open("Writting file.txt", "a") as file:
                file.write(Save_text)
                print("Writting saved")
        else:
            with open("Writting file.txt", "w") as file:
                file.write(Save_text)
                print("Writing saved")

    if "(exit)" in Textinput:
        Writting = False 
