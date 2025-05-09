import json
import os
from datetime import datetime
import matplotlib.pyplot as plt
from colorama import init, Fore, Style
from typing import List, Dict

# Initialize colorama

init(autoreset=True)

class ExpenseTracker:
    def __init__(self, data_file: str = "expenses.json"):
        """Initialize the ExpenseTracker with a data file."""
        self.data_file = data_file
        self.categories = ["Food", "Transport", "Entertainment", "Utilities", "Other"]
        self.data = self.load_data()

    def load_data(self) -> Dict:
        """Load data from JSON file or create a new one if it doesn't exist."""
        if os.path.exists(self.data_file):
            try:
                with open (self.data_file, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print(Fore.RED + "Error: Corrupted data file. Starting fresh." + Style.RESET_ALL)
        return {"income": 0.0, "expenses": [], "balance": 0.0}
    
    def save_data(self) -> None:
        """Save data to JSON file."""
        with open(self.data_file, "w") as file:
            json.dump(self.data, file, indent=4)

    def add_income(self, amount: float) -> None:
        """Add income and update balance."""
        try:
            amount = float(amount)
            if amount < 0:
                raise ValueError("Income cannot be negative.")
            self.data["income"] += amount
            self.data["balance"] += amount
            self.save_data()
            print(Fore.GREEN + f"Added ${amount: .2f} to income. New balance: ${self.data['balance']: .2f}" + Style.RESET_ALL)
        except ValueError as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
    
    def add_expense(self, amount: float, category: str, description: str = "") -> None:
        """Add an expense and update balance."""
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Expense must be positive.")
            if category not in self.categories:
                raise ValueError(f"Invalid category. Choose from: {', '.join(self.categories)}")
            expense = {
                "amount": amount,
                "category": category,
                "description": description,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            self.data["expenses"].append(expense)
            self.data["balance"] -= amount
            self.save_data()
            print(Fore.GREEN + f"Added expense: ${amount: .2f} in {category}. New balance: ${self.data['balance']: .2f}" + Style.RESET_ALL)
        except ValueError as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def show_summary(self) -> None:
        """Display a financial summary."""
        print(Style.BRIGHT + "\n=== Financial Summary ===" + Style.RESET_ALL)
        print(Fore.CYAN + f"Total Income: ${self.data['income']: .2f}" + Style.RESET_ALL)
        total_expenses = sum(expense["amount"] for expense in self.data["expenses"])
        print(Fore.CYAN + f"Total Expenses: ${total_expenses: .2f}" + Style.RESET_ALL)
        print(Fore.CYAN + f"Current Balance: ${self.data['balance']: .2f}" + Style.RESET_ALL)
        print("\nExpenses by Category:")
        for category in self.categories:
            category_total = sum(expense["amount"] for expense in self.data["expenses"] if expense["category"] == category)
            if category_total > 0:
                print(Fore.YELLOW + f"{category}: ${category_total: .2f}" + Style.RESET_ALL)

    def plot_expenses(self) -> None:
        """Generate a pie chart of expenses by category."""
        category_totals = {category: 0.0 for category in self.categories}
        for expense in self.data["expenses"]:
            category_totals[expense["category"]] += expense["amount"]

        labels = [category for category, total in category_totals.items() if total > 0]
        sizes = [total for total in category_totals.values() if total > 0]
        if not sizes:
            print(Fore.RED + "No expenses to plot." + Style.RESET_ALL)
            return
        
        plt.figure(figsize=(8, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
        plt.title("Expenses by Category")
        plt.savefig("expenses_pie_chart.png")
        print(Fore.GREEN + "Pie chart saved as 'expenses_pie_chart.png'." + Style.RESET_ALL)

def main():
    tracker = ExpenseTracker()
    while True:
         print(Style.BRIGHT + "\n=== Personal Expense Tracker ===" + Style.RESET_ALL)
         print("1. Add Income")
         print("2. Add Expense")
         print("3. Show Summary")
         print("4. Plot Expenses")
         print("5. Exit")
         choice = input(Fore.CYAN + "Seflect an option: " + Style.RESET_ALL)

         if choice == "1":
            amount = input("Enter income amount: ")
            tracker.add_income(amount)
         elif choice == "2":
            print("Categories: " + ", ".join(tracker.categories))
            category = input("Enter expense category: ").capitalize()
            amount = input("Enter expense amount: ")
            description = input("Enter expense description (optional): ")
            tracker.add_expense(amount, category, description)
         elif choice == "3":
            tracker.show_summary()
         elif choice == "4":
            tracker.plot_expenses()
         elif choice == "5":
            print(Fore.GREEN + "Thank you for using the expense Tracker!" + Style.RESET_ALL)
            break
         else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

if __name__ == "__main__":
    main()           
        



