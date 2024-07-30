from django import forms

class TransactionForm(forms.Form):
    sender = forms.CharField(max_length=42)
    recipient = forms.CharField(max_length=42)
    amount = forms.DecimalField(max_digits=20, decimal_places=10)
