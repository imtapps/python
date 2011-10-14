def asdf(self):
    print type(self)
    print "I'm ALIVE!!!"

class YourMetaClass(type):

    def __new__(cls, name, bases, attrs):
        print "YourMetaClass %s" % name
        print "create %s" % name
        nt = type.__new__(cls, name, bases, attrs)
        nt.asdf = asdf
        return nt

def instance_method(self):
    print "I'm an instance method on %s" % self

class MyMetaClass(type):
    def __new__(cls, name, bases, attrs):
        print "MyMetaClass %s" % names
        v = type.__new__(cls, name, bases, attrs)
        v.setUp = None
        v.tearDown = None
        v.run = instance_method
        return v

def autopatch(something_to_patch):
    def wrap(cls):
        return MyMetaClass(cls.__name__, cls.__bases__, dict(cls.__dict__))
    return wrap

@autopatch("here is my thing")
class MyClassOne(object):
    __metaclass__ = YourMetaClass

    def here_i_am(self):
        print "I'm right here!"

class MyClassTwo(MyClassOne):
    pass


if __name__ == '__main__':
    mco = MyClassOne()
    #mco.asdf()
    mco.run()

    mct = MyClassTwo()
    mct.here_i_am()
    mct.run()


    import sys

    my_mod = sys.modules[__name__]

    print dir(my_mod)
