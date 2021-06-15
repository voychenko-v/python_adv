import socket
import sys
from logging import getLogger, StreamHandler
from time import sleep

logger = getLogger(__name__)
stdout_handler = StreamHandler(sys.stdout)
logger.addHandler(stdout_handler)
logger.setLevel("DEBUG")


sock = socket.create_connection(('127.0.0.1', 10002), timeout=5)
sock.settimeout(2)

with sock:
    with open('doc_client.txt', 'r') as f:
        for line in f.readlines():
            data_four_sending = line.strip('\n').encode('utf-8')
            sock.sendall(data_four_sending)
            logger.info(f'I im send: {data_four_sending}')
            sleep(0.5)
