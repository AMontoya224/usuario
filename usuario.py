class Usuario:
    def __init__(self, name):
        self.name = name
        self.balance_cuenta = 0

    def hacer_depósito(self, amount):
        self.balance_cuenta += amount
    
    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount

    def mostrar_balance_usuario(self):
        print("User: " + self.name + ", Balance: " + str(self.balance_cuenta))
    
    def transferir_dinero(self, amount, name):
        self.balance_cuenta -= amount
        name.balance_cuenta += amount