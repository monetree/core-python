#multiple inheritance
class father:
    def height(self):
        print('height=6.0f')
class mother:
    def color(self):
        print('color= tan')
class child(father,mother):
    pass
ch=child()
ch.height()
ch.color()

