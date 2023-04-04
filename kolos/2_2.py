def cutting(slowo):
    binary = ""
    for litera in slowo:
        if litera in ["a", "e", "i", "o", "u", "y"]:
            binary += "1"
        else:
            binary += "0"

    def rekurencja(ciag, kreska=1):
        n = len(ciag)
        jedynki = 0
        for liczba in ciag:
            if liczba == "1":
                jedynki += 1

        if kreska == -1:
            if jedynki == 1:
                return 1
            else:
                return 0

        if jedynki == 0:
            return 0
        if jedynki == 1:
            return 1
        if kreska >= n:
            return 0

        lewo = ciag[:kreska]
        prawo = ciag[kreska:]

        return (rekurencja(lewo, -1) * rekurencja(prawo, 1)) + rekurencja(ciag, kreska + 1)

    return rekurencja(binary)


print(cutting('informatyka'))