# POS eTIMS Auto Invoice Module

## Overview
This module automatically creates posted and paid invoices when the validate button is clicked in POS with the invoice option selected. After posting, it triggers the eTIMS integration to generate invoices with eTIMS details on both the invoice form and report document.

## Features

### 1. Automatic Invoice Processing
- **Auto-Post**: Invoices are automatically posted when created from POS
- **Auto-Pay**: Invoices are automatically paid using the POS payment method
- **Auto-Reconcile**: Payments are automatically reconciled with invoices

### 2. eTIMS Integration
- **Automatic Trigger**: eTIMS integration is triggered after invoice posting
- **Error Handling**: Robust error handling prevents blocking invoice creation
- **Logging**: Comprehensive logging for debugging and monitoring

### 3. Enhanced Invoice Display
- **Form View**: Additional eTIMS fields displayed on invoice form
- **QR Code URL**: Computed field for eTIMS verification URL
- **Report Template**: eTIMS details included in printed invoices

### 4. Report Enhancements
- **eTIMS Details Section**: Shows invoice number, receipt number, control unit
- **QR Code**: Visual QR code for eTIMS verification
- **Professional Layout**: Clean card-based layout for eTIMS information

## Installation
1. Place the module in your custom addons directory
2. Update the app list
3. Install the module
4. Ensure the `l10n_ke_etims_vscu` module is properly configured

## Dependencies
- `point_of_sale`
- `account`
- `l10n_ke_etims_vscu`

## Usage
1. Create a POS order with the invoice option selected
2. Click the validate button
3. The system will automatically:
   - Create the invoice
   - Post the invoice
   - Create and reconcile payment
   - Send to eTIMS (for Kenyan companies)
   - Display eTIMS details on invoice form and report

## Technical Details
- Extends `pos.order` model for automatic invoice processing
- Extends `account.move` model for eTIMS display enhancements
- Includes custom report template for eTIMS details
- Robust error handling and logging throughout



Also before installation ensure you have a l10n_ke_etims_vscu for v15 module installed
