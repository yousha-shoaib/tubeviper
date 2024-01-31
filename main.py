import tkinter as tk
import customtkinter as ctk
from pytube import YouTube as yt
from threading import Thread as th

# Download function
def startDownload():
    try: 
        ytLink = link.get()
        ytObject = yt(ytLink, on_progress_callback=onProgress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finshLabel.configure(text="")

        video.download()

        finshLabel.configure(text="Downloaded", text_color="green")
    except:
        finshLabel.configure(text="Download error", text_color="red")

def onProgress(stream , chunk, btyes_remaining):
    total_size = stream.filesize
    btyes_downloaded = total_size - btyes_remaining
    percentage_completion = (btyes_downloaded / total_size) * 100
    per = str(int(percentage_completion))
    progPercent.configure(text=per + '%')
    progPercent.update()
    progressBar.set(float(percentage_completion / 100))

def init_download():
    t = th(target=startDownload, daemon=True)
    t.start()

# Sytstem settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

# Define app frame
app = ctk.CTk()
app.geometry("720x480")
app.title("Youtube Downlaoder")

# Adding UI elements
title = ctk.CTkLabel(app, text="insert a youtube link")
title.pack(padx=10, pady=10)

# Link input
url_var = tk.StringVar()
link = ctk.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finsihed downloading
finshLabel = ctk.CTkLabel(app, text="")
finshLabel.pack()

# Progress percentage
progPercent = ctk.CTkLabel(app, text="0%")
progPercent.pack()

progressBar = ctk.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download button
download = ctk.CTkButton(app, text="Download", command=init_download)
download.pack(padx=20, pady=10)

# Run app
app.mainloop()
