import logging
import logging_loki


def start_logging():
    logging_loki.emitter.LokiEmitter.level_tag = "level"

    # assign to a variable named handler
    handler = logging_loki.LokiHandler(
        # url="http://localhost:3100/loki/api/v1/push",
        # url="http://localhost:23100/loki/api/v1/push",
        url="localhost:23100/loki/api/v1/push",
        version="1",
    )
    # create a new logger instance, name it whatever you want
    logger = logging.getLogger("my-logger")

    logger.addHandler(handler)

    logger.error(
        "Something bad happened",

        extra={"tags": {"service": "my-service"}},
    )
    logger.warning(
        "Something bad happened but we can keep going",
        extra={"tags": {"service": "my-service"}},
    )


if __name__ == "__main__":
    start_logging()
