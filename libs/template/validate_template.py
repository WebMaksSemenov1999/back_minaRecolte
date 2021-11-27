is_option_type_str = {
    "regulations": {
        "is_option": True,
        "type": {
            "value": str,
            "errors": "данное поле является строкой",
        }
    },
}
required_params = {
    "required": {
        "errors": "данное поле является обязательным",
    }
}

is_option_type_boolean_number = {
    "regulations": {
        "is_option": True,
        "boolean_number": {
            "errors": "данное поле имеет значение 1 или 0",
        }
    },
}
limit_offset = {
    "regulations": {
        "is_option": True,
        "is_int": {
            "errors": "данное поле является целым числом",
        },
    },
}
params_order = {
    "regulations": {
        "is_option": True,
        "is_boolean": {
            "errors": "данное поле имеет значения true, false",
        },
    },
}