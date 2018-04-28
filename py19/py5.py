'''
polymorphism:poly(means)+phism(form)
if something exists in many form, it wis called polymorphism.
if a method or object performs many tasks, then it is called polymorphism.
'''
'''
duck typing: calling a function without knowing its class.
'''
class duck:
    def talk(self):
        print('Quack Quack!')
class dog:
    def talk(self):
        print('Bow Bow!')
def call_talk(obj):
    obj.talk()  #duck typink
d=duck()
call_talk(d)
d=dog()
call_talk(d)    #polymorphism
