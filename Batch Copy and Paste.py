import os

path = (input("Enter path to folder: ")).replace('"', "")
endswith = input("\nWhat is the filename extension? (.txt, .html, etc). Leave blank if you want to edit every file in the folder: ")

filesinfolder = os.listdir(path)
selected_files = []

for filename in filesinfolder:
    if filename.endswith(endswith):
        selected_files.append(filename)

if not selected_files:
    print("\nNo files found with the specified extension.")
    exit()
else:
    print("\nThe following files will be edited:")
    for file in selected_files:
        print(file)

print("\nEnter/Paste your new content. Type \"please stop 837\" (without quotes) to save it.")
data = []
while True: 
    line = input()
    if line.lower() == "please stop 837":
        break
    data.append(line)


while True:
    confirmation = input("\nAre you sure you want to replace EVERYTHING in the selected files with the text? (y/n): " ).lower()
    if confirmation == "y":
        break
    elif confirmation == "n":
        print("Aborting task.")
        exit()

def write_to_file(filename):
    try:
        with open(f"{path}/{filename}", "w") as w:
            if len(data) > 1:
                w.write("")
                with open(f"{path}/{filename}", "a") as a:
                    for x in data:
                        a.write(f"{x}\n")
            else:
                w.write(data)

    except PermissionError as Error:
        return{print (f"{filename} : Not a file")}
    except Exception as Error:
        return {print (f"{filename} : {Error}")}
    return {print (filename, ": Success")}

for filename in selected_files:
    write_to_file(filename)

input("\n\nPress ENTER to exit")
