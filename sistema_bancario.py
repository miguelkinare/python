menu = """"

[d] Depositar
[s] Sacar
[e] Extarto
[q] sair


"""

saldo = 0
limite = 500
extrato = "--"
numero_saques = 3
LIMITE_SAQUES = 3

while True:
  opcao = input(menu)

  if opcao == "d":
      print("Deposito")
      valor = float(input("Informe o valor do deposito:"))
      if valor > 0:
          saldo += valor
          extrato += f"deposito: R${valor:.2f}"
      else:
            print("Operação falhou! o valor informado é invalido")
      

  elif opcao == "s":
       print("Saque")
       valor = float(input("Informe o valor do sacar:"))
       excedeu_saldo = valor > saldo
       excedeu_limite = valor > limite
       excedeu_saque = valor >= LIMITE_SAQUES
       if excedeu_saldo:
           print("Operação falhou! você não tem saldo suficiente")
       
       elif excedeu_limite:
           print("Operação falhou! você não tem limite suficiente")
        
       elif excedeu_saque:
           print("Operação falhou! você não tem saque suficiente")
        
       elif valor > 0:
           saldo -= valor
           extrato += f"deposito: R${valor:.2f}"
           numero_saques += 1
       else:
           print("Operação falhou! o valor informado é invalido")




  elif opcao == "e":
       print("=================Extrato===============")
       print("Não foi realizado movimentação" if not extrato else extrato)
       print(f"\nSaldo: R${saldo:.2f}")
       print("========================================")
  elif opcao == "q":
      break
  
  else:
      print("operação invalida,por favor selecione novamente a operação desejada.")
