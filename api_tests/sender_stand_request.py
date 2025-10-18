import configuration
import requests
import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE+configuration.ORDER_CREATION,
                         json=body,
                         headers=data.headers)


response = post_new_order(data.order_body)
print(response.status_code)
assert response.status_code == 201
print(response.json().get("track"))
track = response.json().get("track")


def get_order(track):
    return requests.get(configuration.URL_SERVICE+configuration.RECEIVE_ORDER,
                        params={"t": track})


response = get_order(track)
print(response.status_code)
print(response.json().get("order", {}).get("id"))
