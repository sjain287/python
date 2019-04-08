# normal callback
def logInfo(city, author):  # HoF or First Class Function
    def wrap_log_outside(fn):
        def wrap_log(*args):
            print(f"logging started @ {city} for {author} **{fn.__name__}**")
            print(sum(args))
            fn(*args)  # callback
            print("logging completed")
        return wrap_log
    return wrap_log_outside


@logInfo("KGF", "Taylor")
def do_Job(x, y):
    print("Job Done")


@logInfo("Ayodhya", "SriRam")
def do_db_job():
    print("DB JOB COMPLETED")


# do_Job = logInfo(do_Job)     # we can give any name
# f2 = logInfo(do_db_job)

do_Job(20, 30)
do_db_job()
