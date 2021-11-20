from libs.order.parsring_order import parsring_order
from libs.request_set import request_sort_set_array


def order_generation(request, params_sql, key, name_array_column, name_array_query):
    params_sort = {}
    request_sort_set_array(request, name_array_column, name_array_query, params_sort)
    order = parsring_order(params_sort)
    if order:
        params_sql[key] = parsring_order(params_sort)