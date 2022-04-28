# This file is part account_tax_rule_tax_deposit module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest


from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class AccountTaxRuleTaxDepositTestCase(ModuleTestCase):
    'Test Account Tax Rule Tax Deposit module'
    module = 'account_tax_rule_tax_deposit'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            AccountTaxRuleTaxDepositTestCase))
    return suite
