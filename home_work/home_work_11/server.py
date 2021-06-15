import datetime
import socket
import sys
from logging import getLogger, StreamHandler

logger = getLogger(__name__)
stdout_handler = StreamHandler(sys.stdout)
logger.addHandler(stdout_handler)
logger.setLevel("DEBUG")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 10002))
sock.listen(socket.SOMAXCONN)

conn, addr = sock.accept()
conn.settimeout(5)

with conn, sock:
    while True:
        received_data = conn.recv(1024)
        if received_data == b'':
            break
            #когда прилетает пустая строка, выход программы. Можно через continue для пропуска если данные не прийшли
        with open('doc_server.txt', 'a', encoding='utf-8') as f:
            print(f'Время: {datetime.datetime.now()}. Записанные данные: {received_data.decode("utf-8")}', file=f)
            logger.info(f'I am received: {received_data}')
