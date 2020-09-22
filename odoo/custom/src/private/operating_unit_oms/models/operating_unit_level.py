# Copyright 2020 Hunki Enterprises BV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class OperatingUnitLevel(models.Model):
    _name = "operating.unit.level"
    _order = "level"

    level = fields.Integer(required=True)
    name = fields.Char(required=True, translate=True)

    _sql_constraints = [
        ("level_unique", "unique(level)", "Level must be unique"),
    ]

    def _next_level(self):
        if not self:
            return self
        self.ensure_one()
        return self.search(
            [("level", ">", self.level)],
            order="level asc",
            limit=1,
        )
