from openerp.models import BaseModel
from openerp import fields

class goods(BaseModel):

    _name = 'gdm.goods'
    name = fields.Char('Name')
    description = fields.Text('Description')
