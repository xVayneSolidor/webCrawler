import threading
from queue import Queue
from spider import Spider
from domain import *
from utils import *
import socket

PROJECT_NAME = 'crawlResults'
HOMEPAGE = 'https://www.pucmm.edu.do/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/urlpool.txt'
CRAWLED_FILE = PROJECT_NAME + '/results.txt'
NUMBER_OF_THREADS = 5
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

#Se crean los threads para los workders
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

#Se realiza el siguiente trabajo en la cola
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

#Cada URL es un nuevo trabajo
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

#Verifica que si hay links en la cola, se revisen
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' URLs en la cola')
        create_jobs()

create_workers()
crawl()