# Copyright

from odoo import fields, models, api
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning


class AlbaranUte(models.Model):
    _inherit = 'repair.order'

    fecha_albaran = fields.Date(string='Fecha albarán')
    secuencia_albaran = fields.Char(string='Secuencia')
    orden_trabajo = fields.Char(string='Orden de trabajo')
    nombre_reparacion = fields.Text(string='Descripción')
    fecha_notificacion = fields.Date(string='Fecha notificación')

    def get_hours(self):
        for record in self:
            total = 0
            for li in record.fees_lines:
                total += li.product_uom_qty
            record.horas = total
    horas = fields.Float(string='Horas', compute='get_hours', store=False)