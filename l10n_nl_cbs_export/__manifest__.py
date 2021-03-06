# Copyright 2017 Odoo Experts (<https://www.odooexperts.nl>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "CBS Export Intrahandel Sale",
    "version": "11.0.1.0.0",
    "author": "Odoo Experts, Onestein, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-netherlands",
    "category": "Accounting",
    "depends": ["account", "report_intrastat"],
    "summary": "CBS Export File for Dutch Intrahandel Sale",
    "data": [
        "security/ir.model.access.csv",
        "security/cbs_export_file_security.xml",
        "data/cbs_export_file_sequence.xml",
        "data/cron_process_cbs_export.xml",
        "view/cbs_export_file_view.xml",
    ],
    "installable": True,
    "license": "AGPL-3",
}
