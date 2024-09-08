from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

filename = None

def newfile():
    global filename
    Text.delete(0.0, END)
    
def savefile():
    global filename
    t = Text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    t.close()
    
def saveas():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = Text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Oops!", message="Unable to save file...")
        
def openfile():
    f = askopenfile(mode='r')
    t = f.read()
    Text.delete(0.0, END)
    Text.insert(0.0, t)
    
def bold():
    current_tags = Text.tag_names("sel.first")
    if "bt" in current_tags:
        Text.tag_remove("bt", SEL_FIRST, SEL_LAST)
    else:
        Text.tag_add("bt", SEL_FIRST, SEL_LAST)
        Text.tag_config("bt", font=("Georgia", "12", "bold"))
    
    
def underline():
    current_tags = Text.tag_names("sel.first")
    if "u" in current_tags:
        Text.tag_remove("u", SEL_FIRST, SEL_LAST)
    else:
        Text.tag_add("u", SEL_FIRST, SEL_LAST)
        Text.tag_config("u", underline=1)

def italic():
    current_tags = Text.tag_names("sel.first")
    if "i" in current_tags:
        Text.tag_remove("i", SEL_FIRST, SEL_LAST)
    else:
        Text.tag_add("i", SEL_FIRST, SEL_LAST)
        Text.tag_config("i", font=("Georgia", "12", "italic"))

def removetags():
    for tag in Text.tag_names():
        Text.tag_delete(tag)
       
       
# Screen
       
root = Tk()
root.title("Python Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=500, height=500)

Text = Text(root, width=400, height=400)
Text.pack()


# Menu
menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New",  activebackground="sky blue", activeforeground="black", command=newfile)
filemenu.add_command(label="Open",  activebackground="sky blue", activeforeground="black", command=openfile)
filemenu.add_command(label="Save",  activebackground="sky blue", activeforeground="black", command=savefile)
filemenu.add_command(label="Save as",  activebackground="sky blue", activeforeground="black", command=saveas)
filemenu.add_separator()
filemenu.add_command(label="Quit",  activebackground="sky blue", activeforeground="black", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

stylemenu = Menu(menubar)
stylemenu.add_command(label="Bold",  activebackground="yellow", activeforeground="black", command=bold)
stylemenu.add_command(label="Underline",  activebackground="yellow", activeforeground="black", command=underline)
stylemenu.add_command(label="Italic",  activebackground="yellow", activeforeground="black", command=italic)
stylemenu.add_separator()
stylemenu.add_command(label="Remove all",  activebackground="yellow", activeforeground="black", command=removetags)
menubar.add_cascade(label="Style", menu=stylemenu)

root.config(menu=menubar)

root.mainloop()
