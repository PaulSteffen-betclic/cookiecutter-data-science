# -*- coding: utf-8 -*-
import os
import hydra

from dotenv import find_dotenv, load_dotenv
from loguru import logger
from omegaconf import DictConfig
from utils import configure_logger, CONFIG_NAME, CONFIG_PATH

@logger.catch
@hydra.main(version_base=None, config_path=CONFIG_PATH, config_name=CONFIG_NAME)
def main(cfg: DictConfig):
    pass

if __name__ == "__main__":
    configure_logger()

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv(), override=True)
    secrets_path = os.path.join(os.getcwd(), ".secrets")
    load_dotenv(secrets_path, override=True)

    main()
  
