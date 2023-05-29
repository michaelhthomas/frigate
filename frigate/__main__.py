import faulthandler
import threading

from flask import cli

from frigate.app import FrigateApp
from frigate.server import ServerApp

faulthandler.enable()

threading.current_thread().name = "frigate"

cli.show_server_banner = lambda *x: None

if __name__ == "__main__":
    if "server" in sys.argv:
        frigate_app = ServerApp()
    else:
        frigate_app = FrigateApp()

    frigate_app.start()

