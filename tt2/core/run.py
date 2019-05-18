"""
run.py

Main entry point into bot script. Ensuring that the directory is
manually added to the system path so all modules are able to be imported.
"""
import argparse

from os import sys, getcwd
sys.path.append("\\".join(getcwd().split("\\")[:-2]))

if __name__ == '__main__':
    # Begin argument setup/build.
    parser = argparse.ArgumentParser()
    parser.add_argument("-start", action="store_true", default=False, help="Initialize a new bot instance and begin automation. (Ensure that the bot screen is open and at the top-left most portion of the screen).")
    parser.add_argument("-parse_artifacts", action="store_true", default=False, help="Parse artifacts in game. May take up to two minutes. Check your stats file afterwards to view the results.")
    parser.add_argument("-parse_clan", action="store_true", default=False, help="Parse clan statistics in game.")

    arguments = parser.parse_args()
    if arguments.start:
        from tt2.core.bot import Bot
        Bot().run()
    elif arguments.parse_artifacts:
        from tt2.tools.parse_artifacts import parse_artifacts
        parse_artifacts()
    elif arguments.parse_clan:
        from tt2.tools.parse_clan import parse_clan
        parse_clan()
    else:
        parser.print_help()
