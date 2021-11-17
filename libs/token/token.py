def token(request):
    authorization = request.headers.get('authorization')
    print(authorization)


def validate_admin(request):
    token(request)


def validate_users():
    pass
