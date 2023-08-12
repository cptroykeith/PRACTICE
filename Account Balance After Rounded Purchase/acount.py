class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        purchaseAmount = (purchaseAmount + 5) // 10 * 10

        return 100 - purchaseAmount