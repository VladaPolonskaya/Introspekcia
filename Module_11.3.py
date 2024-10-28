def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    module = obj.__class__.__module__
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module}

    return info

number_info = introspection_info(42)
print(number_info)

string_info = introspection_info('Stroka')
print(string_info)

list_info = introspection_info([5, 10, 2.0, 'Urban'])
print(list_info)