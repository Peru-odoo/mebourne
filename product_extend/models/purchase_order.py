from odoo import models, fields, api, _

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    internal_po_no = fields.Char(string='Internal PO No')


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    supplier_id = fields.Many2one('res.partner')


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    invoice_no = fields.Char(string='Invoice No')
    internal_po_no = fields.Char(string='Internal PO No')
    project_name = fields.Char(string='Project Name')


class PurchseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    brand_id = fields.Many2one('product.brand', string='Brand')

    @api.onchange('product_id')
    def _onchange_product(self):
        product_tempalte_obj = self.env['product.template'].search([('id', '=', self.product_id.product_tmpl_id.id)])
        self.brand_id = product_tempalte_obj.brand_id
