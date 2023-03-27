# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class PurchaseLastCost(models.Model):
    _inherit = 'purchase.order'

    #@api.onchange('currency_id')
    #def _get_tasa_currency(self):
        #for order in self:
            #order.tipo_cambio_othercurrency = order.currency_id.inverse_rate

    def button_confirm(self):
        res = super(PurchaseLastCost,self).button_confirm()
        for line in self.order_line:
            line.product_id.standard_price = line.price_unit * self.currency_id.inverse_company_rate

            getSupplierLine = line.product_id.seller_ids.filtered(lambda r: r.name == self.partner_id)
            for p in getSupplierLine:
                if p.currency_id.id == self.currency_id.id:
                    p.price = line.price_unit
            if not getSupplierLine:
                self.env['product.supplierinfo'].sudo().create({'name': self.partner_id.id, 'currency_id': self.currency_id.id, 'price': line.price_unit})
        return res
