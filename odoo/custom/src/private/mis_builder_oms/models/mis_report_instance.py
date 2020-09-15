# Copyright 2020 Hunki Enterprises
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import mock
from odoo import fields, models
from odoo.addons.mis_builder import models as mis_models

from .aep import AEP


class MisReportInstance(models.Model):
    _inherit = "mis.report.instance"

    use_holding_accounts = fields.Boolean(default=False)
    ignore_partner_ids = fields.Many2many(
        "res.partner",
        "mis_report_instance_ignore_partners",
        string="Ignore partners",
    )

    def drilldown(self, arg):
        """Use custom AEP object"""
        with mock.patch.object(mis_models.mis_report_instance, "AEP") as aep:
            aep.side_effect = AEP
            return super().drilldown(arg)
