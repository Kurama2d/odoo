from odoo import fields, models, api

class TestModel(models.Model):
    _name = "test.model"
    
    name = fields.Char()
    description = fields.Text()
    count = fields.Integer()
    float = fields.Float()
    currency_id = fields.Many2one("res.currency")
    money = fields.Monetary()
    html = fields.Html()
    date = fields.Date()
    time = fields.Datetime()
    checkbox = fields.Boolean()
    select = fields.Selection([("one", "Один"), ("two", "Два")])
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Good'),
        ('2', 'Very Good'),
        ('3', 'Excellent')
    ])
    file = fields.Binary()
    image = fields.Binary()
    sign = fields.Binary()
    
    doc_creator = fields.Many2one('res.users','Doc Creator', default=lambda self: self.env.user.id, required=True) 
    responsible_contact = fields.Many2one('res.partner', 'Responsible Contact')
    
    clients = fields.One2many('test.model.lines', 'test_model_id', string='Clients')
    
    check_1 = fields.Boolean()
    check_2 = fields.Boolean()
    all = fields.Boolean()
    
    
    @api.onchange('check_1', 'check_2')
    def _onchange_checkbox(self):
        if self.check_1 and self.check_2:
            self.all = True
        elif not self.check_1 and self.all:
            self.all = False
            self.check_2 = True
        elif not self.check_2 and self.all:
            self.all = False
            self.check_1 = True
    
    @api.onchange('all')
    def _onchange_all(self):
        if not self.all and (self.check_1 and self.check_2):
            self.check_1 = False
            self.check_2 = False
        if self.all:
            self.check_1 = True
            self.check_2 = True

    def open_wizard(self):
        new_wizard = self.env['wizard.model'].create({})

        return {
            'type': 'ir.actions.act_window',
            'name': 'Create and Add Client',
            'view_mode': 'form',
            'res_model': 'wizard.model',
            'target': 'new',
            'res_id': new_wizard.id,
            'views': [[False, 'form']],
        }
    
    
class TestModelLines(models.Model):
    _name = "test.model.lines"
    
    test_model_id = fields.Many2one('test.model', ondelete='cascade')
    partner_id = fields.Many2one('res.partner', ondelete='cascade')
    
    email = fields.Char(related='partner_id.email')
     