from unittest import TestCase, main as testmain
from chapter_27_delimost_summi_i_proizvedeniya_pary.lab_27_15812.B_27_15812 import main as main_B

from unittest.mock import patch
import io

class TestApps(TestCase):
    def test_A_27_5503(self):
        with patch('builtins.input', side_effect=[4, 1, 2, 3, 4]), \
             patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            main_B()
            self.assertEqual('2\n', fake_out.getvalue())

    def test_A_27_5503_2(self):
        with patch('builtins.input', side_effect=[6, 1, 2, 3, 4, 5, 6]), \
             patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            main_B()
            self.assertEqual('5\n', fake_out.getvalue())