# This file is part account_tax_rule_tax_deposit module for Tryton.
# The COPYRIGHT file at the top level of this repository contains


from trytond.tests.test_tryton import ModuleTestCase
from trytond.modules.company.tests import CompanyTestMixin


class AccountTaxRuleTaxDepositTestCase(CompanyTestMixin, ModuleTestCase):
    'Test Account Tax Rule Tax Deposit module'
    module = 'account_tax_rule_tax_deposit'
    extras = ['purchase', 'sale']


del ModuleTestCase