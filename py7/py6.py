#we can return one function from another function

def display(str):
    def message():
        return 'hello'
    return message()+str
x=display(' krish')
print(x)

