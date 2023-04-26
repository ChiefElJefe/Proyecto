# -*- coding: utf-8 -*-

from odoo import models, fields, api

BUGS_TYPES = [
    ('blue_screen', 'Blue Screen'),
    ('audio_glitch', 'Audio Glitch'),
    ('graphic_glitch', 'Graphic Glitch'),
    ('low_performance', 'Low Performance'),
    ('other_issues', 'Other Issues'),
]


class Ticket(models.Model):
    _name = 'proyecto.ticket'
    _description = 'proyecto.ticket'

    name = fields.Char("User")
    email = fields.Char(string="Email")
    subject = fields.Selection(BUGS_TYPES, string="Subject")
    description = fields.Text(string="Description")
    repair_id = fields.Many2one('proyecto.repairs')
