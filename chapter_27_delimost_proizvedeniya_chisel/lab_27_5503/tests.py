from unittest import TestCase, main as testmain
from chapter_27_delimost_proizvedeniya_chisel.lab_27_5503.A_27_5503 import main as main_A
from chapter_27_delimost_proizvedeniya_chisel.lab_27_5503.B_27_5503 import main as main_B
from unittest.mock import patch
import io

class TestApps(TestCase):
    def test_A_27_5503(self):
        with patch('builtins.input', side_effect=[6, 77, 14, 7, 9, 499, 100, 7700]), \
             patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            main_A()
            self.assertEqual('Вычисленное контрольное значение: 7700\n'
                             'Контроль пройден\n',
                             fake_out.getvalue())

    def test_B_27_5503(self):
        with patch('builtins.input', side_effect=[6, 77, 14, 7, 9, 499, 100, 7700]), \
             patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            main_B()
            self.assertEqual('Вычисленное контрольное значение: 7700\n'
                             'Контроль пройден\n',
                             fake_out.getvalue())

if __name__ == '__main__':
    testmain()