from odoo import models, api
import logging

_logger = logging.getLogger(__name__)

class PosOrder(models.Model):
    _inherit = 'pos.order'

    @api.model
    def create_from_ui(self, orders, draft=False):
        """Override to auto-trigger eTIMS after POS order creation with invoice"""
        _logger.info('POS eTIMS Auto Invoice: create_from_ui called')
        
        order_ids = super().create_from_ui(orders, draft)
        
        for order_data in order_ids:
            order = self.browse(order_data['id'])
            _logger.info(f'Processing POS order {order.name}, has invoice: {bool(order.account_move)}')
            
            # Check if order has invoice and trigger eTIMS
            if (order.account_move and 
                order.company_id.country_id.code == 'KE' and 
                hasattr(order.account_move, 'action_l10n_ke_oscu_send_customer_invoice') and
                getattr(order.company_id, 'l10n_ke_oscu_is_active', False) and
                not order.account_move.l10n_ke_oscu_invoice_number):
                
                try:
                    _logger.info(f'Auto-triggering eTIMS for POS invoice {order.account_move.name}')
                    order.account_move.action_l10n_ke_oscu_send_customer_invoice()
                    _logger.info(f'eTIMS integration successful for POS invoice {order.account_move.name}')
                except Exception as e:
                    _logger.error(f'eTIMS integration failed for POS invoice {order.account_move.name}: {str(e)}')
        
        return order_ids