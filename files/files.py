class Diary:
    def __init__(self, path):
        self.path = path
        f = open(path, "r", encoding="UTF8")
        self.tasks = f.read().split("|")
        f.close()

    def gettasks(self):
        print("some")
        return self.tasks

    def addtask(self, task):
        self.tasks.append(task)
        self.update_file()
    def update_file(self):
        f = open(self.path, "w", encoding="utf8")
        f.write("|".join(self.tasks))
        f.close()
    def delete_task_by_index(self,index):
        self.tasks.pop(index)
        self.update_file()
    def delete_task_by_task(self,task):
        self.tasks.remove(task)
        self.update_file()

# s = Diary("ege.txt")
# # st=input("Задача:\n")
# # s.addtask(st)
# print(s.gettasks())
# # s.delete_task_by_index(3)
# # print(s.gettasks())
# s.delete_task_by_task("купить водку")
# print(s.gettasks())