amountsHeads = 0
amountsTails = 0
sums = 0

while True:
    again = input("Do you want to flip again? ")
    match again.lower():
        case 'no':
            break
        case 'yes':
            response = input("Throw the coin and enter heads or tails here: ")
            with open(f"../files/HeadsOrTails.txt", "w") as file:
                file.writelines(response + "\n")
            match response.lower():
                case 'heads':
                    amountsHeads = amountsHeads + 1
                    sums = sums + 1
                    print("Heads: ", (amountsHeads / sums) * 100, "%")
                case 'tails':
                    amountsTails = amountsTails + 1
                    sums = sums + 1
                    print("Tails: ", (amountsTails / sums) * 100, "%")
