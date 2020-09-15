# Copyright 2020 Hunki Enterprises
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import inspect

from odoo.addons.mis_builder.models import aep
from odoo.osv import expression


class AEP(aep.AccountingExpressionProcessor):
    """A version of the expression processor that does custom mapping and filtering"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # walk up the stack to find the mis instance calling us
        frame = inspect.currentframe()
        self.mis_instance = None
        while frame:
            if (
                "self" in frame.f_locals
                and getattr(frame.f_locals["self"], "_name", None)
                == "mis.report.instance"
            ):
                self.mis_instance = frame.f_locals["self"]
                break
            frame = frame.f_back

    def _account_codes_to_domain(self, account_codes):
        domain = super()._account_codes_to_domain(account_codes)
        if not self.mis_instance.use_holding_accounts:
            return domain
        return tuple(
            [
                leaf
                if not expression.is_leaf(leaf) or leaf[0] != "code"
                else tuple(["code_holding"] + list(leaf[1:]))
                for leaf in domain
            ]
        )

    def get_aml_domain_for_expr(
        self, expr, date_from, date_to, target_move, account_id=None
    ):
        domain = super().get_aml_domain_for_expr(
            expr, date_from, date_to, target_move, account_id=account_id
        )
        if not self.mis_instance.ignore_partner_ids:
            return domain
        return expression.AND(
            [
                domain,
                [("partner_id", "not in", self.mis_instance.ignore_partner_ids.ids)],
            ]
        )

    def get_aml_domain_for_dates(self, date_from, date_to, mode, target_move):
        domain = super().get_aml_domain_for_dates(date_from, date_to, mode, target_move)
        if not self.mis_instance.ignore_partner_ids:
            return domain
        return expression.AND(
            [
                domain,
                [("partner_id", "not in", self.mis_instance.ignore_partner_ids.ids)],
            ]
        )
