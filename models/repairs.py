from odoo import models, fields, api


class Repairs(models.Model):
    _name = 'proyecto.repairs'
    _description = 'proyecto.repairs'

    name = fields.Char(string="Stage")
    ticket_id = fields.One2many('proyecto.ticket', 'stage_id')
