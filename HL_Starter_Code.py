from datetime import datetime

class BankAccount:
    # Class variable for generating unique account numbers
    _account_counter = 100000

    def __init__(self, holder_name, starting_balance=0.0, account_type="STANDARD"):
        self.holder_name = holder_name
        self.account_type = account_type

        # Encapsulation: protected balance
        self._balance = starting_balance if starting_balance >= 0 else 0.0

        # Unique account number
        self.account_number = BankAccount._account_counter
        BankAccount._account_counter += 1

        # Optional transaction log (still single-class)
        self._transactions = []

        # Record account creation
        self._record_transaction(
            amount=self._balance,
            transaction_type="ACCOUNT_CREATED",
            description=f"Initial balance set to {self._balance}"
        )

    # -----------------------------------------------------
    # Encapsulated balance access
    # -----------------------------------------------------
    def get_balance(self):
        return self._balance

    # -----------------------------------------------------
    # Internal helper for transaction history
    # -----------------------------------------------------
    def _record_transaction(self, amount, transaction_type, description=""):
        timestamp = datetime.now()
        entry = {
            "timestamp": timestamp,
            "type": transaction_type,
            "amount": amount,
            "description": description
        }
        self._transactions.append(entry)

    # -----------------------------------------------------
    # Deposit
    # -----------------------------------------------------
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be a positive amount.")
            return False

        self._balance += amount
        self._record_transaction(
            amount=amount,
            transaction_type="DEPOSIT",
            description=f"Deposited {amount}"
        )
        return True

    # -----------------------------------------------------
    # Withdraw
    # -----------------------------------------------------
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        if amount > self._balance:
            print("Insufficient funds for withdrawal.")
            return False

        self._balance -= amount
        self._record_transaction(
            amount=amount,
            transaction_type="WITHDRAWAL",
            description=f"Withdrew {amount}"
        )
        return True

    # -----------------------------------------------------
    # Transaction history
    # -----------------------------------------------------
    def print_transaction_history(self):
        print(f"\nTransaction history for account {self.account_number}:")
        for entry in self._transactions:
            time = entry["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
            print(f"{time} | {entry['type']} | {entry['amount']} | {entry['description']}")
        print()

    # -----------------------------------------------------
    # String representation (optional helper)
    # -----------------------------------------------------
    def __str__(self):
        return f"Account({self.account_number}) - {self.holder_name} | Balance: {self._balance}"
