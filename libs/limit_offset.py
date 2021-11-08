def limit_and_offset(request):
    limit = 20
    offset = 0
    if request['limit'] is not None:
        if int(request['limit']) < limit:
            limit = request['limit']
    if request['offset'] is not None:
        offset = request['offset']
    return str(limit), str(offset)
