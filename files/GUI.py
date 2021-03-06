import tkinter, files
from operator import attrgetter


class GUI:
    def __init__(self,diary):
        self.diary=diary
        self.root = tkinter.Tk()
        self.root.geometry("800x600")
        self.b1 = tkinter.Button(text="Добавить задание", command=self.add_task)
        self.b1.place(relx=0, rely=0,relwidth=0.33)
        # self.b2 = tkinter.Button(text="Получить задание", command="")
        # self.b2.place(relx=0.25, rely=0,relwidth=0.25)
        self.b3 = tkinter.Button(text="Удалить задание по инд", command=self.del_by_index)
        self.b3.place(relx=0.33, rely=0, relwidth=0.33)
        self.b4 = tkinter.Button(text="Удалить выбранное задание", command=self.del_active)
        self.b4.place(relx=0.66, rely=0, relwidth=0.33)
        self.entry=tkinter.Entry()
        self.entry.place(relx=0.4,rely=0.1,relwidth=0.2)
        self.butSort=tkinter.Button(text="сорт возр",command=self.sort)
        self.butSort.place(relx=0.4, rely=0.2, relwidth=0.1)
        self.butSort2 = tkinter.Button(text="сорт убыв", command=self.sort2)
        self.butSort2.place(relx=0.5, rely=0.2, relwidth=0.1)
        self.butDone = tkinter.Button(text="выполнено/не выполнено", command=self.make_completed)
        self.butDone.place(relx=0.4, rely=0.3, relwidth=0.2)
        self.lb = tkinter.Listbox(self.root,selectbackground="RED")
        self.lb.place(relx=0.4, rely=0.4, relwidth=0.2)
        self.fill_list_box()

    def add_task(self):
        te=self.entry.get()
        self.diary.addtask(te)
        self.fill_list_box()
        self.entry.delete(0, tkinter.END)

    def fill_list_box(self):
        self.lb.delete(0, tkinter.END)
        for task in self.diary.tasks:
            if task.completed == "False":
                self.lb.insert(tkinter.END, task.task+" X")
            else:
                self.lb.insert(tkinter.END, task.task + " V")



    def del_by_index(self):
        ind=int(self.entry.get())
        self.diary.delete_task_by_index(ind)
        self.fill_list_box()
    def del_active(self):

        task=self.lb.get("active")
        self.diary.delete_task_by_task(task)
        self.fill_list_box()

    def make_completed(self):

        task = self.lb.get("active")
        self.diary.make_completed_task(task)
        self.fill_list_box()



    def sort(self):
        self.diary.tasks.sort(key=attrgetter("task"))
        self.fill_list_box()
    def sort2(self):
        self.diary.tasks.sort(key=attrgetter("task"))
        self.diary.tasks=self.diary.tasks[::-1]
        self.fill_list_box()

yiii=GUI(files.Diary("ege.txt"))



yiii.root.mainloop()
