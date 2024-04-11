import os
import sys
import tarfile
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from omegaconf import OmegaConf, DictConfig

from loguru import logger

ASCII_LOGO = """"""

logger_format: str = (
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | {elapsed} | "
    "<level>{level}</level> | "
    "<cyan>{file}</cyan>:<cyan>{function}</cyan> | "
    "<level>{message}</level>"
)

LOG_CONF: dict = {
    "format": logger_format,
    "level": "INFO",
    "colorize": True,
    "backtrace": True,
    "diagnose": True,
}

DATE_FORMAT: str = "%Y-%m-%d"
CONFIG_PATH: str = "../../conf"
CONFIG_NAME: str = "config"


def update_config(cfg: DictConfig, env_variables: dict) -> None:
    for k in cfg.keys():
        if OmegaConf.is_missing(cfg, k):
            OmegaConf.update(cfg, k, env_variables.get(k))
        if OmegaConf.is_config(cfg[k]):
            update_config(cfg[k], env_variables)


def configure_logger() -> None:
    filename = os.path.basename(sys.argv[0]).split(".py")[0]
    logger.remove()
    logger.add(sys.stderr, **LOG_CONF)
    logger.add(
        f"{Path(__file__).parents[1]}/logs/{filename}.log",
        retention="1 days",
        **LOG_CONF,
    )


def find_filename(dir: Path, filename: str) -> Path:
    if isinstance(dir, str):
        dir = Path(dir)
    for path in dir.glob("**"):
        if (path / filename).exists():
            return path / filename


def load_env_variables(secrets: bool = True) -> None:
    load_dotenv(find_dotenv(), override=True)
    if secrets:
        secrets_path = os.path.join(os.getenv("PWD"), ".secrets")
        load_dotenv(secrets_path, override=True)

@logger.catch
def untar_models():
    """
    Untar models from /opt/ml/processing/models and organize them by date in /opt/ml/processing/output/models/{date}/
    This is only executed on sagemaker
    """
    for file in Path("/opt/ml/processing/models").glob("*.tar.gz"):
        logger.info(f"Extracting {file} ...")
        file = tarfile.open(file)
        # extracting file
        for z in file.getnames():
            file_week = z.split(".")[0][-10:]
            logger.info(f"Extracting {z} to {file_week}/")
            file.extract(z, path=f"/opt/ml/processing/output/models/{file_week}/")
        file.close()

        return