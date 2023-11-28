import pypdf as pf
import docx2txt as dtt

import os
 
 
dir_path = ".\Data\\"
string = "den"

 
def main():
 
    clear_output_file()
    read_directory(dir_path, string)
    print("Done")
 
 

def clear_output_file():
    with open ("output.txt", "w") as f:
        f.write("")
 


def read_directory(path, substring):
    files_dir = os.listdir(path)
   
    for file in files_dir:
        filepath = path + file

        if ".pdf" in file:  
            read_pdf(filepath, substring)
            
        elif ".docx" in file: 
            read_docx(filepath, substring)
        
        elif ".txt" in file: 
            read_txt(filepath, substring)
        
        else: 
            print(f"We don't support the filetype of '{file}'  yet\n")
            continue

 
        
def read_pdf(path, substring, maxpages=100):
    file = pf.PdfReader(path)
    num_pages = len(file.pages)
    if num_pages < maxpages:

        print(f"Searching {num_pages} pages for: '{substring}' in {path} \n")

        for i in range(num_pages):
            page = file.pages[i]
            text = page.extract_text()
            
            if substring.lower() in text.lower():
                with open ("output.txt", "a") as f:
                    f.write(f"Hittat '{substring}' på sida {i}, i fil: {path}\n")


 
def read_docx(path, substring):
    # path = (".\Testfiles\\NCvar selector.docx")
    text = dtt.process(path)

    print(f"Searching for: '{substring}' in {path} \n")

    if substring.lower() in text.lower():
        with open ("output.txt", "a") as file:
            file.write(f"Hittat '{substring}' i fil: {path}\n")


    



def read_txt(path, substring):
    ''''''


# def find_substring(i, text, substring):
#     if substring.lower() in text.lower():
#             with open ("output.txt", "a") as file:
#                 file.write(f"Sida {i}, i fil: {file}\n")


 
 
 
if __name__ == "__main__":
    main()