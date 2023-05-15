import redis


# Service Layer -  business logic.
# WHAT are we saving in the redis instance.
class RedisClient:
    def __init__(self):
        # Setup
        self.redis_client = redis.StrictRedis(host="localhost", port="6379")

    def hget(self, hash: str, key: str):
        """
        Sending HGET operation to Redis
        """
        print(f"Lookup in Redis for hash = {hash} and key = {key}")
        if not hash or not key:
            return (
                500,
                f"'hash' and 'key' must have values. Values were hash={hash}, key={key}",
            )

        try:
            result = self.redis_client.hget(hash, key)
            if result:
                output_value = result.decode("utf-8").upper()
                return (200, {"message": output_value})

            else:
                return (
                    404,
                    {
                        "mesage": f"No data found. Result was: {result}, type: {type(result)}"
                    },
                )

        except Exception as err:
            trace_payload = {"hash": hash, "key": key}
            print(trace_payload, err, "RedisClient.hget")

            return (500, {"message": "Error - see prints"})

    def hset(self, hash: str, key: str, value: str):
        """
        Sending HSET operation to Redis
        """
        print(f"Writing to Redis hash={hash}, key={key} and value={value}")
        if not hash or not key or not value:
            return (
                500,
                f"'hash', 'key' and 'value' must have values. Values were hash={hash}, key={key}, value={value}",
            )

        try:
            self.redis_client.hset(hash, key, value)
            return (200, {"message": "OK"})

        except Exception as err:
            trace_payload = {"hash": hash, "key": key, "value": value}
            print(trace_payload, err, "RedisClient.hset")

            return (500, {"message": "Error - see prints"})

    def hdel(self, hash: str, key: str):
        """
        Sending HSET operation to Redis
        """
        print(f"Writing to Redis hash={hash}, key={key}")
        if not hash or not key:
            return (
                500,
                f"'hash', 'key' and 'value' must have values. Values were hash={hash}, key={key}",
            )

        try:
            self.redis_client.hdel(hash, key)
            return (200, {"message": "OK"})

        except Exception as err:
            trace_payload = {"hash": hash, "key": key}
            print(trace_payload, err, "RedisClient.hdel")

            return (500, {"message": "Error - see prints"})
