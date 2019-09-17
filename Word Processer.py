import os.path

print("")
print("After writing enter (save) in parenthisis to save your writting to a text file")
print("Type (save) again to add to that existing file, or type (exit) to exit")
print("")
#Text writting snd saving portion
Writing = True

while Writing:
    Textinput = input("")
    data=[Textinput]

    if "(save)" in Textinput:
        Save_text = Textinput.replace("(save)", "")
        with open("Writting_file.txt", "w") as out_file:
            out_file.write(Save_text)
            print("Writing saved")
            

    if "(save)" in Textinput and os.path.exists("Writting_file.txt"):
        Save_text = Textinput.replace("(save)", "")
        with open("Writting_file.txt", "a") as out_file:
            out_file.write(Save_text)

    if "(exit)" in Textinput:
        Writting = False 
