# -*- coding: utf-8 -*-
from odoo import http

# class /data/cnwls/cnwlsWms(http.Controller):
#     @http.route('//data/cnwls/cnwls_wms//data/cnwls/cnwls_wms/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//data/cnwls/cnwls_wms//data/cnwls/cnwls_wms/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/data/cnwls/cnwls_wms.listing', {
#             'root': '//data/cnwls/cnwls_wms//data/cnwls/cnwls_wms',
#             'objects': http.request.env['/data/cnwls/cnwls_wms./data/cnwls/cnwls_wms'].search([]),
#         })

#     @http.route('//data/cnwls/cnwls_wms//data/cnwls/cnwls_wms/objects/<model("/data/cnwls/cnwls_wms./data/cnwls/cnwls_wms"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/data/cnwls/cnwls_wms.object', {
#             'object': obj
#         })