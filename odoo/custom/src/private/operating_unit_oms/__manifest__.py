# Copyright 2020 Hunki Enterprises BV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Operating Unit (OMS)",
    "summary": "OMS adaptions for Operating Unit",
    "version": "13.0.1.0.0",
    "category": "Generic",
    "author": "Hunki Enterprises BV",
    "license": "AGPL-3",
    "depends": [
        "operating_unit_hierarchical",
        "sale_operating_unit",
        "analytic_operating_unit",
        "mis_builder_operating_unit",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/operating_unit.xml",
        "views/operating_unit_level.xml",
    ],
}
