"""
Module for testing config module.
"""
import pytest
from unittest_example.config import Config, ConfigData

MOCK_CONFIG_DATA_DICT = {"name": "myconfig"}


class TestConfig:
    """TestConfig test class"""

    def test_config_data(self):
        """Test ConfigData dataclass"""
        config_data = ConfigData(**MOCK_CONFIG_DATA_DICT)
        config_data.name == "myconfig"
