from my_tools.RedisTool import RedisTool

redis = RedisTool()
with open("./tokens") as f:
    lines = f.readlines()
    for l in lines:
        token = l.strip()
        print(token)
        # redis.redis_conn.hset(token, "cnt", 100)  # 剩余次数


        