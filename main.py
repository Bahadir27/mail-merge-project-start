 # Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACE_HOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    # print(names)

with open("./Input/Letters/starting_letter.docx") as letter_file:
    letter_content = letter_file.read()
    # print(f"\nletter_content \n{letter_content}")
    for name in names:
        stripped_name = name.strip()
        # print(f"stripped_name {stripped_name}")
        new_letter = letter_content.replace(PLACE_HOLDER, stripped_name)
        # print(f"\nnew Letter \n{new_letter}")
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)
