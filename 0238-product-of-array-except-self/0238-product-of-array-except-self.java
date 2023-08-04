class Solution {
    public int[] productExceptSelf(int[] nums) {
        int taille = nums.length;
        int[] resultat = new int[taille];

        int facteur = 1;
        for (int i = 0; i < taille; i++) {
            resultat[i] = facteur;
            facteur *= nums[i];
        }

        facteur = 1;
        for (int i = taille - 1; i >= 0; i--) {
            resultat[i] *= facteur;
            facteur *= nums[i];
        }

        return resultat;
    }
}
