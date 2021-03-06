#!/usr/bin/python
# -*- coding: utf-8 -*-

from thumbor.crypto import Crypto

def test_can_create_crypto():
    crypto = Crypto(salt="something")

    assert crypto
    assert crypto.salt == "somethingsomethi"

def test_crypto_encrypts():
    crypto = Crypto(salt="something")

    encrypted = crypto.encrypt(width=300,
                               height=300,
                               smart=True,
                               fit_in=False,
                               flip_horizontal=True,
                               flip_vertical=True,
                               halign="center",
                               valign="middle",
                               crop_left=10,
                               crop_top=11,
                               crop_right=12,
                               crop_bottom=13,
                               image="/some/image.jpg")

    assert encrypted == 'OI8j7z9h88_IVzYLiq9UWPkBPBwwJ1pMKQw1UVrL7odTcog5UT4PBBrzoehKm7WUNxU5oq8mV59xMJJUc2aKWA=='

def test_decrypt():
    crypto = Crypto(salt="something")

    encrypted = crypto.encrypt(width=300,
                               height=200,
                               smart=True,
                               fit_in=False,
                               flip_horizontal=True,
                               flip_vertical=True,
                               halign="center",
                               valign="middle",
                               crop_left=10,
                               crop_top=11,
                               crop_right=12,
                               crop_bottom=13,
                               image="/some/image.jpg")

    decrypted = crypto.decrypt(encrypted)

    assert decrypted['width'] == 300
    assert decrypted['height'] == 200
    assert decrypted['smart'] == True

def test_decrypting_with_wrong_key_fails():

    crypto = Crypto(salt="something")

    encrypted = crypto.encrypt(width=300,
                               height=200,
                               smart=True,
                               fit_in=False,
                               flip_horizontal=True,
                               flip_vertical=True,
                               halign="center",
                               valign="middle",
                               crop_left=10,
                               crop_top=11,
                               crop_right=12,
                               crop_bottom=13,
                               image="/some/image/")

    crypto = Crypto(salt="simething")

    decrypted = crypto.decrypt(encrypted)

    assert decrypted

def test_encdec_with_extra_args():

    crypto = Crypto(salt="something")

    encrypted = crypto.encrypt(width=300,
                               height=200,
                               smart=False,
                               fit_in=True,
                               flip_horizontal=True,
                               flip_vertical=True,
                               halign="center",
                               valign="middle",
                               crop_left=10,
                               crop_top=11,
                               crop_right=12,
                               crop_bottom=13,
                               image="/some/image")

    decrypted = crypto.decrypt(encrypted)

    assert decrypted['width'] == 300
    assert decrypted['height'] == 200
    assert not decrypted['smart']
    assert decrypted['fit_in']
    assert decrypted['horizontal_flip']
    assert decrypted['vertical_flip']

    assert decrypted['halign'] == "center"
    assert decrypted['valign'] == "middle"

    assert decrypted['crop']
    assert decrypted['crop']['left'] == 10
    assert decrypted['crop']['top'] == 11
    assert decrypted['crop']['right'] == 12
    assert decrypted['crop']['bottom'] == 13

