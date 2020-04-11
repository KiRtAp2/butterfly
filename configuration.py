import importlib

from settings import settings


dim = [
    0,  # minx
    0,  # maxx
    0,  # miny
    0  # maxy
]


def debug(*args):
    pass


def get_start_points(*args):
    pass


def do_physics(*args):
    pass


def additional_draw(*args):
    pass


def init(module_name):
    module = importlib.import_module(f"configs.{module_name}")

    global debug, get_start_points, do_physics, additional_draw
    debug = module.debug
    get_start_points = module.get_start_points
    do_physics = module.do_physics
    additional_draw = module.additional_draw
    settings.set_dim(module.dim)
