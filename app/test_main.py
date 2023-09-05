from fastapi.testclient import TestClient

from app.main import app, current_datetime

client = TestClient(app)


def test_ping_request():
    request_data = {
        'message_type': 'TYPE_PING',
        'time': current_datetime,
    }
    response_data = {
        'version': 'v0.1',
        'name': 'chat2desk',
        'time': current_datetime,
    }

    response = client.post(f'/ozon', json=request_data)
    assert response.status_code == 200
    assert response.json() == response_data


def test_new_msg_request():
    request_data = [
        {
            'message_type': 'TYPE_NEW_MESSAGE',
            'chat_id': 'b646d975-0c9c-4872-9f41-8b1e57181063',
            'chat_type': 'Buyer_Seller',
            'message_id': '3000000000817031942',
            'created_at': '2022-07-18T20:58:04.528Z',
            'user': {'id': '115568', 'type': 'Сustomer'},
            'data': ['Текст сообщения'],
            'seller_id': '7',
        },
        {
            'message_type': 'TYPE_MESSAGE_READ',
            'chat_id': 'b646d975-0c9c-4872-9f41-8b1e57181063',
            'chat_type': 'Buyer_Seller',
            'message_id': '3000000000817031942',
            'created_at': '2022-07-18T20:58:04.528Z',
            'user': {'id': '115568', 'type': 'Сustomer'},
            'last_read_message_id': '3000000000817031942',
            'seller_id': '7',
        },
    ]
    response_data = {'result': True}

    for data in request_data:
        response = client.post(f'/ozon', json=data)
        assert response.status_code == 200
        assert response.json() == response_data
