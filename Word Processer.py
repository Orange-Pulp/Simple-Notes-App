#This thing is used for checking directories and some other stuff
import os.path

print("")
print("After writing enter (save) in parenthisis to save your writting to a text file")
print("Type (save) again to add to that existing file, or type (exit) to exit")
print("")

Writing = True

while Writing:
    Textinput = input(">")
    data=[Textinput]
#Some fancy stuff for writting text to files amoung other stuff 
    if "(save)" in Textinput:
        Save_text = Textinput.replace("(save)", "")
        if os.path.exists("Writting file.txt"): #This is checking if we already saved text to a file. If so we will continue to use that one insdead of creating another 
            with open("Writting file.txt", "a") as file:
                file.write(Save_text)
                print("Writting saved")
        else:
            with open("Writting file.txt", "w") as file:
                file.write(Save_text)
                print("Writing saved")

    if "(exit)" in Textinput:
        Writting = False 
