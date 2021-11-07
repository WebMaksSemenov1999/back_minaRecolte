def request_set(request, name, params_object):
    if request.args.get(name) is not None:
        params_object[name] = request.args.get(name)


def request_set_array(request, name_array, params_object):
    for name in name_array:
        request_set(request, name, params_object)


def request_sort_set_array(request, name_array_column, name_array_query, params_object):
    index = -1
    for name in name_array_query:
        index = index + 1
        if request.args.get(name) is not None:
            params_object[name_array_column[index]] = request.args.get(name)
