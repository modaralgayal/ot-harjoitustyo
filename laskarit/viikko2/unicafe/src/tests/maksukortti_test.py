import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_saldo_ei_muutu_jos_ei_ole_tarpeeksi(self):

        kortti = Maksukortti(200)
        kortti.ota_rahaa(300)

        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")
