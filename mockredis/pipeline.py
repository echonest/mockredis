from mockredis.redis import MockRedis


class MockRedisPipeline(MockRedis):
    """
    Imitate a redis-python pipeline object
    so unit tests can run without needing a
    real Redis server.
    """

    def __init__(self, redis, timeouts):
        """Initialize the object."""
        self.redis = redis
        self.timeouts = timeouts
        self.buffered_results = []

    def execute(self):
        """
        Emulate the execute method. Return the 
        buffered results and clear the instance copy.
        """ 
        rval = self.buffered_results
        self.buffered_results = []
        return rval

    def _buffer_results(self, val):
        self.buffered_results.append(val)
        return None

    def __exit__(self, *argv, **kwargs):
        self.buffered_results = []

    def __enter__(self, *argv, **kwargs):
        return self
