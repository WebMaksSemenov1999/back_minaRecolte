def limitAndOffset(request):
    limit = 20
    offset = 0
    if request.args.get('limit') is not None and int(request.args.get('limit')) < limit:
        limit = request.args.get('limit')
    if request.args.get('offset') is not None:
        offset = request.args.get('offset')
    return limit, offset
