# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval


class TaxRuleTemplate(metaclass=PoolMeta):
    __name__ = 'account.tax.rule.template'

    use_suspensive_regime = fields.Boolean("Use Suspensive Regime")


class TaxRuleLineTemplate(metaclass=PoolMeta):
    __name__ = 'account.tax.rule.line.template'

    suspensive_regime = fields.Boolean("Suspensive Regime")


class TaxRule(metaclass=PoolMeta):
    __name__ = 'account.tax.rule'

    use_suspensive_regime = fields.Boolean("Use Suspensive Regime")


class TaxRuleLine(metaclass=PoolMeta):
    __name__ = 'account.tax.rule.line'

    suspensive_regime = fields.Boolean("Suspensive Regime",
        states={
            'invisible': ~Eval('_parent_rule', {}).get(
                'use_suspensive_regime', False)
        })

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

        if self.rule and self.rule.use_suspensive_regime:
            if self.suspensive_regime and suspensive_regime != None:
                if self.suspensive_regime and not suspensive_regime:
                    return False
                else:
                    if from_tax_deposit and to_tax_deposit:
                        pass
                    else:
                        return False
            else:
                return False

        return super().match(pattern)

