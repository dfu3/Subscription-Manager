
from datetime import datetime
from flask import abort

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def remove_sub_by_id(subscription_id):
    if subscription_id in SUBSCRIPTIONS:
        del SUBSCRIPTIONS[subscription_id]


def update_existing_sub(
        subscription_id,
        industry,
        source=None,
        category=None,
        ):
    if subscription_id in SUBSCRIPTIONS:
        SUBSCRIPTIONS[subscription_id] = {
        "industry": industry,
        "source": source if source else SUBSCRIPTIONS[subscription_id]["source"],
        "category": category if category else SUBSCRIPTIONS[subscription_id]["category"],
        "user_id": SUBSCRIPTIONS[subscription_id]["user_id"],
        "created_at": SUBSCRIPTIONS[subscription_id]["created_at"],
        "updated_at": get_timestamp(),
    }
    else:
        abort(
            404, f"Subscription with id {subscription_id} not found"
        )

def add_new_sub(
        user_id,
        subscription_id,
        industry,
        source=None,
        category=None,
        ):
    SUBSCRIPTIONS[subscription_id] = {
        "industry": industry,
        "source": source,
        "category": category,
        "user_id": user_id,
        "created_at": get_timestamp(),
        "updated_at": get_timestamp(),
    }
    return {subscription_id: SUBSCRIPTIONS[subscription_id]}

def update_active_sub(user_id):
    next_sub_id = len(SUBSCRIPTIONS) + 1
    if user_id in USERS:
        USERS[user_id]["subscription_id"] = next_sub_id
    else:
        abort(
            404, f"User with id {user_id} not found"
        )
    return next_sub_id

def find_active_sub_by_user(user_id):
    if user_id in USERS:
        sub_id = USERS[user_id]["subscription_id"]
        return find_sub_by_id(sub_id)
    else:
        abort(
            404, f"User with id {user_id} not found"
        )

def find_subs_by_user(user_id):
    user_subs = {}
    if user_id in USERS:
        for k, v in SUBSCRIPTIONS.items():
            if v["user_id"] == user_id:
                user_subs[k] = v
        return user_subs
    else:
        abort(
            404, f"User with id {user_id} not found"
        )

def find_sub_by_id(subscription_id):
    if subscription_id in SUBSCRIPTIONS:
        return {subscription_id: SUBSCRIPTIONS[subscription_id]}
    else:
        abort(
            404, f"Subscription with id {subscription_id} not found"
        )

def find_user_by_id(user_id):
    if user_id in USERS:
        return USERS[user_id]
    else:
        abort(
            404, f"User with id {user_id} not found"
        )

def get_all_users():
    return USERS

def set_active_sub(user_id, subscription_id):
    USER = find_user_by_id(user_id)
    if subscription_id is None:
        USER["subscription_id"] = None  # deactivate current subscription
    else:
        SUB = find_sub_by_id(subscription_id)[subscription_id]
        if SUB["user_id"] == user_id:
            USER["subscription_id"] = subscription_id
        else:
            abort(
                400, f"User does not have subscription with id {subscription_id}"
            )


USERS = {
    1: {
        "f_name": "Horace",
        "l_name": "Mann",
        "subscription_id": 2,  # represents "active" sub
    },

    2: {
        "f_name": "Test",
        "l_name": "Testerson ",
        "subscription_id": 1,
    }
}

SUBSCRIPTIONS = {
    1: {
        "industry": "Consumer Health",
        "source": "Social Media",
        "category": "New Product Releases",
        "user_id": 2,
        "created_at": get_timestamp(),
        "updated_at": get_timestamp(),
    },
    2: {
        "industry": "Beauty",
        "source": "Social Media",
        "category": "Mergers and Acquisitions",
        "user_id": 1,
        "created_at": get_timestamp(),
        "updated_at": get_timestamp(),
    },
    3: {
        "industry": "Tech",
        "source": "News ",
        "category": "Mergers and Acquisitions",
        "user_id": 2,
        "created_at": get_timestamp(),
        "updated_at": get_timestamp(),
    }
}