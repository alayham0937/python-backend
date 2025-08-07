import math
import statistics

# Custom analysis function (simulating a module)
def analyze(data):
    return {
        "mean": statistics.mean(data),
        "median": statistics.median(data),
        "stdev": statistics.stdev(data),
        "sqrt_sum": math.sqrt(sum(data))
    }

# Custom formatter function (simulating a package module)
def print_table(data_dict):
    print("\nAnalysis Results:")
    print("-" * 30)
    for key, value in data_dict.items():
        print(f"{key.capitalize():<15}: {value:.2f}")

# Main program
def main():
    # Example dataset
    numbers = [4, 8, 15, 16, 23, 42]

    # Analyze the data
    results = analyze(numbers)

    # Print the formatted results
    print_table(results)

if __name__ == "__main__":
    main()
