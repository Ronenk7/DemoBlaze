import unittest
import json
import xml.etree.ElementTree as ET
from definitions import Definitions


class CommonOps(unittest.TestCase):

    CONFIG_XML_PATH = f"{Definitions.ROOT_DIR.value}/Configurations/DataConfig.xml"
    CONFIG_LOGIN_JSON_PATH = f"{Definitions.ROOT_DIR.value}/Configurations/config_login_tests.json"

    def get_data(self, node_name) -> str:
        """Read the XML config file and returns it as a parsed string."""
        root = ET.parse(self.CONFIG_XML_PATH).getroot()
        return root.find(".//" + node_name).text

    def config(self) -> dict:
        """Read the JSON config file and returns it as a parsed dict."""
        with open(self.CONFIG_LOGIN_JSON_PATH) as config_file:
            return json.load(config_file)
