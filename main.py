from pytube import YouTube
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *


def startDownloadThreadV():
    thread = Thread(target=startVDownload)
    thread.start()

def startDownloadThreadA():
    thread = Thread(target=startADownload)
    thread.start()

# starting GUI building
main = Tk()

main.title("Daksh's Youtube downloader")

# set the icon
main.iconbitmap('download.ico')
main.geometry("500x300")

#use PhotoImage class to store the photo
photo = PhotoImage(file='download.png')
headingIcon = Label(main, image=photo)
headingIcon.pack(side=TOP)

#url text field
label = Label(main, text='Enter URL', font=("verdana", 15))
label.pack(pady=10)

urlField = Entry(main, font=("verdana", 18), justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=20)

def startVDownload():
    try:
        url = urlField.get()

        path_to_save_video = askdirectory()
        if path_to_save_video is None:
            return
        # creating youtube object with url..
        ob = YouTube(url)

        Vstrm = ob.streams.get_highest_resolution()
        vTitle.config(text=Vstrm.title)
        vTitle.pack(side=BOTTOM)
        Vstrm.download(path_to_save_video)
        print("done")

        showinfo("Download finished", "Downlaoded successfully")
        urlField.delete(0, END)
        vTitle.pack_forget()

    except Exception as e:
        print(e)
        print('error')

def startADownload():
    try:
        url = urlField.get()

        path_to_save_video = askdirectory()
        if path_to_save_video is None:
            return
        # creating youtube object with url..
        ob = YouTube(url)

        Vstrm = ob.streams.get_highest_resolution()
        vTitle.config(text=Vstrm.title)
        vTitle.pack(side=BOTTOM)

        astrm = ob.streams.last()
        astrm.download(path_to_save_video)
        print("done")

        showinfo("Download finished", "Downlaoded successfully")
        urlField.delete(0, END)
        vTitle.pack_forget()

    except Exception as e:
        print(e)
        print('error')


#Video download button
Button(main, text="Download Video", font=("verdana", 8), command=startDownloadThreadV).place(x=135, y=190)
#Audio download button
Button(main, text="Download Audio", font=("verdana", 8), command=startDownloadThreadA).place(x=255, y=190)

vTitle = Label(main,text='video title')

main.mainloop()