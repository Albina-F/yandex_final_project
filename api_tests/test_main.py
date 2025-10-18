import pytest
import data
from sender_stand_request import post_new_order, get_order


def test_get_order_status():
    response_create = post_new_order(data.order_body)
    track = response_create.json().get("track")
    response_get = get_order(track)
    assert response_get.status_code == 200
