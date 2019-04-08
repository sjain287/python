# normal callback
def logInfo(fn):  # HoF or First Class Function
    def wrap_log():
        print("logging started")
        fn()  # callback
        print("logging completed")
    return wrap_log


@logInfo
def do_Job():
    print("Job Done")


@logInfo
def do_db_job():
    print("DB JOB COMPLETED")


# do_Job = logInfo(do_Job)     # we can give any name
# f2 = logInfo(do_db_job)

do_Job()
do_db_job()
