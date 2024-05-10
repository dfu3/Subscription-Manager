# subscriptions.py

from data_store import (
    find_subs_by_user,
    find_sub_by_id,
    find_active_sub_by_user,
    update_active_sub,
    add_new_sub,
    update_existing_sub,
    remove_sub_by_id,
)

def create(user_id, subscription):
    next_sub_id = update_active_sub(user_id)
    return add_new_sub(
        user_id=user_id,
        industry=subscription.get("industry"),
        source=subscription.get("source"),
        category=subscription.get("category"),
    ), 201

def update(subscription_id, subscription):
    return update_existing_sub(
        subscription_id=subscription_id,
        industry=subscription.get("industry"),
        source=subscription.get("source"),
        category=subscription.get("category"),
    ), 204

def delete(subscription_id):
    return remove_sub_by_id(subscription_id), 204

def get_one(subscription_id):
    return find_sub_by_id(subscription_id), 200

def get_active(user_id):
    return find_active_sub_by_user(user_id), 200

def get_all(user_id):
    return find_subs_by_user(user_id), 200