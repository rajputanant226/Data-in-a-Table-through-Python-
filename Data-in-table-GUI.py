import tkinter as tk
from tkinter import ttk
data_coluns=[" ID "," Name "," Age "," Address "]
sample_data=[
    (101,"Anshul",20,"Narwar"),
    (102,"Ankit",23,"Sagar"),
    (103,"Anant",21,"Kareli"),
    (104,"Anshuman",22,"Patna"),
    (105,"Anshuman Rai",20,"Itarsi"),
    (106,"Adarsh",22,"Patna"),
    (107,"Aniket jain",21,"Ashok Nagar"),
    (108,"Aditya",22,"Khandwa"),
]
def create_table_gui():
    root=tk.Tk()
    root.title("Data Table using TreeView")
    root.geometry("800x300")
    tree=ttk.Treeview(root,columns=data_coluns,show='headings',height=10)
    for col in data_coluns:
        tree.column(col,anchor=tk.CENTER,width=120)
        tree.heading(col,text=col)
    
    for item in sample_data:
        tree.insert('',tk.END,values=item)
    
    tree.grid(row=0,column=0,sticky='nsew',padx=10,pady=10)
    root.mainloop()

if __name__=='__main__':
    create_table_gui()