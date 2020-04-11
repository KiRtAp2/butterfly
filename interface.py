import pygame

from settings import settings
import colors
import configuration
import trace


window = None
background = None


def init():
    global window, background
    pygame.init()
    window = pygame.display.set_mode((settings.wwidth, settings.wheight))
    background = pygame.Surface((settings.wwidth, settings.wheight))
    background.fill(colors.BACKGROUND)


def translate(x, y):
    # translate coordinates x, y to pixel positions
    dim = settings.dim
    dx = settings.wwidth * (x-dim[0]) / (dim[1]-dim[0])
    dy = settings.wheight * (y-dim[2]) / (dim[3]-dim[2])
    return int(dx), int(dy)


def redraw(points):
    window.fill(colors.BACKGROUND)
    window.blit(background, (0, 0))

    for p in points:
        pygame.draw.circle(
            window,
            p.color,
            translate(*p.pos.tup()),
            p.radius
        )

    configuration.additional_draw(window, points, translate)

    pygame.display.update()


def draw_traces(points):

    for p in points:
        if p.do_trace:
            if p.last_trace is None:
                p.last_trace = trace.TracePoint(p)
            else:
                px, py = p.last_trace.x, p.last_trace.y
                pygame.draw.line(
                    background,
                    p.last_trace.color,
                    translate(px, py),
                    translate(*p.pos.tup())
                )
                p.last_trace = trace.TracePoint(p)
