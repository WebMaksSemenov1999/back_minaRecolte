from sql_fun.index import snaql_factory
users_inset_admin = snaql_factory.load_queries('users/users_inset_admin.sql').users_inset_user_admin
users_inset_user = snaql_factory.load_queries('users/users_inset_user.sql').users_inset_user
users_select_all = snaql_factory.load_queries('users/users_select_all.sql').users_select_all
