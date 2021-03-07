import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
import argparse
import csv

import interface
import configuration
from settings import settings


def main():

    running = True
    paused = False
    clock = pygame.time.Clock()

    points = configuration.get_start_points()

    TRACEEVENT = pygame.USEREVENT+1
    pygame.time.set_timer(TRACEEVENT, settings.trace_time)
    DEBUGEVENT = pygame.USEREVENT+2
    if settings.debug:
        pygame.time.set_timer(DEBUGEVENT, settings.debug_time)

    t = 0

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

            if e.type == DEBUGEVENT and not paused:
                configuration.debug(points)

            if e.type == TRACEEVENT and not paused and t > 1000:
                interface.draw_traces(points)

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    paused = not paused

        dt = clock.tick(60)
        if not paused:
            t += dt
            configuration.do_physics(dt, points)
        interface.redraw(points)


def run_sim(time):

    points = configuration.get_start_points()

    with open("headless.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Time"] + points[0].description())

        for t in range(time):
            dt = 1
            configuration.do_physics(dt, points)

            if settings.debug and t % settings.debug_time == 0:
                configuration.debug(points)

                data = []
                for p in points:
                    if p.export:
                        data.append([t] + p.compress())
                writer.writerows(data)

        data = []
        for p in points:
            if p.export:
                data.append([time-1] + p.compress())

        writer.writerows(data)

    print("Generated file headless.csv")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Chaotic system simulator")
    parser.add_argument("--headless", dest="headless", action="store_const", default=False, const=True, help="Run in headless mode")
    parser.add_argument("--time", type=int, default=1000, help="Set time for headless mode. Default 1000")
    parser.add_argument("--module", default="double_pendulum", help="Choose module to load. Default double_pendulum")
    args = parser.parse_args()

    configuration.init(args.module)

    if args.headless:
        run_sim(args.time)
        quit()

    interface.init()
    main()
