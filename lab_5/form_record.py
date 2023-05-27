import os

root, dirs, files = list(os.walk("pics/letters"))[0]
files.sort()


root_h, dirs_h, files_h = list(os.walk("pics/hists"))[0]
files_h.sort()

_, _, files_i = list(os.walk("pics/letters-invert"))[0]
files_i.sort()

with open("Лабораторная работа №5.md", "w") as file:

    for i in range(len(files)):
        title = f"{i+1}. \n\n"
        h = f"![](pics/hists/{files_h[i]})\n\n"
        s = f"![](pics/letters/{files[i]})\n\n"
        i = f"![](pics/letters-invert/{files_i[i]})\n\n"

        file.writelines([title, s, i, h])