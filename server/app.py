import tornado.web
import tornado.websocket
import tornado.httpserver
import os

cl = []

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        if self not in cl:
            cl.append(self)

    def on_message(self, message):
        for client in cl:
            client.write_message(message)

    def on_close(self):
        if self in cl:
            cl.remove(self)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/index.html")


settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "hoigadjfahidufawdfa",
    "xsrf_cookies": True,
}

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/websocket", WebSocketHandler)
        ], **settings)


def main():
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(8888)
    server.start(0)  # forks one process per cpu
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main();
