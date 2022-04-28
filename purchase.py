# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import If, Eval, Bool


class Purchase(metaclass=PoolMeta):
    __name__ = 'purchase.purchase'

    shipment_party = fields.Many2One('party.party', 'Shipment Party',
        states={
            'readonly': (Eval('state') != 'draft'),
            },
        context={
            'company': Eval('company', -1),
            },
        search_context={
            'related_party': Eval('party'),
            },
        depends=['state', 'party', 'company'])
    shipment_address = fields.Many2One('party.address', 'Shipment Address',
        domain=[
            ('party', '=', If(Bool(Eval('shipment_party')),
                    Eval('shipment_party'), Eval('party'))),
            ],
        states={
            'readonly': Eval('state') != 'draft',
            'required': ~Eval('state').in_(
                ['draft', 'quotation', 'cancelled']),
            },
        depends=['party', 'shipment_party', 'state'])

    @fields.depends('party', 'shipment_party', 'payment_term', 'lines')
    def on_change_party(self):
        super().on_change_party()
        if not self.shipment_party:
            self.shipment_address = None
        if self.party:
            if not self.shipment_address:
                self.shipment_address = self.party.address_get(type='delivery')

    @fields.depends('party', 'shipment_party')
    def on_change_shipment_party(self):
        if self.shipment_party:
            self.shipment_address = self.shipment_party.address_get(
                type='delivery')
        elif self.party:
            self.shipment_address = self.party.address_get(type='delivery')


class PurchaseLine(metaclass=PoolMeta):
    __name__ = 'purchase.line'

    @fields.depends('product')
    def _get_tax_rule_pattern(self):
        pattern = super()._get_tax_rule_pattern()
        print('PURCHASE GET TAX RULE PATTERN')
        if self.product and self.product.template.suspensive_regime:
            pattern['suspensive_regime'] = (
                self.product.template.suspensive_regime)
        return pattern