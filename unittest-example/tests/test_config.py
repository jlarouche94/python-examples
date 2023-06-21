"""
Module for testing config module.
This file serves as a guide on how to write unit tests and is meant to be verbose for this purpose.

Notable libraries:
- pytest: pytest provides better reporting compared to the built-in unit test module
          it allows us to create reusable fixtures, assert for exceptions raised.
          pytest also has various plugins for things such as coverage and mocking.
- unittest.mock: provides the default implementations and reduces the need for pytest-mock module
                 it works the same exact way.
"""
import pytest
from unittest.mock import patch
from unittest_example.config import Config, ConfigData

MOCK_CONFIG_DATA_DICT = {"name": "myconfig", "description": "my configuration"}
MOCK_CONFIG_DATA = ConfigData(**MOCK_CONFIG_DATA_DICT)

@pytest.fixture("")

class TestConfig:
    """TestConfig test class"""

    def test_config_data(self):
        """Test ConfigData dataclass"""
        config_data = ConfigData(**MOCK_CONFIG_DATA_DICT)
        assert config_data.name == "myconfig"
        assert config_data.description == "my configuration"

    def test_config_data_invalid(self):
        """Test ConfigData when invalid data is used to build the object"""
        with pytest.raises(TypeError):
            ConfigData(name="OnlyName")

    # This will mock a specific function
    # Here we mock the os.path.exists so that we don't need to rely on a file exisiting
    # We also mock get_config() so that we isolate our test to only the __init__ logic.
    @patch("os.path.exists", return_value=True)
    @patch("unittest_example.config.Config.get_config", return_value=MOCK_CONFIG_DATA)
    def test_config_init(self, mock_get_config, mock_path_exists):
        """Test Config class init"""
        config = Config(path="myconfig.json")

        # Here the MagicMock object is returned by the @patch decorator
        # Magic mocks allow us to do assertions on the object and how it as called.
        # This is perfect to use for ensuring the things you mock are being called properly.
        mock_get_config.assert_called_with()
        mock_path_exists.assert_called_with(path="myconfig.json")

    @patch("os.path.exists", return_value=False)
    def test_config_init_file_not_present(self, mock_path_exists):
        """Test Config class init when file doesn't exist."""
        with pytest.raises(ValueError):
            Config(path="myconfig2.json")

    @patch("os.path.exists", return_value=False)
    def test_get_config(self, mock_path_exists):
        """Test Config class init when file doesn't exist."""
        with pytest.raises(ValueError):
            Config(path="myconfig2.json")
