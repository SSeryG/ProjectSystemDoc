from tkinter import messagebox


def ErrorPath(path):
    messagebox.showerror('error', 'Папки не существуют: %s'%path)

def ErrorData():
    messagebox.showerror('error', 'Данные еще не были загружены')
    
def Info():
    return messagebox.askyesno('warning',"Вы точно хотите удалить данные")
