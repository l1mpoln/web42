#!/usr/bin/python3

import datetime
import sys

response_body = "<html><head></head><body><h1>" + datetime.datetime.strftime(datetime.datetime.now(), "%H:%M:%S") + "</h1></body></html>"

# Длина ответа
content_length = len(response_body)

print("HTTP/1.1 201 OK")
print("Content-Type: text/html")
print("Content-Length:", content_length)
print()  # Пустая строка, разделяющая заголовки и тело ответа
print(response_body)

# Закрываем стандартный вывод, чтобы веб-сервер понял, что ответ завершен
sys.stdout.close()