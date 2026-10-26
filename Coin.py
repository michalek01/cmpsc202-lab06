#Isaac Michalek
import time as time
import matplotlib.pyplot as plt

def coin_change_recursive(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    
    min_coins = float('inf')
    for coin in coins:
        num_coins = coin_change_recursive(coins, amount - coin)
        if num_coins != float('inf'):
            min_coins = min(min_coins, num_coins + 1)
    
    return min_coins

def coin_change_recursive_memoized(coins, amount, memo):
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    
    min_coins = float('inf')
    for coin in coins:
        num_coins = coin_change_recursive_memoized(coins, amount - coin, memo)
        if num_coins != float('inf'):
            min_coins = min(min_coins, num_coins + 1)
    
    memo[amount] = min_coins
    return min_coins

def coin_change_dp(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


def compare_performance():
    coins = [1, 5, 10, 25]

    # Keep the naive recursive algorithm manageable
    amounts = [5, 10, 15, 20, 25, 30]

    recursive_times = []
    memoized_times = []
    dp_times = []

    for amount in amounts:
        # Naive recursion
        start_time = time.perf_counter()
        result1 = coin_change_recursive(coins, amount)
        recursive_times.append(time.perf_counter() - start_time)

        # Top-down dynamic programming
        start_time = time.perf_counter()
        result2 = coin_change_recursive_memoized(
            coins, amount, {}
        )
        memoized_times.append(time.perf_counter() - start_time)

        # Bottom-up dynamic programming
        start_time = time.perf_counter()
        result3 = coin_change_dp(coins, amount)
        dp_times.append(time.perf_counter() - start_time)

        # Verify correctness
        assert result1 == result2 == result3

    # Print results
    print("Amount | Recursive | Memoized | Bottom-Up")
    for i, amount in enumerate(amounts):
        print(
            f"{amount:6} | "
            f"{recursive_times[i]:.8f} | "
            f"{memoized_times[i]:.8f} | "
            f"{dp_times[i]:.8f}"
        )

    # Graph the results
    plt.figure(figsize=(9, 5))

    plt.plot(amounts, recursive_times,
             marker="o", label="Naive Recursive")
    plt.plot(amounts, memoized_times,
             marker="s", label="Memoized")
    plt.plot(amounts, dp_times,
             marker="^", label="Bottom-Up DP")

    plt.xlabel("Target Amount")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Coin Change Algorithm Performance")
    plt.yscale("log")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("performance_comparison.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    compare_performance()
