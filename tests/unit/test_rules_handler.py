"""
TODO: Doku
"""
from easywall.rules_handler import RulesHandler
from easywall.utility import file_get_contents, write_into_file
from tests import unittest


class TestRulesHandler(unittest.TestCase):
    """
    TODO: Doku
    """

    def setUp(self):
        self.rules = RulesHandler()
        self.rules.rules_firstrun()

    def test_firstrun(self):
        """
        TODO: Doku
        """
        self.rules.rules_firstrun()

    def test_get_current_rules(self):
        """
        TODO: Doku
        """
        write_into_file("{}/current/tcp".format(self.rules.rulesfolder), """80
443
""")
        self.assertEqual(self.rules.get_current_rules("tcp"), ["80", "443"])

    def test_backup_current_rules(self):
        """
        TODO: Doku
        """
        write_into_file("{}/current/tcp".format(self.rules.rulesfolder), """80
443
""")
        write_into_file("{}/backup/tcp".format(self.rules.rulesfolder), "")
        self.rules.backup_current_rules()
        self.assertEqual(file_get_contents("{}/backup/tcp".format(self.rules.rulesfolder)), """80
443
""")

    def test_apply_new_rules(self):
        """
        TODO: Doku
        """
        write_into_file("{}/new/tcp".format(self.rules.rulesfolder), """80
443
""")
        write_into_file("{}/current/tcp".format(self.rules.rulesfolder), "")
        self.assertEqual(self.rules.get_current_rules("tcp"), [])
        self.rules.apply_new_rules()
        self.assertEqual(self.rules.get_current_rules("tcp"), ["80", "443"])

    def test_rollback_from_backup(self):
        """
        TODO: Doku
        """
        write_into_file("{}/backup/tcp".format(self.rules.rulesfolder), """80
443
""")
        write_into_file("{}/current/tcp".format(self.rules.rulesfolder), "")
        self.assertEqual(self.rules.get_current_rules("tcp"), [])
        self.rules.rollback_from_backup()
        self.assertEqual(self.rules.get_current_rules("tcp"), ["80", "443"])
