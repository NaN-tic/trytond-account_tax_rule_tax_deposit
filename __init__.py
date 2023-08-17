# This file is part account_tax_rule_tax_deposit module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import party
from . import product
from . import purchase
from . import sale
from . import tax
from . import move


def register():
    Pool.register(
        party.Address,
        product.Template,
        product.Product,
        tax.TaxRuleTemplate,
        tax.TaxRuleLineTemplate,
        tax.TaxRule,
        tax.TaxRuleLine,
        module='account_tax_rule_tax_deposit', type_='model')
    Pool.register(
        purchase.Purchase,
        purchase.PurchaseLine,
        module='account_tax_rule_tax_deposit', type_='model',
        depends=['purchase'])
    Pool.register(
        sale.SaleLine,
        module='account_tax_rule_tax_deposit', type_='model',
        depends=['sale'])
    Pool.register(
        move.Move,
        module='account_tax_rule_tax_deposit', type_='model',
        depends=['stock_valued'])
