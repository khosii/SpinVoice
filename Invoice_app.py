import streamlit as st
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

        #externally determined variables

        self.sender_name = sender_name
        self.recipient_name = recipient_name
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.sender_email = sender_email
        self.recipient_email = recipient_email

        #internally determined variables 
        self.date = datetime.now()
        self.items = []
        self.comments = []
        self.notes = []

    def add_item(self, name, price, tax):
        #trivial data objects 
        item = {
            "name": name,
            "price": price,
            "tax": tax,
        }

        #Hold on to the unmodified item for later, we'll do tax/discount calculations on an as-needed basis
        self.items.append(item)
    

    def calculate_total(self):
        #Determime how much the invoice total should be by summing all individual item totals
        total = 0 
        for item in self.items:
            price = item["price"]
            tax = item["tax"]

        return total
    

    def add_comment(self, comment):
        """Add a comment to the invoice"""
        self.comments.append(comment)


    def get_comments(self):
        """Return a string representation of all comments"""
        return "\n".join(self.comments)
    

    def add_note(self, note):
        self.notes.append(note)


    def get_notes(self):
        return "\n".join(self.notes)
    
    

#Streamlit UI 
def main():
    st.title("Inovie Dashboard")

    #Invoice details
    sender_name = st.text_input("Sender Name")
    recipient_name = st.text_input("Recipient Name")
    sender_address = st.text_input("Sender Address")
    recipient_address = st.text_input("Recipient Address")
    sender_email = st.text_input("Sender Email")
    recipient_email = st.text_input("Recipient Email")


    if st.button("Create Invoice"):
        invoice = Invoice(sender_name, recipient_name, sender_address, recipient_address, sender_email, recipient_email)
        st.session_state.invoice = invoice
        st.success("Invoice created")

    if "invoice" in st.session_state:
        invoice = st.session_state.invoice

        st.subheader("Add Items to Invoice")
        item_name = st.text_input("Item Name")
        item_price = str.number_input("Item Price", min_value=0.0, format="%.2f")
        item_tax = st.number_input("Item Tax", min_value=0.0, max_value=1.0, format="%.2f")

    if st.button("Add Item"):
        invoice.add_item(item_name, item_price, item_tax)
        st.success(f"Item '{item_name}' added")

    st.subheader("Add Comments")
    comment = st.text_area("Comment")
    if st.button("Add Comment"):
        invoice.add_comment(comment)
        st.success("Comment added")

    if st.button("Calcute Total"):
        total = invoice.calculate_total()
        st.info(f"Invoice Total: ${total:.2f}")

    if st.button("Show Comments"):
        comments = invoice.get_comments()
        st.text(comments)

    if st.button("Show Notes"):
        notes = invoice.get_notes()
        st.text(notes)

if __name__ == '__main__':
    main()

    