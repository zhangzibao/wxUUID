import redis

from configs.configs import redis_host, redis_password, db_index, redis_port


class RedisTool:
    def __init__(
            self,
            host=redis_host,
            port=redis_port,
            password=redis_password,
            db=db_index,
            decode_responses=True
    ):
        self.redis_pool = redis.ConnectionPool(host=host, port=port, password=password, db=db,
                                               decode_responses=decode_responses)
        self.redis_conn = redis.Redis(connection_pool=self.redis_pool, decode_responses=True)

    def get_new_name(self):
        last_name = self.index(0)
        new_name = int(last_name) + 1
        self.redis_conn.lpush("ImageList", new_name)  # 头插
        return str(new_name)

    def index(self, index):
        return self.redis_conn.lindex("ImageList", index)

    def __len__(self):
        return self.redis_conn.llen("ImageList")

    def empty(self):
        self.redis_conn.delete("ImageList")

    def __repr__(self):
        image_name_list = []
        for i in range(len(self)):
            image_name_list.append(self.index(i))
        return "-".join(image_name_list)

    def __del__(self):
        self.redis_pool.disconnect()


if __name__ == "__main__":
    db_tool = RedisTool()
    import json

    res = db_tool.redis_conn.get("valid-headers")
    print(json.loads(res))
