import signal
import sys

from app import create_app, cleanup
from app.models_manager import models_manager
from app.log import log

app = create_app()
models_manager.load_models()

def signal_handler(sig, freame):
    log("Get signal")
    cleanup()
    log("Clean done, app close successfully")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=False)

