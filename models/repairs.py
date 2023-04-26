from odoo import models, fields, api


class Repairs(models.Model):
    _name = 'proyecto.repairs'
    _description = 'proyecto.repairs'

    name = fields.Char("Stage")
