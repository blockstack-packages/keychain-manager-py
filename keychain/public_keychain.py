from bitmerchant.wallet import Wallet as HDWallet


class PublicKeychain():
    def __init__(self, public_keychain):
        if isinstance(public_keychain, HDWallet):
            keychain = public_keychain
        elif isinstance(public_keychain, (str, unicode)):
            keychain = HDWallet.deserialize(public_keychain)
        else:
            raise ValueError('public keychain must be a string')
        self.keychain = keychain

    def __str__(self):
        return self.keychain.serialize_b58(private=False)

    def child(self, index):
        child_keychain = self.keychain.get_child(
            index, is_prime=False, as_private=False)
        return PublicKeychain(child_keychain)
