"""
Basic test file for configuration and environment variables.
"""

import unittest
import os

class TestConfig(unittest.TestCase):
    def test_env_variables_exist(self):
        # Check that required environment variables are defined
        required_vars = ["TELEGRAM_BOT_TOKEN", "TWITTER_BEARER_TOKEN", "CHAT_ID"]
        for var in required_vars:
            self.assertIn(var, os.environ)
