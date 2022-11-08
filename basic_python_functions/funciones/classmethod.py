#accede a la clase no la instancia

class TestClass:
    def regular_method(self):
        print (self)
    
    @classmethod
    def class_method(cls):
        #cls es la clase no la instancia
        print (cls)
        
    def __str__(self):
        return "TestClass Instance"

t = TestClass()
t.regular_method()
t.class_method() #llama a la clase, no la instancia <class '__main__.TestClass'>
TestClass.class_method() #llama a la clase, no la instancia <class '__main__.TestClass'>