# -*- coding: utf-8 -*-

from odoo import models, fields, api

BUGS_TYPES = [
    ('blue_screen', 'Blue Screen'),
    ('audio_glitch', 'Audio Glitch'),
    ('graphic_glitch', 'Graphic Glitch'),
    ('low_performance', 'Low Performance'),
    ('other_issues', 'Other Issues'),
]

STATE_TYPE = [
    ('start', 'Start'),
    ('working_in_it', 'Working in it'),
    ('fixed', 'Fixed')
]


class Ticket(models.Model):
    _name = 'proyecto.ticket'
    _description = 'proyecto.ticket'

    def _default_stage(self):
        return self.env['proyecto.repairs'].search([], limit=1)

    @api.model
    def _expands_group_ids(self, stages, domain, order):
        return self.env['proyecto.repairs'].search([], order=order)

    name = fields.Char("User")
    email = fields.Char(string="Email")
    subject = fields.Selection(BUGS_TYPES, string="Subject")
    kanban_state = fields.Selection(STATE_TYPE, string="Status", default='start')
    description = fields.Text(string="Description")
    stage_id = fields.Many2one('proyecto.repairs', default=_default_stage, group_expand='_expands_group_ids')
