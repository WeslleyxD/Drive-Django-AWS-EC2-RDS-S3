from django import template
from s3.requests import list_all_items_by_user, storage, download_item_user

register = template.Library()

@register.inclusion_tag('dashboard_items.html')
def items(user):
    all_items = list_all_items_by_user(user)
    links = {}
    for item in all_items:
        generate_url_item = download_item_user(key=f'{user}/{item}')
        links[item] = generate_url_item
    return {'links' : links}

@register.inclusion_tag('dashboard_percent.html')
def percent(user):
    percent_storage = storage(user)
    return {'percent_storage' : percent_storage}




