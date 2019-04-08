import datetime


class TimeCalculation:
    def __init__(self, author, creation):
        self.author = author
        self.creation = creation

    def __call__(self, fn):
        def wrap_fun(*args):
            print(f"Time started for {fn.__name__} written by {self.author}")
            fn(*args)
            print("Time completed")
            print("*" * 50)
        return wrap_fun


@TimeCalculation("ELizabeth", "12th aug 1994")
def do_Job(x, y):
    print(f"Job Done {x},{y}")


@TimeCalculation("Kalam", "12th aug 1994")
def do_db_job():
    print("DB JOB COMPLETED")


do_Job(20, 30)
do_db_job()
