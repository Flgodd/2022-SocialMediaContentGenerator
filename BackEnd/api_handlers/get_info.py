from typing import Optional, Awaitable

import tornado.web

from information_provider import InformationProvider


class GetInfo(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        self.information_provider: InformationProvider = None
        super().__init__(application, request, **kwargs)

    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Content-type', 'application/json')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Allow-Headers', 'Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def initialize(self, information_provider: InformationProvider):
        self.information_provider = information_provider

    def get(self):
        self.write(self.information_provider.get_info())
