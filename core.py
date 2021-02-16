from PIL import Image
import PIL
import os
import glob
import pathlib
import math



def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])
def CompressSingle(directory=False,filename='', quality=30,file_size=0,com_ratio=None,com_btn=None):
    picture = Image.open(directory+ filename)
    if os.path.exists(os.path.join(directory,'Compressed')) == False:
        new_path = os.path.join(directory,'Compressed')
        os.mkdir(new_path)
    picture.save( directory +"/Compressed/Compressed_"+ filename[1:] ,optimize=True,quality=30)
    for item in pathlib.Path(os.path.join(directory,'Compressed')).iterdir():
        new_size = os.path.getsize(item)
    com_btn.config(text='Compressed Size: '+convert_size(new_size),font=("Courier", 10))
    temp_ratio = (file_size - new_size) / file_size
    com_ratio.config(text='Ratio: +' + str(temp_ratio*100) + '%')
    

def CompressDir(directory=False, quality=30,file_size=0,com_btn=None,com_ratio=None):
    if directory:
        os.chdir(directory)

    files = os.listdir()

    images = [file for file in files if file.endswith(('jpg', 'png'))]

    for image in images:
        print(image)

        img = Image.open(image)

        if os.path.exists(os.path.join(directory,'Compressed')) == False:
            new_path = os.path.join(directory,'Compressed')
            os.mkdir(new_path)

        img.save( "Compressed/Compressed_"+image, optimize=True, quality=quality)
        new_size= 0
        for item in pathlib.Path(os.path.join(directory,'Compressed')).iterdir():
            new_size += os.path.getsize(item)
        com_btn.config(text='Compressed Size: '+convert_size(new_size),font=("Courier", 10))
        temp_ratio = (file_size - new_size) / file_size
        com_ratio.config(text='Ratio: +' + str(temp_ratio*100) + '%')
        