from odoo import models, fields, api


class Repairs(models.Model):
    _name = 'proyecto.repairs'
    _description = 'proyecto.repairs'
    _sql_constraints = [
        ('name', 'unique(name)', 'State names cannot be repeated.')
    ]

    name = fields.Char(string="Stage")
    ticket_id = fields.One2many('proyecto.ticket', 'stage_id')
