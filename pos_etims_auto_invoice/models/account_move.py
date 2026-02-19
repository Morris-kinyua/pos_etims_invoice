from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    l10n_ke_qr_code_url = fields.Char(
        string="eTIMS QR Code URL", 
        compute="_compute_etims_qr_url"
    )
    
    @api.depends('l10n_ke_oscu_signature', 'company_id.vat', 'company_id.l10n_ke_branch_code')
    def _compute_etims_qr_url(self):
        for move in self:
            if (move.l10n_ke_oscu_signature and 
                move.company_id.vat and 
                move.company_id.l10n_ke_branch_code):
                domain = "etims-sbx" if move.company_id.l10n_ke_server_mode == "test" else "etims"
                data = f"{move.company_id.vat}{move.company_id.l10n_ke_branch_code}{move.l10n_ke_oscu_signature}"
                move.l10n_ke_qr_code_url = f"https://{domain}.kra.go.ke/common/link/etims/receipt/indexEtimsReceiptData?Data={data}"
            else:
                move.l10n_ke_qr_code_url = False