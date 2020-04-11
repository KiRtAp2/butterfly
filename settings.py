import json


class Settings:
    def __init__(self, data: dict):
        self.wwidth = data["wwidth"]
        self.wheight = data["wheight"]
        self.debug = data["debug"]
        self.debug_time = data["debug_time"]
        self.trace_time = data["trace_time"]

    def set_dim(self, dim):
        self.dim = dim


with open("settings.json") as f:
    settings = Settings(json.load(f))
