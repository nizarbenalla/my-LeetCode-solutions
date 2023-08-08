class Solution {
    public int maxProfit(int[] valeurs) {
        int debutAchat = 0;
        int profitMaximal = 0;
        
        for (int i = 1; i < valeurs.length; i++) {
            if (valeurs[debutAchat] < valeurs[i]) {
                profitMaximal = Math.max(profitMaximal, valeurs[i] - valeurs[debutAchat]);
            } else {
                debutAchat = i;
            }
        }
        
        return profitMaximal;
    }
}
