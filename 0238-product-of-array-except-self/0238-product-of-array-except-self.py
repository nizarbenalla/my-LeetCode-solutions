class Solution:
    def productExceptSelf(self, nombres: List[int]) -> List[int]:
        taille = len(nombres)
        resultat = [1] * taille

        facteur = 1
        for i in range(taille):
            resultat[i] = facteur
            facteur *= nombres[i]

        facteur = 1
        for i in range(taille - 1, -1, -1):
            resultat[i] *= facteur
            facteur *= nombres[i]

        return resultat