# users.py

from data_store import ( 
     get_all_users,
     find_user_by_id,
     set_active_sub,
)


def patch(user_id, body):
    return set_active_sub(user_id, body.get("subscription_id")), 204

def get_one(user_id):
    return find_user_by_id(user_id)

def get_all():
    return get_all_users()