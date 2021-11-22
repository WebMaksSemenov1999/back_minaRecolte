from libs.order.parsing_order import parsing_order
from libs.request_set import request_sort_set_array


def order_generation(request, params_sql, key, name_array_column, name_array_query):
    params_sort = {}
    request_sort_set_array(request, name_array_column, name_array_query, params_sort)
    order = parsing_order(params_sort)
    if order:
        params_sql[key] = parsing_order(params_sort)