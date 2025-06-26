
class LokiClient:

    def __init__(self, url: str = "http://localhost:3100"):
        self.url = url

    def push_log(self, labels: dict, message: str):
        pass


class DriverLogger:

    def __init__(self, driver_name: str, labels: dict, nats_conn):
        self.driver_name = driver_name
        self.labels = labels
        self.nats_conn = nats_conn
        self.loki_client = LokiClient()

    def log(self, labels: dict, message: str):
        pass
