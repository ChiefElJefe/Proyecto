from odoo import http
from odoo.http import request


class Gamesite(http.Controller):

    @http.route('/incidence_form', type="http", auth="public", website=True)
    def incidence(self, **kw):
        return http.request.render('proyecto.create_ticket', {})

    @http.route('/create/ticket', type="http", auth="public", website=True)
    def create_incidence(self, **kw):
        request.env['proyecto.ticket'].sudo().create(kw)
        return http.request.render('proyecto.send_incidence', {})
