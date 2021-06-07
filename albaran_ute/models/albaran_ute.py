# Copyright

from odoo import fields, models, api
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning


class AlbaranUte(models.Model):
    _inherit = 'repair.order'

    fecha_albaran = fields.Date(string='Fecha')
    secuencia_albaran = fields.Char(string='Secuencia')
    orden_trabajo = fields.Char(string='Orden de trabajo')
    nombre_reparacion = fields.Text(string='Nombre')
