import inspect

class Info_obj:

    def __init__(self):
        self.attribute_1 = None

    def introspection_info(self, obj):
        self.obj = obj
        attributes = inspect.getmembers(Info_obj, lambda attr: not(inspect.isroutine(attr)))
        print(attributes)
number_info = Info_obj()
number_info.introspection_info(42)
print(number_info)
