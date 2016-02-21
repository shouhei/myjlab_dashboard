class BaseConfig:
    _websocket_protocol = "ws://"
    _http_protocol = "http://"
    _endpoint = ""
    _port = ":8888"

    @classmethod
    def http_endpoint(cls):
        return cls._http_protocol + cls._endpoint + cls._port

    @classmethod
    def websocket_endpoint(cls):
        return cls._websocket_protocol + cls._endpoint + cls._port

class DevelopConfig(BaseConfig):
    _endpoint = "localhost"

class VagrantConfig(BaseConfig):
    _endpoint = "192.168.33.100"
    _port = ":80"
