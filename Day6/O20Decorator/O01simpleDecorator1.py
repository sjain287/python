# normal callback
def logInfo(fn):  # HoF or First Class Function
    print("logging started")
    fn()  # callback
    print("logging completed")


def do_Job():
    print("Job Done")


def do_db_job():
    print("DB JOB COMPLETED")


logInfo(do_Job)
logInfo(do_db_job)
