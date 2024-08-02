def div(a,b):
    print(a/b)
def decorators(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
    return inner
div=decorators(div)
div(2,4)
