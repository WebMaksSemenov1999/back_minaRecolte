def request_set(request, name, params_object):
    if request.args.get(name) is not None:
        params_object[name] = request.args.get(name)


def request_set_array(request, name_array, params_object):
    for name in name_array:
        if request.args.get(name) is not None:
            params_object[name] = request.args.get(name)
