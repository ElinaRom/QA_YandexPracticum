import requests
import configuration
import data


def post_new_order():
    return requests.post(url=configuration.URL_SERVICE + configuration.ORDERS_PATH,
                         json=data.order_data,
                         headers=data.headers)


def get_order_by_track(track):
    return requests.get(url=f"{configuration.URL_SERVICE}{configuration.ORDERS_PATH}/track?t={track}")
