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
        'name': fields.char('Name', help='Supplier that will supplier the goods', required=True, select=True, copy=False),
        'city': fields.char('City', help='Supplier city', select=True),
        'state': fields.char('State', help='Supplier state', select=True),
        'country': fields.char('Country', help='Supplier country', select=True),
        'zip': fields.integer('Zip code', help='Supplier zip', select=True),
        'company_name': fields.char('Company name', help='Supplier`s company name', select=True),
        'email': fields.char('Email', help='Email Id of supplier', select=True),
        'website': fields.char('Website', help='Supplier`s website', select=True),
        'jobPosition': fields.selection([('',''), ('dir', 'Director'), ('tech','Technical Director')], 'Job Position', help='Jon position', select=True),
        'mobile': fields.char('Mobile No', help='Supplier`s mobile number', select=True),
        'phone': fields.char('Phone', help='Supplier`s phone number', select=True),
        'fax': fields.char('Fax', help='Supplier`s Fax', select=True),
        'goods': fields.one2many('gdm.good', 'id', help='Goods Details', copy=True),
        'image': fields.binary("Image",
                               help="This field holds the image used as image for the supplier, limited to 1024x1024px.")

      }

    def supplier_address_action(self):
        return 1

class customer(osv.osv):
    _name = 'gdm.customer'
    _table = 'gdm_customer'
    _description = 'customer'
    _columns = {
        'name': fields.many2one('res.users', help='Supplier that will supplier the goods', select=True, copy=False),
        'address': fields.char('Supplier address',
                               help='Supplier address from where goods, order will be received and send', select=True),
        'ordered_quantity': fields.char('Ordered quantity', help='', select=True),
        'type': fields.char('Order Type', help='', select=True)
    }

class invoice(osv.osv):
    _name = 'gdm.invoice'
    _table = 'gdm_invoice'
    _columns = {
        'supplier': fields.one2one('gdm.supplier', 'name', help='Supplier Name', copy=True),
        'fPosition': fields.selection([('', ''), ('tx', 'Tax'), ('te', 'Tax Exempt')], 'Fiscal Position',
                                        help='Fiscal position', select=True),
        'source_doc': fields.char('Source document', help='', select=True),
        'Supplier Invoice number': fields.char('Invoice number for the supplier', help='', select=True),
        'pays_status': fields.char('Payment Status', help='', select=True),
        'invoice_date': fields.date('Invoice date', help="Date of the request"),
        'due_date': fields.date('Due date', help="Due Date for the payment")
    }