#Some instruction in using this high tech piece of software
print("")
print("After writing Enter (savefile) to save text to a new file")
print("Type (save) to save to that existing file, or type (exit) to exit")
print("")
#Text writting snd saving portion
Writing = True

while Writing:
    Textinput = input("")
    data=[Textinput]

    if "(savefile)" in Textinput:
            with open("Writting_file.txt", "a") as out_file:
                out_file.write('\n'.join(data))
                print("Writing saved")

    if "(save)" in Textinput:
            with open("Writting_file.txt", "a") as out_file:
                out_file.write('\n'.join(data))
                print("Writing saved")
        
    if "(exit)" in Textinput:
        print("Exiting program")
        Writing = False
