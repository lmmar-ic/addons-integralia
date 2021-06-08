# Copyright

from odoo import fields, models, api
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning


class AlbaranUte(models.Model):
    _inherit = 'repair.order'

    ute_fecha_albaran = fields.Date(string='Fecha albarán')
    ute_secuencia = fields.Char(string='Secuencia')
    ute_ot = fields.Char(string='Orden de trabajo')
    ute_descripcion = fields.Text(string='Descripción')
    ute_fecha_notificacion = fields.Date(string='Fecha notificación')
    ute_cargo = fields.Char('Cargo')

    def get_hours(self):
        for record in self:
            total = 0
            for li in record.fees_lines:
                total += li.product_uom_qty
            record.horas = total
    horas = fields.Float(string='Horas', compute='get_hours', store=False)

    def get_ute_sequence(self):
        for record in self:
            if not record.ute_secuencia:
                record.ute_secuencia = self.env['ir.sequence'].next_by_code('albaran.ute')
