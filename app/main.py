from sanic import Sanic
from sanic.response import json


app = Sanic("payment-api")



@app.get("/")
async def index(request):
    return json({
        "message": "message"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, dev=True)