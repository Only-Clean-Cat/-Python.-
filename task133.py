import requests
import logging
from requests.exceptions import ConnectionError, ConnectTimeout, ReadTimeout
logger = logging.getLogger('RequestsLogger')



sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com',
         'https://tiktok.com', 'https://www.ozon.ru']


logger.setLevel(logging.INFO)

# Создание файловых handlers для каждого типа логов
success_handler = logging.FileHandler('success_responses.log', 'w')
success_handler.setLevel(logging.INFO)
success_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))

bad_handler = logging.FileHandler('bad_responses.log', 'w')
bad_handler.setLevel(logging.WARNING)
bad_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))

blocked_handler = logging.FileHandler('blocked_responses.log', 'w')
blocked_handler.setLevel(logging.ERROR)
blocked_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))

# Добавление handlers к логгеру
# logger.addHandler(success_handler)
# logger.addHandler(bad_handler)
# logger.addHandler(blocked_handler)

for site in sites:
    try:
        # Отправка запроса
        response = requests.get(site, timeout=3)
        site_cod = response.status_code
        print(site_cod)

        # Проверка статуса ответа
        if int(site_cod) == 200:
            logger.addHandler(success_handler)
            logger.info(f"{site}, response - {response.status_code}")
        if int(site_cod) != 200:
            logger.addHandler(bad_handler)
            logger.warning(f"{site}, response - {response.status_code}")
    except Exception as e:
        logger.addHandler(blocked_handler)
        logger.error(f"{site}, {type(e)}")

