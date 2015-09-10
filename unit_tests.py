import json
import traceback
import unittest
from test import test_support
from keychain import PrivateKeychain, PublicKeychain


class KeychainTest(unittest.TestCase):
    def setUp(self):
        self.private_keychains = {
            "root": "xprv9s21ZrQH143K3QTDL4LXw2F7HEK3wJUD2nW2nRk4stbPy6cq3jPPqjiChkVvvNKmPGJxWUtg6LnF5kejMRNNU3TGtRBeJgk33yuGBxrMPHi",
            "0H": "xprv9uHRZZhk6KAJC1avXpDAp4MDc3sQKNxDiPvvkX8Br5ngLNv1TxvUxt4cV1rGL5hj6KCesnDYUhd7oWgT11eZG7XnxHrnYeSvkzY7d2bhkJ7",
            "0H/1": "xprv9wTYmMFdV23N2TdNG573QoEsfRrWKQgWeibmLntzniatZvR9BmLnvSxqu53Kw1UmYPxLgboyZQaXwTCg8MSY3H2EU4pWcQDnRnrVA1xe8fs",
            "0H/1/2H": "xprv9z4pot5VBttmtdRTWfWQmoH1taj2axGVzFqSb8C9xaxKymcFzXBDptWmT7FwuEzG3ryjH4ktypQSAewRiNMjANTtpgP4mLTj34bhnZX7UiM",
            "0H/1/2H/2": "xprvA2JDeKCSNNZky6uBCviVfJSKyQ1mDYahRjijr5idH2WwLsEd4Hsb2Tyh8RfQMuPh7f7RtyzTtdrbdqqsunu5Mm3wDvUAKRHSC34sJ7in334",
            "0H/1/2H/2/1000000000": "xprvA41z7zogVVwxVSgdKUHDy1SKmdb533PjDz7J6N6mV6uS3ze1ai8FHa8kmHScGpWmj4WggLyQjgPie1rFSruoUihUZREPSL39UNdE3BBDu76"
        }
        self.public_keychains = {
            "root": "xpub661MyMwAqRbcFtXgS5sYJABqqG9YLmC4Q1Rdap9gSE8NqtwybGhePY2gZ29ESFjqJoCu1Rupje8YtGqsefD265TMg7usUDFdp6W1EGMcet8",
            "0H": "xpub68Gmy5EdvgibQVfPdqkBBCHxA5htiqg55crXYuXoQRKfDBFA1WEjWgP6LHhwBZeNK1VTsfTFUHCdrfp1bgwQ9xv5ski8PX9rL2dZXvgGDnw",
            "0H/1": "xpub6ASuArnXKPbfEwhqN6e3mwBcDTgzisQN1wXN9BJcM47sSikHjJf3UFHKkNAWbWMiGj7Wf5uMash7SyYq527Hqck2AxYysAA7xmALppuCkwQ",
            "0H/1/2H": "xpub6D4BDPcP2GT577Vvch3R8wDkScZWzQzMMUm3PWbmWvVJrZwQY4VUNgqFJPMM3No2dFDFGTsxxpG5uJh7n7epu4trkrX7x7DogT5Uv6fcLW5",
            "0H/1/2H/2": "xpub6FHa3pjLCk84BayeJxFW2SP4XRrFd1JYnxeLeU8EqN3vDfZmbqBqaGJAyiLjTAwm6ZLRQUMv1ZACTj37sR62cfN7fe5JnJ7dh8zL4fiyLHV",
            "0H/1/2H/2/1000000000": "xpub6H1LXWLaKsWFhvm6RVpEL9P4KfRZSW7abD2ttkWP3SSQvnyA8FSVqNTEcYFgJS2UaFcxupHiYkro49S8yGasTvXEYBVPamhGW6cFJodrTHy"
        }
        self.root_private_keychain = PrivateKeychain(self.private_keychains["root"])

    def tearDown(self):
        pass

    def test_root_private_to_public(self):
        public_keychain = self.root_private_keychain.public_keychain()
        self.assertEqual(str(public_keychain), str(self.public_keychains["root"]))

    def test_hardened_child_0H(self):
        private_keychain = self.root_private_keychain.hardened_child(0)
        self.assertEqual(str(private_keychain), str(self.private_keychains["0H"]))
        self.assertEqual(str(private_keychain.public_keychain()), str(self.public_keychains["0H"]))

    def test_unhardened_child_0H_1(self):
        private_keychain = self.root_private_keychain.hardened_child(0).child(1)
        self.assertEqual(str(private_keychain), str(self.private_keychains["0H/1"]))
        public_keychain = private_keychain.public_keychain()
        self.assertEqual(str(public_keychain), str(self.public_keychains["0H/1"]))
        public_keychain_2 = self.root_private_keychain.hardened_child(0).public_keychain().child(1)
        self.assertEqual(str(public_keychain), str(public_keychain_2))

    def test_5_step_derivation(self):
        private_keychain = self.root_private_keychain.hardened_child(0).child(1).hardened_child(2).child(2).child(1000000000)
        self.assertEqual(str(private_keychain), str(self.private_keychains["0H/1/2H/2/1000000000"]))
        public_keychain = private_keychain.public_keychain()
        self.assertEqual(str(public_keychain), str(self.public_keychains["0H/1/2H/2/1000000000"]))


def test_main():
    test_support.run_unittest(
        KeychainTest
    )


if __name__ == '__main__':
    test_main()