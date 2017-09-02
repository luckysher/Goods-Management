from openerp.osv import fields, osv

class good(osv.osv):

    _name = 'gdm.good'
    _table = 'gdm_good'
    _description = 'Goods to send or receive'
    _columns = {
        'name': fields.char('Name', help="Name of the goods that will either supplied or received", select=True, copy=True),
        'desc': fields.text('Description', help="Detailed information regarding the good", select=True, copy=True),
        'mf_date': fields.date('Manufacturing date', help="Manufatring date of this good")
    }

class goods_supplier(osv.osv):
    _name = 'gdm.supplier'
    _table = 'gdm_supplier'
    _description = 'Goods suppliers'
    _columns = {
        'name': fields.many2one('res.users', help='Supplier that will supplier the goods', select=True, copy=False),
        'address': fields.char('Supplier address', help='Supplier address from where goods, order will be received and send', select=True),
        'company_name': fields.char('Company name', help='Supplier`s company name', select=True),
        'email': fields.char('Email', help='Email Id of supplier', select=True),
        'website': fields.char('Website', help='Supplier`s website', select=True),
        'mobile': fields.char('Mobile No', help='Supplier`s mobile number', select=True),
        'fax': fields.char('Fax', help='Supplier`s Fax', select=True),
        'title': fields.char('Title', help='', select=True),
        'goods': fields.one2many('gdm.good', 'id', help='Add goods for supplier', copy=True),
        'image': fields.binary("Image",
                               help="This field holds the image used as image for the supplier, limited to 1024x1024px.")

      }

