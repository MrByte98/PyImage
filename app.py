import tkinter as tk
import tkinter.filedialog as fd
import os
import math
from core import CompressDir,CompressSingle
import pathlib



### init window
window = tk.Tk()
window.geometry('500x200')
window.resizable(0,0)
window.title('PyImage ver0.1 - Write by: MOhammad Isaac-Ahmadi')
window.config(background='black') 

Logo = tk.Label(window,text='PyImage',font=("Courier", 20),fg='green',bg='black')
Logo.place(x=195,y=5)



def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

 

src = ''
orginal_src = ''
_filename = ''
def ChooseImages():
    filez = fd.askopenfilenames(parent= window, title='Choose a Image/Images',filetypes =[('All Image Format',['*.jpg','*.png']),('Jpeg', '*.jpg'),('PNG','*.png')])
    size = 0
    single_file = False
    try:
        if filez[1] != None:
            src = str(filez[0])[:(str(filez[0]).rfind('/'))] + '/...' 
            orginal_src = str(filez[0])[:(str(filez[0]).rfind('/'))]
    except:
        src = str(filez[0])
        size = os.path.getsize(src)
        orginal_src = str(filez[0])[:(str(filez[0]).rfind('/'))]
        _filename = str(filez[0])[(str(filez[0]).rfind('/')):]
        single_file = True

    
    for ind,val in enumerate(filez):
        size += os.path.getsize(str(filez[ind]))

    location_text = tk.Message(window,text='Location: '+src,font=("Courier", 8),fg='green',bg='black')
    location_text.place(x=10,y=72)
    if single_file == False:
        file_size = tk.Label(window,text='Folder Size: '+convert_size(size),font=("Courier", 8),fg='green',bg='black')
    else:
        file_size = tk.Label(window,text='File Size: '+convert_size(size),font=("Courier", 8),fg='green',bg='black')
    file_size.place(x=195,y=72)

    compress_size=tk.Label(window,text=None,fg='green',bg='black')
    compress_ratio = tk.Label(window,text='',font=("Courier", 10),fg='green',bg='black')
    if single_file == False:
        
        compress_btn = tk.Button(window,text='Compress',command=lambda: CompressDir(directory=orginal_src,file_size=size,com_ratio=compress_ratio,com_btn=compress_size),font=("Courier", 10),fg='green',bg='black')
    else:

        compress_btn = tk.Button(window,text='Compress',command=lambda: CompressSingle(directory=orginal_src,filename=_filename,file_size=size,com_btn=compress_size,com_ratio=compress_ratio),font=("Courier", 10),fg='green',bg='black')

    compress_btn.place(x=195,y=100)
    compress_size.place(x=195,y=135)
    compress_ratio.place(x=195,y=155)
    tips = tk.Label(window,text="Warning: After click 'Compress', Wait for complete task.",font=("Courier", 10),fg='green',bg='black')
    tips.place(x=10,y=180)
    

        

select_addr = tk.Button(window,text='Choose images',command=ChooseImages,font=("Courier", 10),fg='green',bg='black')
select_addr.place(x=10,y=40)



# show compress size of image/all images




window.mainloop()