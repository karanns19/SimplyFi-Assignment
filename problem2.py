# Function to calculate the minimum number of players who need to get shot
def min_players_to_get_shot(N, K, heights):
    min_shot = 0
    for h in heights:
        if h > K:
            min_shot += 1
    return min_shot

# Input number of test cases
T = int(input("Enter the number of test cases: "))

# Iterate through each test case
for _ in range(T):
    # Input N and K for each test case
    N, K = map(int, input().split())

    # Input heights of players for each test case
    heights = list(map(int, input().split()))

    # Calculate and print the minimum number of players who need to get shot
    print(min_players_to_get_shot(N, K, heights))
