# Copyright 2020 Hunki Enterprises BV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class OperatingUnit(models.Model):
    _inherit = "operating.unit"

    level_id = fields.Many2one(
        "operating.unit.level", index=True, required=True, compute="_compute_level_id"
    )

    @api.depends("parent_level")
    def _compute_level_id(self):
        for this in self.sorted("parent_level"):
            this.level_id = this.parent_id.level_id._next_level() or self.env[
                "operating.unit.level"
            ].search([("level", "=", 0)])
