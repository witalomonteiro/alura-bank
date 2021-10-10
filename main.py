import conta

conta1 = conta.Conta(123, "Witalo", 100.0, 1000.0)
conta2 = conta.Conta(321, "Monteiro", 250.0, 1000.0)


conta1.imprimir_extrato()

conta1.transferir(conta2, 2000)