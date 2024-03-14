# Элина Романцова, 14-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request


# Тест для создания заказа и проверки успешности его создания
def test_create_order_and_retrieve_order_info():
    # Запрос на создание заказа
    create_order_response = sender_stand_request.post_new_order()

    # Проверить, что код ответа равен 201
    assert create_order_response.status_code == 201, "Не удалось создать заказ"

    # Получить трек номер заказа
    order_track = create_order_response.json().get("track")

    # Запрос на получение заказа по треку
    retrieve_order_response = sender_stand_request.get_order_by_track(order_track)

    # Проверить, что код ответа равен 200
    assert retrieve_order_response.status_code == 200, "Не удалось получить заказ"
