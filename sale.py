# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta


class SaleLine(metaclass=PoolMeta):
    __name__ = 'sale.line'

    @fields.depends('product')
    def _get_tax_rule_pattern(self):
        pattern = super()._get_tax_rule_pattern()
        print('SALE GET TAX RULE PATTERN')
        if self.product and self.product.template.suspensive_regime:
            pattern['suspensive_regime'] = (
                self.product.template.suspensive_regime)
        return pattern

