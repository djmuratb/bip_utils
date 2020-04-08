# Copyright (c) 2020 Emanuele Bellocchia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


# Imports
import binascii
import unittest
from bip_utils import BitcoinConf, LitecoinConf, P2WPKH


# Some keys randomly taken from Ian Coleman web page
# https://iancoleman.io/bip39/
TEST_VECTOR = \
    [
        {
            "pub_key"      : b"03e775fd51f0dfb8cd865d9ff1cca2a158cf651fe997fdc9fee9c1d3b5e995ea77",
            "address"      :  "bc1qnjg0jd8228aq7egyzacy8cys3knf9xvrerkf9g",
            "net_addr_ver" :  BitcoinConf.P2WPKH_NET_VER["main"],
        },
        {
            "pub_key"      : b"0299b4cb4809f52dac21bbd8c997d8bf052cf4d68bfe966c638c312fbfff636e17",
            "address"      :  "bc1qtet8q6cd5vqm0zjfcfm8mfsydju0a29ggqrmu9",
            "net_addr_ver" :  BitcoinConf.P2WPKH_NET_VER["main"],
        },
        {
            "pub_key"      : b"021c1750d4a5ad543967b30e9447e50da7a5873e8be133eb25f2ce0ea5638b9d17",
            "address"      :  "ltc1qwlezpr3890hcp6vva9twqh27mr6edadreqvhnn",
            "net_addr_ver" :  LitecoinConf.P2WPKH_NET_VER["main"],
        },
        {
            "pub_key"      : b"0201084ea04fa9619a056281e7c87a97693f67e5baa4ec604e7e8245b84e31cc96",
            "address"      :  "ltc1qdjtr2jc5uu6r0ss2fcey3djvkhlu7jux420fhr",
            "net_addr_ver" :  LitecoinConf.P2WPKH_NET_VER["main"],
        },
        {
            "pub_key"      : b"02339193c34cd8ecb21ebd48af64ead71d78213470d61d7274f932489d6ba21bd3",
            "address"      :  "tb1qxdyjf6h5d6qxap4n2dap97q4j5ps6ua8sll0ct",
            "net_addr_ver" :  BitcoinConf.P2WPKH_NET_VER["test"],
        },
        {
            "pub_key"      : b"03443a4f06e4182fe7f7020318cc394ffdb5517e3ad31991f57252b631ac9df33a",
            "address"      :  "tb1qextge928njsn94qu5jhc80uyx3wpz0fjqneen4",
            "net_addr_ver" :  BitcoinConf.P2WPKH_NET_VER["test"],
        },
        {
            "pub_key"      : b"02b396686039259ba12198413122c86f5375932ca0be7e052e48107654eb8b097e",
            "address"      :  "tb1qfvczjgwnc6l4tr4ee8vlffr6hznf7u28xnm2yh",
            "net_addr_ver" :  BitcoinConf.P2WPKH_NET_VER["test"],
        },
        {
            "pub_key"      : b"034f8b2f463fa3fe8e514baf6e2d98c3bc895a22f4d0e279bbb9bc846374939fb3",
            "address"      :  "tb1q4kestxh2w7r7h5hxvn4pn2qv2dldvylgj6t2kr",
            "net_addr_ver" :  BitcoinConf.P2WPKH_NET_VER["test"],
        },
    ]

# Some invalid keys
TEST_VECTOR_KEY_ERR = \
    [
        # Private key (not accepted by P2WPKH)
        b"132750b8489385430d8bfa3871ade97da7f5d5ef134a5c85184f88743b526e38",
        # Compressed public key with valid length but wrong version (0x01)
        b"019efbcb2db9ee44cb12739e9350e19e5f1ce4563351b770096f0e408f93400c70",
        # Compressed public key with invalid length
        b"029efbcb2db9ee44cb12739e9350e19e5f1ce4563351b770096f0e408f93400c7000",
        # Uncompressed public key (not accepted by P2WPKH)
        b"aaeb52dd7494c361049de67cc680e83ebcbbbdbeb13637d92cd845f70308af5e9370164133294e5fd1679672fe7866c307daf97281a28f66dca7cbb52919824f"
    ]


#
# Tests
#
class P2WPKHTests(unittest.TestCase):
    # Run all tests in test vector
    def test_vector(self):
        for test in TEST_VECTOR:
            self.assertEqual(test["address"], P2WPKH.ToAddress(binascii.unhexlify(test["pub_key"]), test["net_addr_ver"]))

    # Test invalid keys
    def test_invalid_keys(self):
        for test in TEST_VECTOR_KEY_ERR:
            self.assertRaises(ValueError, P2WPKH.ToAddress, binascii.unhexlify(test))


# Run test if executed
if __name__ == "__main__":
    unittest.main()
