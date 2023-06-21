"""
Module for interfacing with this modules configuration.
Uses JSON format.
"""
import os
import json
from dataclasses import dataclass


class InvalidConfiguration(Exception):
    """Exception raised when invalid configuration is detected"""


@dataclass
class ConfigData:
    name: str
    description: str


class Config:
    """Config class"""

    def __init__(self, path: str) -> None:
        """
        Loads the configuration into its class instance variable.
        :param path: Path to the configuration file.
        """
        # Check for valid path
        if not os.path.exists(path=path):
            raise ValueError(f"Configuration file {path} was not found.")
        self.path = path
        self.config = self.get_config()

    def get_config(self) -> ConfigData:
        """
        Load configuration as dictionary

        :return: ConfigData
        """
        with open(self.path, "r") as config_file:
            try:
                json_config = json.loads(config_file)
            except json.JSONDecodeError as exc:
                raise InvalidConfiguration("Unable to decode configuration as JSON.")

        return ConfigData(**json_config)
