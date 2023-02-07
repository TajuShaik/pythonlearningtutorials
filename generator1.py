def func1():
    yield "python"
    yield "django"
    yield "Python"
    yield "developed"
    yield "by "
    yield "Gudo van rossum"
res=func1()
for i in range(6):
    print(next(res))
 
