import os
import json
from flask import Flask, request, jsonify
from clients.redis_client import RedisClient
from clients.bigtable_client import BigtableClient

# Configuration for Bigtable client
os.environ["BIGTABLE_EMULATOR_HOST"] = "localhost:8086"
os.environ["BIGTABLE_PROJECT_ID"] = "project_id"
os.environ["BIGTABLE_INSTANCE_ID"] = "instance_id"

app = Flask(__name__)
client = RedisClient()
bigtable_client = BigtableClient(
    "project_id", "instance_id", "table_id"
)  # these are the names u enter in the extension!


# Router & Controller handles everything related to HTTP requests
# REDIS Routes: GET, POST, DELETE
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


@app.route("/redis/hdel", methods=["DELETE"])
def hdel_endpoint():
    """
    Endpoint for Redis HDEL
    Usage:
        localhost:8080/redis/hset?hash=<some hash>&key=<some key>
    """
    try:
        # Parse path params
        hash = request.args.get("hash")
        key = request.args.get("key")
        print(f"The request is: hash={hash}, key={key}")

        # Send request to Redis
        (status, response) = client.hdel(hash, key)

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


# BIGTABLE Routes: POST, READ, DELETE
# Router & Controller handles everything related to HTTP requests


@app.route("/bigtable/write", methods=["POST"])
def write_endpoint():
    """
    Endpoint for Bigtable write
    Usage:
        localhost:8080/bigtable/write?kind=<some_data_kind>
    """
    try:
        # Parse path params
        kind = request.args.get("kind")
        # Parse request body
        request_body = request.get_json()

        # Write data to Bigtable
        bigtable_client.write_row(kind, request_body)

        # Return success response
        return (
            jsonify({"status": "success", "message": "Data written to Bigtable"}),
            200,
        )

    except Exception as err:
        # Return error response
        print(f"Error occurred : {err}")
        return (
            jsonify(
                {"status": "Error", "message": "Something went wrong - check logs!"}
            ),
            500,
        )


@app.route("/bigtable/read", methods=["GET"])
def read_endpoint():
    """
    Endpoint for Bigtable read using GET request
    Usage:
        localhost:8080/bigtable/read?row_key=<key>&row_id=<id>
    """
    try:
        # Get key from request query parameters
        row_key = request.args.get("row_key")
        row_id = request.args.get("row_id")
        # Read data from Bigtable
        data = bigtable_client.get_row(f"{row_key}#{row_id}")

        # Return success
        return (
            str(data),
            200,
        )
    except Exception as err:
        # Return error response
        print(f"Error occurred : {err}")
        return (
            jsonify(
                {"status": "Error", "message": "Something went wrong - check logs!"}
            ),
            500,
        )


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
