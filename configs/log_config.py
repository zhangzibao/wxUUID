from os import path

from loguru import logger

__all__ = [
    "logger",  # 配置日志
]

current_path = path.dirname(__file__)  # 当前文件的path
Environment = 1  # 0:测试环境；1：生产环境
logger.add(
    path.join(current_path, "../logs/debug.{time:MM-DD}.log"),
    level="DEBUG",
    encoding="utf-8",
    enqueue=True,
    # rotation="4h",
    retention="10 days",
    filter=lambda x: 'DEBUG' == x['level'].name
)

logger.add(
    path.join(current_path, "../logs/info.{time:MM-DD}.log"),
    level="INFO",
    encoding="utf-8",
    # rotation="4h",
    enqueue=True,
    retention="10 days",
    filter=lambda x: 'INFO' == x['level'].name
)

logger.add(
    path.join(current_path, "../logs/warning.{time:MM-DD}.log"),
    level="WARNING",
    encoding="utf-8",
    # rotation="4h",
    enqueue=True,
    retention="10 days",
    filter=lambda x: 'WARNING' == x['level'].name

)

if __name__ == "__main__":
    pass
