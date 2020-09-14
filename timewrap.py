import time

def cal_time(func):
    def wrapper(*args,**kwargs):
        t1=time.time()
        res=func(*args,**kwargs)
        t2=time.time()
        print(f'"{func.__name__}" 运行时间：{t2-t1}')
        return res
    return wrapper