import pickle, os
class Task:
    def __init__(self, task, completed=False):
        self.task = task
        self.completed = completed

    def __str__(self):
        return f"задача: {self.task} завершенность:{self.completed}"


class Diary:
    def __init__(self, path):
        self.path = path
        self.tasks = []
        if os.path.getsize(path)>0:
            f = open(path, "rb")
            self.tasks=pickle.load(f)
            f.close()

    def gettasks(self):
        return self.tasks

    def addtask(self, task):
        self.tasks.append(Task(task))
        self.update_file()

    def update_file(self):
        f = open(self.path, "wb")
        pickle.dump(self.tasks,f)

    def obj_to_str(self,obj):
        return pickle.dumps(obj)

    def delete_task_by_index(self, index):
        self.tasks.pop(index)
        self.update_file()

    def delete_task_by_task(self, task):
        for i in range(len(self.tasks)):
            if self.tasks[i].task==task[0:-2]:
                self.tasks.pop(i)
                return
        self.update_file()

    def make_completed_task(self, task):
        for i in range(len(self.tasks)):
            if self.tasks[i].task == task[0:-2] and self.tasks[i].completed is False:
                self.tasks[i].completed = True
                return
            elif self.tasks[i].task == task[0:-2] and self.tasks[i].completed is True:
                self.tasks[i].completed = False
        self.update_file()

# s = Diary("ege.txt")
# # st=input("Задача:\n")
# # s.addtask(st)
# #
# # print(s.gettasks())
# #
# # # s.delete_task_by_index(3)
# # # print(s.gettasks())
# # #
# # # print(s.gettasks())
#
# for i in s.tasks:
#     print(i.completed)



