from usuario import Usuario

lopez = Usuario("Guido Lopez")
monty = Usuario("Ricardo Monty")
reyes = Usuario("Anibal Reyes")

lopez.hacer_depósito(500)
lopez.hacer_depósito(55)
lopez.hacer_depósito(100)
lopez.hacer_retiro(350)
lopez.mostrar_balance_usuario()

monty.hacer_depósito(140)
monty.hacer_depósito(1200)
monty.hacer_retiro(50)
monty.hacer_retiro(90)
monty.mostrar_balance_usuario()

reyes.hacer_depósito(700)
reyes.hacer_retiro(780)
reyes.hacer_retiro(5150)
reyes.hacer_retiro(2270)
reyes.mostrar_balance_usuario()

lopez.transferir_dinero(100, reyes)
lopez.mostrar_balance_usuario()
reyes.mostrar_balance_usuario()