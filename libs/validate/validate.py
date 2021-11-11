from libs.validate.is_type import is_type
from libs.validate.is_required import is_required
from libs.validate.is_object import is_object
from libs.validate.boolean_string import boolean_string


def validate(data, schema):
    errors = {}
    for elem in schema:
        if 'is_option' in schema[elem]['regulations']:
            if is_object(data, elem):
                continue
        if 'required' in schema[elem]['regulations']:
            is_required(data, schema[elem]['regulations']['required'], elem, errors)
            # проверка на существование логики и дальнейшней валидации
            if is_object(data, elem):
                return errors
        if 'type' in schema[elem]['regulations']:
            is_type(data, schema[elem]['regulations']['type'], elem, errors)
        if 'boolean_string' in schema[elem]['regulations']:
            boolean_string(data, schema[elem]['regulations']['boolean_string'], elem, errors)
    return errors
