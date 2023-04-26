# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class proyecto_project_module(models.Model):
#     _name = 'proyecto_project_module.proyecto_project_module'
#     _description = 'proyecto_project_module.proyecto_project_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
