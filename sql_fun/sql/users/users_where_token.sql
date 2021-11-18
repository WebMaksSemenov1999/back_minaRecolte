-- параметры sql
-- token

{% sql 'users_where_token', note='получить пользователя по токену' %}
SELECT users.id, fio, nik, email, avatar, is_active, is_admin, is_user, token.token, token.active, token.date
	FROM public.users
	LEFT JOIN "users_token" ON "users"."id" = "users_token"."id_users"
	LEFT JOIN "token" ON "token"."id" = "users_token"."id_token"
	WHERE token.token = {{ token | guards.string }}

{% endsql %}

