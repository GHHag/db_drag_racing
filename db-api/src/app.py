from flask import Flask, request, jsonify
from clients.redis_client import RedisClient


app = Flask(__name__)
client = RedisClient()


@app.route("/redis/hget", methods=["GET"])
def hget_endpoint():
    """
    Endpoint for Redis HGET
    Usage:
        localhost:8080/redis/hget?hash=<some hash>&key=<some key>
    """
    try:
        # Parse path params
        hash = request.args.get("hash")
        key = request.args.get("key")
        print(f"The request is: hash={hash}, key={key}")

        # Send request to Redis
        (status, response) = client.hget(hash, key)

        # Respond
        return (
            jsonify(response),
            status,
        )

    except Exception as err:
        print(f"Error occured : {err}")
        return (
            500,
            jsonify(
                {
                    "status": "Error",
                    "message": "Something went wrong - check logs!",
                }
            ),
        )


@app.route("/redis/hset", methods=["POST"])
def hset_endpoint():
    """
    Endpoint for Redis HSET
    Usage:
        localhost:8080/redis/hset?hash=<some hash>&key=<some key>&value=<some value>
    """
    try:
        # Parse path params
        hash = request.args.get("hash")
        key = request.args.get("key")
        value = request.args.get("value")
        print(f"The request is: hash={hash}, key={key}, value={value}")

        # Send request to Redis
        (status, response) = client.hset(hash, key, value)

        # Respond
        return (
            jsonify(response),
            status,
        )

    except Exception as err:
        print(f"Error occured : {err}")
        return (
            500,
            jsonify(
                {
                    "status": "Error",
                    "message": "Something went wrong - check logs!",
                }
            ),
        )


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
