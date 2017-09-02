from openerp.osv import fields, osv

class goods(osv.osv):

    _name = 'gdm.goods'
    _table = 'gdm_goods'
    _description = 'Goods to send or receive'
    _columns = {
        'name': fields.char('Name', help="Name of the goods that will either supplied or received", select=True, copy=True),
        'description': fields.text('Description', help="Detailed information regarding the good", select=True, copy=True)
    }

class goods_supplier(osv.osv):
    _name = 'goods.supplier'
    _table = 'goods_supplier'
    _description = 'Goods suppliers'
    _columns = {
        'name': fields.many2one('res.users', help='Supplier that will supplier the goods', select=True, copy=False),
        'address': fields.char('Supplier address', help='Supplier address from where goods, order will be received and send', select=True),
        'company_name': fields.char('Company name', help='Supplier`s company name', select=True),
        'email': fields.char('Email', help='Email Id of supplier', select=True),
        'website': fields.char('Website', help='Supplier`s website', select=True),
        'mobile': fields.char('Mobile No', help='Supplier`s mobile number', select=True),
        'fax': fields.char('Fax', help='Supplier`s Fax', select=True)

    }
