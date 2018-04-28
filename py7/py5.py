#it is possible to define one function inside another function
#called nested function
# def display(str):
#     def message():
#         return 'hello'
#     return message()+str
# x=display(' krish')
# print(x)


def display(str):
    def message():
        return "hello"
    return message()+str
print(display('krish'))
