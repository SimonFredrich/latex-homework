import os

entries = os.listdir('./')
for entry in entries:
    if (entry[2] == "-" or entry[2] == "."):
        new_entry = ""

        if entry[2]=='-':
            new_entry = entry[6:10]+'_'+entry[3:5]+'_'+entry[0:2] + entry[10:]
        elif entry[2]=='.':
            new_entry = entry[6:10]+'_'+entry[3:5]+'_'+entry[0:2] + entry[10:]

        new_entry.replace(":", "_")
        new_entry.replace("(", "_")
        new_entry.replace(")", "_")

        print(new_entry)
        os.system("git mv " + entry + " " + new_entry)

