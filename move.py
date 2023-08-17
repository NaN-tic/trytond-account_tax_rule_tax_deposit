# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta


class Move(metaclass=PoolMeta):
    __name__ = 'stock.move'

    @fields.depends('product', 'shipment', '_parent_shipment.')
    def _get_tax_rule_pattern(self):
        pattern = super()._get_tax_rule_pattern()
        pattern['suspensive_regime'] = False
        if self.product and self.product.template.suspensive_regime:
            pattern['suspensive_regime'] = (
                self.product.template.suspensive_regime)
        pattern['to_tax_deposit'] = False
        pattern['from_tax_deposit'] = False
        if self.shipment and self.shipment.__name__ == 'stock.shipment.out':
            if (self.shipment and self.shipment.delivery_address and
                    self.shipment.delivery_address.tax_deposit_code):
                pattern['to_tax_deposit'] = True
            if (self.shipment and self.shipment.warehouse and
                    self.shipment.warehouse.address and
                    self.shipment.warehouse.address.tax_deposit_code):
                pattern['from_tax_deposit'] = True
        elif self.shipment and self.shipment.__name__ == 'stock.shipment.in':
            if (self.shipment and self.shipment.contact_address and
                    self.shipment.contact_address.tax_deposit_code):
                pattern['from_tax_deposit'] = True
            if (self.shipment and self.shipment.warehouse and
                    self.shipment.warehouse.address and
                    self.shipment.warehouse.address.tax_deposit_code):
                pattern['to_tax_deposit'] = True
        return pattern
