GET_NAME = "Привет! Как тебя зовут?"

GET_CONTACT_OR_USERNAME = "Отправь свой контакт или введи username:"

GET_PRODUCT = "Какой продукт вас интересует?"

GET_TIME = "Когда вам удобно созвониться?"

FINAL = "Спасибо! Мы скоро с вами свяжемся."

ADMIN_ERROR = "Это команда администратора"


def get_lead(lead):
    return f"""
Имя: {lead.name}
Контакты: {lead.contact}
Продукт: {lead.product}
Время: {lead.time}
    """