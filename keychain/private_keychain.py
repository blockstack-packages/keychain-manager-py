from bitmerchant.wallet import Wallet as HDWallet
from .public_keychain import PublicKeychain


class PrivateKeychain():
    def __init__(self, private_keychain=None):
        if private_keychain:
            if isinstance(private_keychain, HDWallet):
                self.hdkeychain = private_keychain
            elif isinstance(private_keychain, (str, unicode)):
                self.hdkeychain = HDWallet.deserialize(private_keychain)
            else:
                raise ValueError('private keychain must be a string')
        else:
            self.hdkeychain = HDWallet.new_random_wallet()

    def __str__(self):
        return self.hdkeychain.serialize_b58(private=True)

    def hardened_child(self, index):
        child_keychain = self.hdkeychain.get_child(
            index, is_prime=True, as_private=True)
        return PrivateKeychain(child_keychain)

    def child(self, index):
        child_keychain = self.hdkeychain.get_child(
            index, is_prime=False, as_private=True)
        return PrivateKeychain(child_keychain)

    def public_keychain(self):
        public_keychain = self.hdkeychain.public_copy()
        return PublicKeychain(public_keychain)

    def private_key(self):
        return self.hdkeychain.get_private_key_hex()
