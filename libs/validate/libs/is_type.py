from libs.validate.libs.errors_create_array import errors_create_array


def is_type(data, schema, elem, errors):
    if not isinstance(data[elem], schema['value']):
        errors_create_array(errors, elem)
        errors[elem].append(schema['errors'])
        return True
    return False