class TimeCalculation:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args):
        print("Time started")
        self.fn(*args)
        print("Time completed")
        print("*"*50)


@TimeCalculation
def do_Job():
    print("Job Done")


@TimeCalculation
def do_db_job():
    print("DB JOB COMPLETED")


do_Job()
do_db_job()
