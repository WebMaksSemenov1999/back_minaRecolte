def limit_and_offset(request):
    limit = 20
    offset = 0
    if request.args.get('limit') is not None:
        print('is not None')
        if int(request.args.get('limit')) < limit:
            limit = request.args.get('limit')
    if request.args.get('offset') is not None:
        offset = request.args.get('offset')
    return str(limit), str(offset)
