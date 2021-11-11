from libs.validate.errors_create_array import errors_create_array
from libs.validate.is_object import is_object


def is_required(data, schema, elem, errors):
    if is_object(data, elem):
        errors_create_array(errors, elem)
        errors[elem].append(schema['errors'])
    elif data[elem] == "" or data[elem] is None or data[elem] == 0:
        errors_create_array(errors, elem)
        errors[elem].append(schema['errors'])
