from flask import Blueprint
from .algod import get_balance
from .forms import SendForm

def index():
    balance = get_balance("INPUT YOUR TESTNET ADDRESS HERE")
    return render_template('index.html', balance=balance)

main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@main_bp.route('/send', methods=['GET', 'POST'])
def send():
    """Provides a form to create and send a transaction"""
    form = SendForm()
    address = "INPUT YOUR TESTNET ADDRESS HERE" # use mnemonic.to_public_key(passphrase)
    sk = "INPUT YOUR PRIVATE KEY HERE" # use mnemonic.to_private_key(passphrase)
    if form.validate_on_submit():
        success = send_txn(address, form.quantity.data, form.receiver.data, form.note.data, sk)
        return render_template('success.html', success=success)

    # show the form, it wasn't submitted
    return render_template('send.html', form=form, address=address)

@main_bp.route('/')
def index():
    return "Algorand Balance"