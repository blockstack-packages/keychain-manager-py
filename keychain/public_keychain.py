from bitmerchant.wallet import Wallet as HDWallet


class PublicKeychain():
    def __init__(self, public_keychain):
        if isinstance(public_keychain, HDWallet):
            self.hdkeychain = public_keychain
        elif isinstance(public_keychain, (str, unicode)):
            self.hdkeychain = HDWallet.deserialize(public_keychain)
        else:
            raise ValueError('public keychain must be a string')

    def __str__(self):
        return self.hdkeychain.serialize_b58(private=False)

    def child(self, index):
        child_keychain = self.hdkeychain.get_child(
            index, is_prime=False, as_private=False)
        return PublicKeychain(child_keychain)

    def descendant(self, chain_path):
        """ A descendant is a child many steps down.
        """
        public_child = self.hdkeychain
        chain_step_bytes = 4
        max_bits_per_step = 2**31
        chain_steps = [
            int(chain_path[i:i+chain_step_bytes*2], 16) % max_bits_per_step
            for i in range(0, len(chain_path), chain_step_bytes*2)
        ]
        for step in chain_steps:
            public_child = public_child.get_child(step)

        return PublicKeychain(public_child)

    def public_key(self, compressed=True):
        return self.hdkeychain.get_public_key_hex(compressed=compressed)

    def address(self):
        return self.hdkeychain.to_address()
