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
        print('\n\nTAX PATTERN:\n',pattern,'\n')
        if 'suspensive_regime' in pattern:
            if self.suspensive_regime == False:
                return False
        return super().match(pattern)

