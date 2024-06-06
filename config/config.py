import os
import yaml


def config_loader():
    with open('config/config.yaml') as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
    return cfg
