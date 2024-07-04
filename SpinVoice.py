from datetime import datetime


class Invoice:
    """Represents an invoice for a collection of services rendered to a recipient"""

    def __init__(self,
                 sender_name,
                 recipient_name,
                 sender_address,
                 recipient_address,
                 sender_email,
                 recipient_email):
        # externally determined variables
        self.sender_name = sender_name
        self.recipient_name = recipient_name
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.sender_email = sender_email
        self.recipient_email = recipient_email

        # internally determined variables
        self.date = datetime.now()
        self.items = []
        self.comments = [] #List to store comments
        self.notes = [] #List to store general purpose notes


    def add_item(self, name, price, tax):
        # python makes working with trivial data-objects quite easy
        item = {
            "name": name,
            "price": price,
            "tax": tax,
        
        }

        # hold on to the unmodified item for later, we'll do tax/discount calculations on an as-needed basis
        self.items.append(item)


    def calculate_total(self, discount):
        # determine how much the invoice total should be by summing all individual item totals
        total = 0
        for item in self.items:
            price = item["price"]
            tax = item["tax"]

            #Apply item-specific discount
            discounted_price = price - (price * discount)

            #Apply tax after discount
            total += discounted_price + (discounted_price * tax)

        return total
    
    def add_comment(self, comment):
        """Add a comment to the invoice"""
        self.comments.append(comment)
    
    def get_comments(self):
        """Return a string representation of all comments"""
        return "\n".join(self.comments)

    def add_note(self, note):
        """Add a general purpose note to the invoice"""
        self.notes.append(note)

    def get_notes(self):
        """Return a string representation of all notes"""
        return "\n".join(self.notes)
    
    


if __name__ == '__main__':
    invoice = Invoice(
        "Larry Jinkles",
        "Tod Hooper",
        "34 Windsor Ln.",
        "14 Manslow road",
        "lejank@billing.com",
        "discreetclorinator@hotmail.com"
    )

    invoice.add_item("34 floor building", 3400, .1)
    invoice.add_item("Equipment Rental", 1000, .1)
    invoice.add_item("Fear Tax", 340, 0.0)
    
    invoice.add_comment("First comment")

    print("Comments on the Invoice:")
    invoice_total = invoice.calculate_total(.4)
    print(invoice.get_comments())