import frappe
from frappe.utils import get_url
from urlparse import urlparse

def get_home_page(arg1):
	domain_name = urlparse(get_url()).netloc
	site = frappe.get_list("Site", filters={'domain_name': domain_name}, fields=['target_type'])
	if site:
		return "/" + site[0]['target_type'].lower()+"2"
	if frappe.local.flags.home_page:
		return frappe.local.flags.home_page
