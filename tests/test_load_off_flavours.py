from unittest import TestCase
from off_flavor import OffFlavor, load_off_flavors

class test_off_flavours(TestCase):
    def test_load(self) -> None:
        data = load_off_flavors()
        off_flavor = OffFlavor(
            name='Ethanethiol of ethyl mercaptaan',
            description='Afvoerput',
            causes='Een ongezonde gist of giststerfte (autolyse)',
            doemens_nr=21)

        self.assertIn(off_flavor, data)