# -*- encoding: utf-8 -*-
from __future__ import print_function, unicode_literals, division, absolute_import

from enocean.protocol.packet import Packet
from enocean.protocol.constants import RORG


def test_ute():
    # ['0xd4', '0xa0', '0xff', '0x3e', '0x0', '0x1', '0x1', '0xd2', '0x1', '0x94', '0xe3', '0xb9', '0x0'] ['0x1', '0xff', '0xff', '0xff', '0xff', '0x40', '0x0']
    status, buf, p = Packet.parse_msg(bytearray([
        0x55,
        0x00, 0x0D, 0x07, 0x01,
        0xFD,
        0xD4, 0xA0, 0xFF, 0x3e, 0x00, 0x01, 0x01, 0xD2, 0x01, 0x94, 0xE3, 0xB9, 0x00,
        0x01, 0xFF, 0xFF, 0xFF, 0xFF, 0x40, 0x00,
        0xAB
    ]))
    assert p.sender_hex == '01:94:E3:B9'
    assert p.unidirectional is False
    assert p.bidirectional is True
    assert p.response_expected is True
    assert p.number_of_channels == 0xFF
    assert p.rorg_manufacturer == 0x3E
    assert p.rorg_of_eep == RORG.VLD
    assert p.rorg_func == 0x01
    assert p.rorg_type == 0x01
    assert p.teach_in is True
    assert p.delete is False