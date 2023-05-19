"""Main entrypoint for the cron module."""
from cron import log_config


logger = log_config.get_logger(__name__)


def main() -> None:
    """Main method."""
    logger.info("Cron template operational.")


if __name__ == "__main__":
    main()