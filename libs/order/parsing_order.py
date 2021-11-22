def parsing_order(obj):
    string_order = ""
    for key in obj:
        if obj[key] == 'true':
            string_order += key + ' DESC,'
        if not obj[key] == 'false':
            string_order += key + ' ASC,'

    return string_order[0:-1]
