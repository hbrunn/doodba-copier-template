# Copyright 2020 Hunki Enterprises
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class AccountAccount(models.Model):
    _inherit = "account.account"

    # TODO remove all of this when the dependency on cg_account is fixed
    code_holding = fields.Integer()
