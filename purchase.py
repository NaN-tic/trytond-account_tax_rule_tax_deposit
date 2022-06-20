# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import If, Eval, Bool


class Purchase(metaclass=PoolMeta):
    __name__ = 'purchase.purchase'

    shipment_address = fields.Many2One('party.address', 'Shipment Address',
        domain=[
            ('party', '=', If(Bool(Eval('party')),
                    Eval('party'), Eval('party'))),
            ],
        states={
            'readonly': Eval('state') != 'draft',
            'required': ~Eval('state').in_(
                ['draft', 'quotation', 'cancelled']),
            },
        depends=['party', 'state'])

    @fields.depends('party', 'payment_term', 'lines', 'shipment_address')
    def on_change_party(self):
        super().on_change_party()
        if not self.party:
            self.shipment_address = None
        if self.party:
            if not self.shipment_address:
                self.shipment_address = self.party.address_get(type='delivery')


class PurchaseLine(metaclass=PoolMeta):
    __name__ = 'purchase.line'

    @fields.depends('product', 'purchase', '_parent_purchase.shipment_address',
        '_parent_purchase.warehouse')
    def _get_tax_rule_pattern(self):
        pattern = super()._get_tax_rule_pattern()
        pattern['suspensive_regime'] = False
        if self.product and self.product.template.suspensive_regime:
            pattern['suspensive_regime'] = (
                self.product.template.suspensive_regime)
        pattern['from_tax_deposit'] = False
        if (self.purchase and self.purchase.shipment_address and
                self.purchase.shipment_address.tax_deposit_code):
            pattern['from_tax_deposit'] = True
        pattern['to_tax_deposit'] = False
        if (self.purchase and self.purchase.warehouse and
                self.purchase.warehouse.address and
                self.purchase.warehouse.address.tax_deposit_code):
            pattern['to_tax_deposit'] = True
        return pattern
