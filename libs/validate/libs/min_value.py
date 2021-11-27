from libs.validate.libs.errors_create_array import errors_create_array


def min_value(data, schema, elem, errors):
    if len(data[elem]) < schema['value']:
        errors_create_array(errors, elem)
        errors[elem].append(schema['errors'])
