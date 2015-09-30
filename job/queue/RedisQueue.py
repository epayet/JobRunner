import redis


class RedisQueue:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis = redis.StrictRedis(host=host, port=port, db=db)
        self.jobQueueKey = "jobQueue"
        pass

    def push(self, data):
        self.redis.lpush(self.jobQueueKey, data)

    def get_nb_data(self):
        return self.redis.llen(self.jobQueueKey)

    def clear_queue(self):
        self.redis.delete(self.jobQueueKey)

    def pop(self):
        return eval(self.redis.lpop(self.jobQueueKey))
