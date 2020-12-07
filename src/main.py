import socket

from fastapi import FastAPI

import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return {
        "lang": "python",
        "hostname": socket.gethostname()
    }


def start():
    uvicorn.run(app, host="0.0.0.0", port=3000)


if __name__ == "__main__":
    start()
