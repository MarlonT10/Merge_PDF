from PyPDF2 import PdfMerger
import shutil
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk
import os
from sys import platform
root = tk.Tk()
root.title('PDF Editor')
root.geometry('800x600')
pdfs = []

def add_pdf():
    test = "Y"
    while test == "Y":
        root.filename = filedialog.askopenfilename(title = "Select a File",filetypes=(("PDF Files","*.pdf"),))
        original_path = root.filename
        current_dir = os.getcwd()
        print("Current directory" + current_dir)
        shutil.copy(original_path,current_dir)
        print("File Copied")
        pdf_name = os.path.split(root.filename)[1]
    
        if platform == "win32":
            destination_dir = current_dir + "\\" + pdf_name
        elif platform == "darwin":
            destination_dir = current_dir + "/" + pdf_name
        global pdfs
        pdfs.append(destination_dir)
        test = input("Add More PDfs? If yes, enter Y.")
    merger = PdfMerger()
    for pdf in pdfs:
        merger.append(pdf)
    resultname = input("Enter Result name: ")
    merger.write(resultname + ".pdf")
    merger.close()

    destination2 = filedialog.askdirectory()
    if platform == "win32":
        result = current_dir + "\\" + resultname + ".pdf"
    elif platform == "darwin":
        destination_dir = current_dir + "/" + resultname + ".pdf"
    shutil.copy(result,destination2)




button = tk.Button(root,text = "Open File", command = add_pdf).pack()
root.mainloop()