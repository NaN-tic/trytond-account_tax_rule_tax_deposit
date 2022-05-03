# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta


class TaxRuleLineTemplate(metaclass=PoolMeta):
    __name__ = 'account.tax.rule.template'

    suspensive_regime = fields.Boolean("Suspensive Regime")


class TaxRuleLine(metaclass=PoolMeta):
    __name__ = 'account.tax.rule.line'

    suspensive_regime = fields.Boolean("Suspensive Regime")

    def match(self, pattern):
        pattern = pattern.copy()
        suspensive_regime = None
        if 'suspensive_regime' in pattern:
            suspensive_regime = pattern.pop('suspensive_regime')

        from_tax_deposit = False
        if 'from_tax_deposit' in pattern:
            from_tax_deposit = pattern.pop('from_tax_deposit')

        to_tax_deposit = False
        if 'to_tax_deposit' in pattern:
            to_tax_deposit = pattern.pop('to_tax_deposit')

        if suspensive_regime:
            if suspensive_regime == False:
                return False
            if not from_tax_deposit and not to_tax_deposit:
                return False
            if from_tax_deposit and not to_tax_deposit:
                return False
        return super().match(pattern)

