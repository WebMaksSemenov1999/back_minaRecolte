from flask import jsonify


def request_set(request, name, params_object):
    if name in request:
        params_object[name] = request[name]


def request_set_array(request, name_array, params_object):
    for name in name_array:
        request_set(request, name, params_object)


def request_sort_set_array(request, name_array_column, name_array_query, params_object):
    index = -1
    for name in name_array_query:
        index = index + 1
        if name in request:
            params_object[name_array_column[index]] = request[name]


def request_json(data):
    json = {}
    for k, v in data:
        json[k] = v
    return json


def request_json_params(request):
    return request_json(request.args.items())


def request_json_body(request):
    data = request.get_json()
    return data


