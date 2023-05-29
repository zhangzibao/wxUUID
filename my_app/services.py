from my_app.WXAPI import WXAPI
from my_tools.RedisTool import RedisTool


def getUUID(token, WxData, WechatVersion=None, DeviceVersion=None, XmlData=None):
    redis = RedisTool()
    if not IsExistsUser(token):
        return {
            "success": False,
            "data": None,
            "message": "密钥无效"
        }
    cnt = int(redis.redis_conn.hget(token, "cnt"))  # 剩余次数
    if cnt <= 0:
        return {
            "success": False,
            "data": None,
            "message": "剩余次数已经用完"
        }
    if not WxData:
        return {
            "success": False,
            "data": None,
            "message": "a16/62数据不允许为空"
        }
    uuid = WXAPI.getUUID(WxData, WechatVersion, DeviceVersion, XmlData)
    if not uuid:
        return {
            "success": False,
            "data": None,
            "message": "获取uuid失败，此次调用不消耗次数"
        }
    else:
        redis.redis_conn.hincrby(token, "cnt", -1)  # 剩余次数
        cnt = int(redis.redis_conn.hget(token, "cnt"))  # 剩余次数
        return {
            "success": True,
            "data": uuid,
            "cnt": cnt,
            "message": ""
        }


def addUser(token=None, cnt=0):
    # 添加用户
    redis = RedisTool()
    if IsExistsUser(token):
        post_cnt = redis.redis_conn.hget(token, "cnt")

        return {
            "success": False,
            "message": f"该用户已存在：{token}  剩余次数：  {post_cnt}"
        }
    redis.redis_conn.hset(token, "cnt", cnt)  # 剩余次数
    return {
        "success": True,
        "message": f"添加成功{token}  剩余次数  {cnt}"
    }


def IsExistsUser(token):
    return RedisTool().redis_conn.hexists(token, 'cnt')  # 剩余次数


def delUser(token):
    # 删除用户
    redis = RedisTool()
    redis.redis_conn.delete(token)  # 剩余次数
    return {
        "success": True,
        "message": f"删除成功：{token}"
    }


def addCnt(token, cnt=0):
    # 增加调用次数
    redis = RedisTool()
    if not IsExistsUser(token):
        return {
            "success": False,
            "message": f"该用户不存在：{token}"
        }

    for_cnt = redis.redis_conn.hget(token, "cnt")

    redis.redis_conn.hincrby(token, "cnt", cnt)  # 剩余次数
    post_cnt = redis.redis_conn.hget(token, "cnt")

    return {
        "success": True,
        "message": f"{token}成功添加次数：{cnt}  添加之前:{for_cnt}   添加之后:  {post_cnt} "
    }


def readCnt(token):
    # 读取剩余调用次数
    redis = RedisTool()
    if not IsExistsUser(token):
        return {
            "success": False,
            "message": f"该用户不存在：{token}"
        }

    for_cnt = redis.redis_conn.hget(token, "cnt")

    return {
        "success": True,
        "cnt": for_cnt,
    }
