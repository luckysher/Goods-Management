from openerp.osv import fields, osv

class goods(osv.osv):

    _name = 'gdm.goods'
    _table = 'gdm_goods'
    _description = 'Goods to send or receive'
    _columns = {
        'name': fields.char('Name', help="Name of the goods that will either supplied or received", select=True, copy=True),
        'description': fields.text('Description', help="Detailed information regarding the good", select=True, copy=True)
    }


