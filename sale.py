# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta


class SaleLine(metaclass=PoolMeta):
    __name__ = 'sale.line'

    @fields.depends('product', 'sale', '_parent_sale.shipment_address',
        '_parent_sale.warehouse')
    def _get_tax_rule_pattern(self):
        pattern = super()._get_tax_rule_pattern()
        pattern['suspensive_regime'] = False
        if self.product and self.product.template.suspensive_regime:
            pattern['suspensive_regime'] = (
                self.product.template.suspensive_regime)
        pattern['to_tax_deposit'] = False
        if (self.sale and self.sale.shipment_address and
                self.sale.shipment_address.tax_deposit_code):
            pattern['to_tax_deposit'] = True
        pattern['from_tax_deposit'] = False
        if (self.sale and self.sale.warehouse and
                self.sale.warehouse.address and
                self.sale.warehouse.address.tax_deposit_code):
            pattern['from_tax_deposit'] = True
        return pattern

