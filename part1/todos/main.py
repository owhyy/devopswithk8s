from bottle import run
import os

PORT = int(os.getenv("PORT", "8080"))

run(host="localhost", port=PORT)
