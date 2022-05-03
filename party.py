# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta


class Address(metaclass=PoolMeta):
    __name__ = 'party.address'

    tax_deposit_code = fields.Char("Tax Deposit Code")
