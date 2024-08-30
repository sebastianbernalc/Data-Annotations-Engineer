# Functions.py
class VendorInfo:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def to_dict(self):
        return {
            "vendor_name": self.name,
            "vendor_address": self.address,
        }

class BillToInfo:
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {
            "bill_to_name": self.name,
        }

class InvoiceInfo:
    def __init__(self, invoice_number, date, vendor_info, bill_to_info):
        self.invoice_number = invoice_number
        self.date = date
        self.vendor_info = vendor_info
        self.bill_to_info = bill_to_info

    def to_dict(self):
        return {
            "invoice_number": self.invoice_number,
            "date": self.date,
            **self.vendor_info.to_dict(),
            **self.bill_to_info.to_dict(),
        }

class LineItem:
    def __init__(self, sku, description, quantity, tax_rate, price, total):
        self.sku = sku
        self.description = description
        self.quantity = quantity
        self.tax_rate = tax_rate
        self.price = price
        self.total = total

    def to_dict(self):
        return {
            "sku": self.sku,
            "description": self.description,
            "quantity": self.quantity,
            "tax_rate": self.tax_rate,
            "price": self.price,
            "total": self.total,
        }

def validate_field(field_name, field_value):
    if not field_value:
        raise ValueError(f"Missing or invalid value for {field_name}")
    return field_value

def extract_general_info(response):
    vendor_info = VendorInfo(
        validate_field("vendor_name", response.get("vendor", {}).get("name")),
        validate_field("vendor_address", response.get("vendor", {}).get("address"))
    )
    
    bill_to_info = BillToInfo(
        validate_field("bill_to_name", response.get("bill_to", {}).get("name"))
    )

    invoice_info = InvoiceInfo(
        validate_field("invoice_number", response.get("invoice_number")),
        validate_field("date", response.get("date")),
        vendor_info,
        bill_to_info
    )

    return invoice_info.to_dict()

def extract_line_items(response):
    return [LineItem(
        item.get("sku"),
        item.get("description"),
        item.get("quantity"),
        item.get("tax_rate"),
        item.get("price"),
        item.get("total")
    ).to_dict() for item in response.get("line_items", [])]
