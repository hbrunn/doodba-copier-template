# Copyright 2020 Hunki Enterprises
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import mock
from odoo import models
from odoo.addons.mis_builder import models as mis_models

from .aep import AEP


class MisReport(models.Model):
    _inherit = "mis.report"

    def _prepare_aep(self, companies, currency=None):
        """Use custom AEP object"""
        with mock.patch.object(mis_models.mis_report, "AEP") as aep:
            aep.side_effect = AEP
            return super()._prepare_aep(companies, currency=currency)
