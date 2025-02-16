import redis
import json
import pickle

from src import settings
from src.models import Singleton


class DataAdapter(metaclass=Singleton):
    def __init__(self):
        self.client = redis.StrictRedis.from_url(settings.REDIS_ENDPOINT)

    def set(self, key, value, expire=None, serialize=True):
        """Store data in Redis with optional expiration time."""
        if serialize:
            value = json.dumps(value)  # Convert complex data to JSON
        self.client.set(key, value, ex=expire)

    def get(self, key, deserialize=True):
        """Retrieve data from Redis."""
        value = self.client.get(key)
        if value and deserialize:
            try:
                return json.loads(value)  # Convert JSON back to Python object
            except json.JSONDecodeError:
                return value
        return value

    def delete(self, key):
        """Delete a key from Redis."""
        self.client.delete(key)

    def exists(self, key):
        """Check if a key exists in Redis."""
        return self.client.exists(key) > 0

    def expire(self, key, seconds):
        """Set expiration time for a key."""
        self.client.expire(key, seconds)

    def set_pickle(self, key, value, expire=None):
        """Store complex Python objects using Pickle."""
        self.client.set(key, pickle.dumps(value), ex=expire)

    def get_pickle(self, key):
        """Retrieve complex Python objects stored with Pickle."""
        value = self.client.get(key)
        return pickle.loads(value) if value else None
