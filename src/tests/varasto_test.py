import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_luo_negetiivisella_tilavuudella(self):
        varasto = Varasto(-1)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_konstruktori_luo_negatiivisella_saldolla(self):
        varasto = Varasto(2, -1)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_konstruktori_luo_ylijaamasaldolla(self):
        varasto = Varasto(2, 3)
        self.assertAlmostEqual(varasto.saldo, 2)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_saldoa_yli_tilavuuden(self):
        self.varasto.lisaa_varastoon(18)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_negatiivista_saldoa(self):
        self.varasto.lisaa_varastoon(-8)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_palauttaa_nolla_kun_negatiivinen(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(-2)

        self.assertAlmostEqual(saatu_maara, 0)

    def test_ottaminen_palauttaa_kaikki_kun_liikaa(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(12)

        self.assertAlmostEqual(saatu_maara, 8)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ottaminen_lisaa_tilaa_kun_negatiivinen(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(-2)

        # varastossa pitäisi olla tilaa 10 - 8 + 0 eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_lisaa_tilaa_kun_liikaa_ottaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(12)

        # varastossa pitäisi olla tilaa 10 - 8 + 12 eli 10 (14)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_konstruktori_asettaa_ja_string(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
