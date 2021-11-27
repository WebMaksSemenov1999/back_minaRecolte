from libs.validate.libs.errors_create_array import errors_create_array


def boolean_number(data, schema, elem, errors):
    if not data[elem] == "0" and not data[elem] == "1":
        errors_create_array(errors, elem)
        errors[elem].append(schema['errors'])
