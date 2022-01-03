from data_access import *
import tkinter as tk
from tkinter import *
import webbrowser
from presenter import *
from tkinter import ttk

root = tk.Tk()
root.title('PutMeOn')


main_frame = tk.Frame(root)
main_frame.pack(fill=BOTH, expand=1)

canvas = tk.Canvas(main_frame, bg='black')
canvas.pack(side=LEFT, fill=BOTH, expand=1)

scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion= canvas.bbox("all")))

aux_frame = tk.Frame(canvas, bg='black')

canvas.create_window((0, 1000), window=aux_frame, anchor='n')

def get_recs():
    recs = get_recommendations(get_recc_data())
    recs = sorted(recs, key=itemgetter(1))

    for track in recs:
        unique_label(track[0], track[2])

def unique_label(text, url):
    label = tk.Label(aux_frame, text=text + '.mp3', bg='black', fg="green", cursor="hand2")
    label.bind("<Button-1>", lambda e: callback(url))
    label.pack()

openFile = tk.Button(root, text="Put Me On", padx=20, pady=10, fg='green', bg='black', command=get_recs)
openFile.pack()


root.mainloop()


# if __name__ == '__main__':
#     top = get_recc_data()
#     get_recommendations(top)
