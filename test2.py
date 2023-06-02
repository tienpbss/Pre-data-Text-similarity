

import fitz
import os
import shutil

path = 'D:\\Document-CSDLDPT'
path1 = 'D:\\Study\\Visual Studio Code\\Find Document\\documents'

file1 = 'The Art Market 2018.pdf'
file2 = 'The arts.pdf'

src = os.path.join(path, file1)
des = file2

file_name = os.path.basename(src)

def copy(src, des):
    '''copy file from src to des'''
    try:
        shutil.copy(src, des)
        print(f'copied {src} to {des}')

    except shutil.SameFileError:
        print("Source and destination represents the same file.")
    except PermissionError:
        print("Permission denied.")
    except:
        print("Error occurred while copying file.")

def getFirstPage(pathFile):
    doc = fitz.open(pathFile)
    text1 = doc[0].get_text() 
    doc.close()
    return text1  

check = []

#get all text of first page of each document to check
for file in os.listdir(path):
    f = os.path.join(path, file)
    text1 = getFirstPage(f)
    check.append(text1)

listSrcFile = os.listdir(path1)

count = 0
for i in range(0, len(listSrcFile)):
    file = listSrcFile[i]
    f = os.path.join(path1, file)
    doc = fitz.open(f)
    pageNums = len(doc)
    text = doc[0].get_text()
    if 20<=pageNums and not(text in check) :
        src = f
        des = os.path.join(path, file)
        copy(src, des)
        count+=1
    doc.close()

print('copied', count)