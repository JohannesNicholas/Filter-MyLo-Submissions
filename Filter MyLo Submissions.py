#Script for filtering and moving submission files downloaded from MyLo.
#Author: Johannes Nicholas https://github.com/JohannesNicholas

from os import listdir, rename, mkdir, remove
import zipfile

input("Place this .py file in the same directory as the submissions.\n(Enter to continue)")

#get all the files
files = listdir("./") #all the files in current directory
print(len(files), "files detected.")


#get all the students
noSubmissions = [] #students who did not submit anything
print("Please enter the students first and last names that you are marking. This can be copy pasted in from a spreadsheet.")

#for each name entered
while True:
    name = input("(enter done when complete) Name:")

    #quit if done is entered
    if name == "done":
        break
    
    name = name.replace('\t', ' ')
    studentFiles = [] #files from one student


    #search for files that include the students name
    for file in files:
        if name in file:
            studentFiles.append(file)
            
    
    #if the student has no files
    if studentFiles == []:
        noSubmissions.append(name)
    else:
        mkdir(name) #make folder for student
        for file in studentFiles:
            
            #if .zip file
            if file.endswith(".zip"):
                try:
                    extractTo = name + "/" + file[-26:-4]
                    mkdir(extractTo) #make folder to extract into
                    with zipfile.ZipFile(file, 'r') as zipRef:
                        zipRef.extractall(extractTo)
                    remove(file) #.zip file no longer needed, delete it.
                except Exception as e:
                    print("\n\nError extracting file:\n", file)
                    print("This is probably due to a file name being too long.")
                    print("Please extract this file manually.\n\n")


            #not .zip file
            else:
                rename(file, name + "/" + file) #move to folder for student


        print(len(studentFiles), " files moved")


#output students that did not submit
print("No submissions from the following students:")
for name in noSubmissions:
    print(name)

input("Complete!\nPress enter to exit.")