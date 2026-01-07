import statistics

class Statistics:
    def __init__(self):
        self.numbers = []

    def add_number(self):
        number = float(input("Enter number: "))
        self.numbers.append(number)

    def add_value(self, value):
        self.numbers.append(value)

    def display_numbers(self):
        print("Numbers:", " ".join(map(str, self.numbers)))

    def get_max(self):
        return max(self.numbers) if self.numbers else None

    def get_min(self):
        return min(self.numbers) if self.numbers else None

    def get_mean(self):
        return sum(self.numbers) / len(self.numbers) if self.numbers else None

    def get_median(self):
        return statistics.median(self.numbers) if self.numbers else None

    def print_results(self):
        if not self.numbers:
            print("No data available.")
            return
            
        print(f"Minimum: {self.get_min()}")
        print(f"Maximum: {self.get_max()}")
        print(f"Arithmetic Mean: {self.get_mean()}")
        print(f"Median: {self.get_median()}")