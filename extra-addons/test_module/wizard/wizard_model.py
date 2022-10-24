from odoo import fields, models
from odoo.exceptions import ValidationError

class Wizard_model(models.TransientModel):
    _name = "wizard.model"

    name = fields.Char()

    def create_and_add_client(self):
        if self.env['res.partner'].search([('name', '=', self.name)]):
            raise ValidationError('User already exists')
        else:
            client = self.env['res.partner'].create({'name': self.name})
            test_model_line = self.env['test.model.lines'].create({'partner_id': client.id, 'test_model_id': self.env.context.get('active_id')})
            return client
            
    def create_and_edit_client(self):
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': 'web#id=%s&cids=&menu_id=74&model=res.partner&view_type=form' % self.create_and_add_client().id
        }
        