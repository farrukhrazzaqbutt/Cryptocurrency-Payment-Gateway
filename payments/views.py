from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from web3 import Web3

from .forms import TransactionForm
from .models import Transaction

# Connect to an Ethereum node
web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))


def create_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            recipient = form.cleaned_data['recipient']
            amount = float(form.cleaned_data['amount'])

            # Create and sign transaction
            transaction = {
                'to': recipient,
                'value': web3.toWei(amount, 'ether'),
                'gas': 2000000,
                'gasPrice': web3.toWei('50', 'gwei'),
                'nonce': web3.eth.getTransactionCount(sender),
            }
            private_key = 'YOUR_PRIVATE_KEY'
            signed_txn = web3.eth.account.signTransaction(transaction, private_key)

            # Send transaction
            tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            tx_hash_hex = web3.toHex(tx_hash)

            # Save transaction to database
            Transaction.objects.create(tx_hash=tx_hash_hex, sender=sender, recipient=recipient, amount=amount, status='pending')

            return JsonResponse({'tx_hash': tx_hash_hex})
    else:
        form = TransactionForm()

    return render(request, 'payments/create_transaction.html', {'form': form})

def get_transaction_status(request, tx_hash):
    transaction = get_object_or_404(Transaction, tx_hash=tx_hash)
    tx_receipt = web3.eth.getTransactionReceipt(tx_hash)

    if tx_receipt:
        transaction.status = 'confirmed' if tx_receipt['status'] == 1 else 'failed'
        transaction.save()

    return render(request, 'payments/transaction_status.html', {'status': transaction.status})
