# #another way
# def decor(fun):
#     def inner():
#         res=fun()
#         return res+2
#     return inner
# #this is another fun to which decor is applied
# @decor
# def num():
#     return 10
# print(num())

def decor(fun):
    def inner():
        res=fun()
        return res+2
    return inner
@decor
def num():
    return 10
print(num())