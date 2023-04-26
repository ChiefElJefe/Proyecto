# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class ProyectoProjectModule(http.Controller):
    @http.route('/proyecto_project_module/', website=True, auth='public')
    def index(self, **kw):
        # return "Hello, world"
        return request.render("proyecto_project_module.ticket_page", {})

#     @http.route('/proyecto_project_module/proyecto_project_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('proyecto_project_module.listing', {
#             'root': '/proyecto_project_module/proyecto_project_module',
#             'objects': http.request.env['proyecto_project_module.proyecto_project_module'].search([]),
#         })

#     @http.route('/proyecto_project_module/proyecto_project_module/objects/<model("proyecto_project_module.proyecto_project_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proyecto_project_module.object', {
#             'object': obj
#         })
