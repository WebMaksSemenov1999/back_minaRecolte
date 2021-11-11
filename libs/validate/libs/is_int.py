from libs.validate.libs.errors_create_array import errors_create_array


def is_int(data, schema, elem, errors):
    if data[elem].isdigit():
        errors_create_array(errors, elem)
        errors[elem].append(schema['errors'])
