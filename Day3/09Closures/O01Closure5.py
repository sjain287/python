def log_detail(func):  # receives functions as input. It is a higher order function
    def log(*nums):
        res = func(*nums)
        print(f"Logging for {func.__name__},*nums")
        return res
    return log


def sum(x, y):
    return x+y


def diff(x, y):
    return x - y


log_sum = log_detail(sum)
print(log_sum(10, 20))

log_diff = log_detail(diff)
print(log_diff(10, 20))
