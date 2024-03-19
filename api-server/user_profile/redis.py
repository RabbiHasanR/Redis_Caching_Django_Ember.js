import redis
import os
# from dotenv import load_dotenv

# load_dotenv()

class RedisManager:
    def __init__(self, host=os.environ.get('REDIS_HOST'), port=os.environ.get('REDIS_PORT'), password=os.environ.get('REDIS_PASSWORD'), db=0):
        self.host = host
        self.port = port
        self.password = password
        self.db = db
        self.redis_client = redis.Redis(host=self.host, port=self.port, password=password, db=self.db)

    def set_redis_cache(self, key, value, expiry=None):
        self.redis_client.set(key, value, ex=expiry)

    def get_redis_cache(self, key):
        return self.redis_client.get(key)

    def delete_redis_cache(self, key):
        self.redis_client.delete(key)

    # def publish_redis(self, channel, message):
    #     return self.redis_client.publish(channel, message)


# Example usage:
# redis_manager = RedisManager()

# Set a key-value pair
# redis_manager.set_redis_cache('my_key', 'my_value', expiry=3600)

# Get the value associated with a key
# value = redis_manager.get_redis_cache('my_key')
# print(value.decode() if value else "Key not found")  # Decoding bytes to string

# Delete a key
# redis_manager.delete_redis_cache('my_key')

# Publish a message to a Redis channel
# num_subscribers = redis_manager.publish_redis('my_channel', 'Hello, subscribers!')
# print(f"{num_subscribers} subscribers received the message.")
