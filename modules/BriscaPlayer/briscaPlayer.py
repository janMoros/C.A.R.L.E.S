### Estructura de les cartes: (numero, pal). Pals com a strings.
##################### CONSTANTS:
W_pinta = 10
W_benefici = 9.5
W_cost = 2


class partida:
    ############################################################# ESTRUCTURA DE DADES
    def __init__(self): #, maInicial, pinta):
        #self.cartesJugades = [pinta]
        self.ma = []
        self.pinta = (0,'a')
        self.puntsH = 0
        self.puntsIA = 0
    ############################################################# HEURÍSTIQUES
    valorNumeros = {1: 11, 3: 10, 12: 4, 11: 3, 10: 2, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 2: 0}
    prioritat_base = {1: 12, 3: 11, 12: 10, 11: 9, 10: 8, 9: 7, 8: 6, 7: 5, 6: 4, 5: 3, 4: 2, 2: 1}

    def cost(self, carta):
        cost = self.prioritat_base[carta[0]]
        if carta[1] == self.pinta[1]:
            cost *= W_pinta
        return cost

    def guanyaIA(self, cartaIA, cartaH, comencaH): # true si IA guanya H
        if cartaIA[1] == self.pinta[1] and cartaH[1] != self.pinta[1]:
            return True
        elif cartaIA[1] != self.pinta[1] and cartaH[1] == self.pinta[1]:
            return False
        else:
            if comencaH and cartaIA[1] != cartaH[1]:
                return False
            elif not comencaH and cartaIA[1] != cartaH[1]:
                return True
            else: # Si els pals son iguals
                if self.prioritat_base[cartaIA[0]] > self.prioritat_base[cartaH[0]]:
                    return True
                else:
                    return False

    def benefici(self,cartaH,cartaIA,comencaH=True):
        b = self.valorNumeros[cartaH[0]] + self.valorNumeros[cartaIA[0]]
        if not self.guanyaIA(cartaIA,cartaH,comencaH): # Si guanya l'humà
            b = -b
        return b

    def h(self,comencaH,cartaIA,cartaH=None):
        if not comencaH:
            h = - self.cost(cartaIA)
        else:
            h = self.benefici(cartaH, cartaIA) * W_benefici - self.cost(cartaIA) * W_cost
        return h

    def TriarCarta(self,comencaH,cartaH=None): #retorna l'índex de la carta seleccionada
        cartaSelec = 0
        h_cartaSelec = self.h(comencaH,self.ma[0],cartaH)
        for i,carta in enumerate(self.ma[1:]):
            h = self.h(comencaH,carta,cartaH)
            if h > h_cartaSelec:
                h_cartaSelec = h
                cartaSelec = i+1
        return cartaSelec

    ############################################################# ALTRES FUNCIONS

    def el7laTreu(self, ma):
        for i,carta in enumerate(ma):
            if (self.pinta[0] > 7 or self.pinta[0] in [1,3]) and carta[0] == 7 and self.pinta[1] == carta[1]:
                self.pinta, ma[i] = carta, self.pinta
                print("El 7 la treu")
            elif self.pinta not in [1,3] and carta[0] == 2 and self.pinta[1] == carta[1]:
                self.pinta, ma[i] = carta, self.pinta
                print("El 2 la treu perquè un 7 ja ho és")



