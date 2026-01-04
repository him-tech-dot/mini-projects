import os

def arrange_files(files,ext):
    files_with_ext = [file for file in files if file.endswith(ext)]
    print(files_with_ext)
    
    # if not(os.path.exists("images")):
    #     os.mkdir("images")
    # i=1
    # for file in files_with_ext:
    #     os.rename(file,f"images/pic-{i}{ext}")
    #     i+=1

    if not(os.path.exists("images")):
        os.mkdir("images")
    for i,file in enumerate(files_with_ext,start=1):
        os.rename(file,f"images/photo-{i}{ext}")   

if __name__=="__main__":
    
    files = os.listdir()
    arrange_files(files,".jpg")

    print(__name__)
