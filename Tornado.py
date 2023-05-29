# run.py
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from my_app.dns_app import app
from loguru import logger

if __name__ == '__main__':
    logger.info("启动flask进程")
    http_server = HTTPServer(WSGIContainer(app))
    http_server.bind(10011)
    http_server.start(num_processes=4)
    IOLoop.instance().start()
