def add(request):
    print(request.path)
    return {
        'path': request.path,
    }
