from tkinter import messagebox


def ErrorPath(path):
    messagebox.showerror('error', 'Папки не существуют: %s'%path)

def ErrorData():
    messagebox.showerror('error', 'Данные еще не были загружены')
    
def Info():
    return messagebox.askyesno('warning',"Вы точно хотите удалить данные")

def ErrorDataProcces():
    messagebox.showwarning('warning','Введется работа с данными очистка невозможна')

def ErrorButtonPuskProcces():
    messagebox.showwarning('error','Невозможно запустить загрузку данных, выполняется систематизация')

def ErrorButtonCreateProcces():
    messagebox.showwarning('error','Невозможно запустить систематизацию, выполняется загрузка данных')

def ErrorOpenFileDoc(path):
    messagebox.showwarning('error','не закрыт файл: %s'%path)