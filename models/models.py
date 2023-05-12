# -*- coding: utf-8 -*-
from odoo import models, fields, api
import html2text
import base64
from datetime import datetime
import requests
import json
import pandas as pd
import pandas.io.sql
import pytz
from num2words import num2words
import pymssql
from odoo.exceptions import UserError
from odoo.modules import get_modules, get_module_path
from jinja2 import Environment, FileSystemLoader
import pdfkit
import os


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
	countdate		= fields.Char("Count Date")
	ref2 	    	= fields.Char("Ref2") 
	remarks 	    = fields.Char("Remarks") 

	v_totalqty 		= fields.Float("Total Qty  Inventory Counting")
	v_totalvalue	= fields.Float("Total Value Inventory Counting")

	v_sap_id 		= fields.Char("SAP ID - Docentry")
	v_sap_docnum 	= fields.Char("SAP Docnum")
	v_sap_status 	= fields.Char("Status")

	opname_line_ids = fields.One2many("cnwls.wms.opname.line", "opname_id")


class CNWLS_OpnameDetail(models.Model):
	_name 			= "cnwls.wms.opname.line"
	_description 	= "cnwls.wms.opname.line"
	company_id      = fields.Many2one("res.company", "Company", required=True, index=True,  default=lambda self: self.env.user.company_id.id)

	opname_id		= fields.Many2one("cnwls.wms.opname","Opname")

	name 			= fields.Char("Opname Number")
	linenum 		= fields.Char("LineNumber")  
	itemcode		= fields.Char("Item  Code")
	itemname 	    = fields.Char("Item Name") 
	itemgroup 	    = fields.Char("Item Group") 
	itemsubgroup 	= fields.Char("Item Sub Group") 
	opname_id  		= fields.Char("Opname IDS")
	countqty 		= fields.Float("Counted Qty")
	inwarehouseqty 	= fields.Float("in WH Qty")
	variance 		= fields.Float("Variance / difference")
	afterqty		= fields.FLoat("After Opname")
	avgprice		= fields.FLoat("Avg Price")
	amount			= fields.FLoat("Amount")
	
	v_sap_id 		= fields.Char("SAP ID - Docentry")
	v_sap_docnum 	= fields.Char("SAP Docnum")
	v_sap_status 	= fields.Char("Status")



class CNWLS_OpnameGenerate(models.TransientModel):
	_name 			= "cnwls.wms.opname.generate"
	_description 	= "cnwls.wms.opname.generate"
	company_id      = fields.Many2one("res.company", "Company", required=True, index=True,  default=lambda self: self.env.user.company_id.id)

	countdate 		= fields.Date("Count Date")

	filexls         = fields.Binary("File Output")    
	filenamexls     = fields.Char("File Name Output")

	v_sap_ids 		= fields.Char("SAP ID - Docentry")
	

