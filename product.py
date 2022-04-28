# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta


class Template(metaclass=PoolMeta):
    __name__ = 'product.template'

    suspensive_regime = fields.Boolean("Suspensive Regime")