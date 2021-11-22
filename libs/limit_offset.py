def limit_and_offset(request):
    limit = 20
    offset = 0
    if "limit" in request:
        if int(request['limit']) < limit:
            limit = request['limit']
    if "offset" in request:
        offset = request['offset']
    return str(limit), str(offset)
