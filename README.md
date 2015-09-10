# keychain-manager-python

### Private Keychains

```python
>>> private_keychain = PrivateKeychain("xprv9s21ZrQH143K3QTDL4LXw2F7HEK3wJUD2nW2nRk4stbPy6cq3jPPqjiChkVvvNKmPGJxWUtg6LnF5kejMRNNU3TGtRBeJgk33yuGBxrMPHi")
>>> print private_keychain
xprv9s21ZrQH143K3QTDL4LXw2F7HEK3wJUD2nW2nRk4stbPy6cq3jPPqjiChkVvvNKmPGJxWUtg6LnF5kejMRNNU3TGtRBeJgk33yuGBxrMPHi
```

### Public Keychains

```
>>> public_keychain = private_keychain.public_keychain()
>>> print public_keychain
xpub661MyMwAqRbcFtXgS5sYJABqqG9YLmC4Q1Rdap9gSE8NqtwybGhePY2gZ29ESFjqJoCu1Rupje8YtGqsefD265TMg7usUDFdp6W1EGMcet8
```

### Hardened Private Child Keychains

```python
>>> private_child_keychain_0H = private_keychain.hardened_child(0)
```

### Un-hardened Private Child Keychains

```python
>>> private_child_keychain_0H_1 = private_keychain.hardened_child(0).child(1)
```

### Un-hardened Public Child Keychains

```python
>>> public_child_keychain_0H = private_child_keychain_0H.public_keychain(0)
>>> public_child_keychian_0H_1 = public_child_keychain_0H.child(1)
```
