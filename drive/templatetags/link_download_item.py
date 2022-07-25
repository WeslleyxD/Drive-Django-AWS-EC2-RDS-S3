from django import template
from s3.requests import list_all_items_by_user, storage, link_open_item, link_download_item

register = template.Library()

@register.inclusion_tag('dashboard_items.html')
def items(user):
    all_items = list_all_items_by_user(user)
    link_item_download = []
    for item in all_items:
        url_open = link_open_item(key=f'{user}/{item}')
        url_download = link_download_item(key=f'{user}/{item}')
        link_item_download.append({'url_open':url_open, 'item':item, 'url_download':url_download})
    return {'attributes' : link_item_download}

@register.inclusion_tag('dashboard_percent.html')
def percent(user):
    percent_storage = storage(user)
    return {'percent_storage' : percent_storage}

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
