# -*- coding: utf-8 -*-

from odoo import models, fields, api



class CNWLS_WMS_MASTER(models.Model):
	_name 			= "cnwls.wms.warehouse"
	_description 	= "cnwls.wms.warehouse"
	company_id      = fields.Many2one('res.company', 'Company', required=True, index=True,  default=lambda self: self.env.user.company_id.id)
	name 			= fields.Char("Warehouse")
	whse_id 		= fields.Char("Warehouse ID")
	whse_code 	    = fields.Char("Warehouse Code ")
	whse_name 	    = fields.Char("Warehouse Name ")
	ibin            = fields.Char("Bin Location Enabled") 
	

	itemcount 		= fields.Integer("Item Count",default=0)
	itemqty 		= fields.Float("Item Quantity", digit=(19,2), default=0.0)
	itemvalue 		= fields.Float("Item Value",digit=(19,2),default=0.0)	


class CNWLS_WMS_LOCATION(models.Model):
	_name 			= "cnwls.wms.location"
	_description 	= "cnwls.wms.location"
	company_id      = fields.Many2one('res.company', 'Company', required=True, index=True,  default=lambda self: self.env.user.company_id.id)
	name 			= fields.Char("Location")
	location_id 	= fields.Char("Location ID")
	location_code 	= fields.Char("Location Code ")
	location_name 	= fields.Char("Location Name ") 


class CNWLS_WMS_BIN(models.Model):
	_name 			= "cnwls.wms.bin"
	_description 	= "cnwls.wms.bin"
	company_id      = fields.Many2one('res.company', 'Company', required=True, index=True,  default=lambda self: self.env.user.company_id.id)
	name 			= fields.Char("Bin Location")
	bin_id 	        = fields.Char("Bin ID")
	bin_name 	    = fields.Char("Bin Name")
	istatus 	    = fields.Char("Status") 

	itemcount 		= fields.Integer("Item Count",default=0)
	itemqty 		= fields.Float("Item Quantity", digit=(19,2), default=0.0)
	itemvalue 		= fields.Float("Item Value",digit=(19,2),default=0.0)	



class CNWLS_WMS_BP(models.Model):
	_name 			= "cnwls.wms.bp"
	_description 	= "cnwls.wms.bp"
	company_id      = fields.Many2one('res.company', 'Company', required=True, index=True,  default=lambda self: self.env.user.company_id.id)
	name 			= fields.Char("Partner ")
	partner_id		= fields.Char("Partner Code")
	partner_name	= fields.Char("Partner Name") 
	

class CNWLS_WMS_ITEM(models.Model):
	_name 			= "cnwls.wms.item"
	_description 	= "cnwls.wms.item"
	company_id      = fields.Many2one('res.company', 'Company', required=True, index=True,  default=lambda self: self.env.user.company_id.id)
	name 			= fields.Char("Item ")
	itemcode		= fields.Char("Item  Code")
	itemname 	    = fields.Char("Item Name") 
	itemgroup 	    = fields.Char("Item Group") 
	
# end of MAster data 
#####


class CNWLS_OpnameMaster(models.Model):
	_name 			= "cnwls.wms.opname"
	_description 	= "cnwls.wms.opname"
	company_id      = fields.Many2one('res.company', 'Company', required=True, index=True,  default=lambda self: self.env.user.company_id.id)
	name 			= fields.Char("Opname Number")
	itemcode		= fields.Char("Item  Code")
	itemname 	    = fields.Char("Item Name") 
	itemgroup 	    = fields.Char("Item Group") 


class CNWLS_OpnameDetail(models.Model):
	_name 			= "cnwls.wms.opname.line"
	_description 	= "cnwls.wms.opname.line"
	company_id      = fields.Many2one('res.company', 'Company', required=True, index=True,  default=lambda self: self.env.user.company_id.id)
	name 			= fields.Char("Opname Number")
	itemcode		= fields.Char("Item  Code")
	itemname 	    = fields.Char("Item Name") 
	itemgroup 	    = fields.Char("Item Group") 