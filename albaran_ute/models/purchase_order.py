# Copyright

from odoo import fields, models, api
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.depends('sale_id', 'repair_id')
    def get_report_job(self):
        for record in self:
            job = ""
            if (record.sale_id.id) and not (record.repair_id.id):
                job = record.sale_id.name
            elif (record.repair_id.id) and not (record.sale_id.id):
                try:
                    end = record.repair_id.name.index(' ', 0)
                    job = record.repair_id.name[1:end]
                except:
                    job = record.repair_id.name
            elif (record.repair_id.id) and (record.sale_id.id):
                try:
                    end = record.repair_id.name.index(' ', 0)
                    job = record.sale_id.name + " | " + record.repair_id.name[1:end]
                except:
                    job = record.sale_id.name + " | " + record.repair_id.name
            record.report_job = job

    report_job = fields.Char(compute='get_report_job', store=True)