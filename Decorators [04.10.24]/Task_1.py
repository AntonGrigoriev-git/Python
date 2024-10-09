"""A decorator for checking access rights."""


def requires_permission(permission):
    def decor(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) if permission == "admin" else "Access denied!"
        return wrapper
    return decor


@requires_permission("user")
def delete_user(user_id):
    return f"User {user_id} deleted."

print(delete_user("Tom"))


@requires_permission("admin")
def delete_user(user_id):
    return f"User {user_id} deleted."

print(delete_user("Tom"))