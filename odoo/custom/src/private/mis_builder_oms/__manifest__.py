# Copyright 2020 Hunki Enterprises BV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "MIS Builder (OMS)",
    "summary": "OMS adaptions for MIS builder",
    "version": "13.0.1.0.0",
    "category": "Reporting",
    "author": "Hunki Enterprises BV",
    "license": "AGPL-3",
    "depends": [
        "mis_builder",
        # TODO depend on this when deployment is clear
        # "cg_accounting",
    ],
    "data": [
        "views/mis_report_instance.xml",
    ],
}
