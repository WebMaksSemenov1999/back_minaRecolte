from libs.validate.libs.is_type import is_type
from libs.validate.libs.is_required import is_required
from libs.validate.libs.is_object import is_object
from libs.validate.libs.boolean_number import boolean_number
from libs.validate.libs.is_int import is_int
from libs.validate.libs.is_boolean import is_boolean
from libs.validate.libs.min_value import min_value
from flask import abort


def validate(data, schema):
    errors = {}
    for elem in schema:
        if 'is_option' in schema[elem]['regulations']:
            if is_object(data, elem):
                continue
        # обязательное поле
        if 'required' in schema[elem]['regulations']:
            is_required(data, schema[elem]['regulations']['required'], elem, errors)
            # проверка на существование логики и дальнейшней валидации
            if is_object(data, elem):
                return errors
        # проверка на тип переменной
        if 'type' in schema[elem]['regulations']:
            is_type(data, schema[elem]['regulations']['type'], elem, errors)
        # проверка на 1 или 0 в виде строки
        if 'boolean_number' in schema[elem]['regulations']:
            boolean_number(data, schema[elem]['regulations']['boolean_number'], elem, errors)
        if 'min_value' in schema[elem]['regulations']:
            min_value(data, schema[elem]['regulations']['is_int'], elem, errors)
        # проверка на целое число
        if 'is_int' in schema[elem]['regulations']:
            is_int(data, schema[elem]['regulations']['is_int'], elem, errors)
        # проверка на булевое значение из строки
        if 'is_boolean' in schema[elem]['regulations']:
            is_boolean(data, schema[elem]['regulations']['is_boolean'], elem, errors)
    if not len(errors.keys()) == 0:
        abort(400, errors)
