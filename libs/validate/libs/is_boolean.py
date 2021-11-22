from libs.validate.libs.errors_create_array import errors_create_array


def is_boolean(data, schema, elem, errors):
    if data[elem] != 'true' and data[elem] != 'false':
        errors_create_array(errors, elem)
        errors[elem].append(schema['errors'])
