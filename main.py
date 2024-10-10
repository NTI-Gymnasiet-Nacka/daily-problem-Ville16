class User:
    def __init__(self, name):
        """
        Initializes a user with a name, income, and spending categories.
        
        Args:
            name (str): The name of the user.
        """
        self.name = name
        self.income = 0
        self.spending_categories = {}

    def set_income(self, income):
        """
        Sets the user's income.
        
        Args:
            income (float): The user's income.
        """
        self.income = income

    def set_categories(self, categories):
        """
        Sets the budget categories for the user.
        
        Args:
            categories (dict): A dictionary of budget categories and amounts.
        """
        self.spending_categories = categories

    def add_transaction(self, amount, category):
        """
        Adds a transaction to a specific category and adjusts the budget.
        
        Args:
            amount (float): The amount for the transaction.
            category (str): The category for the transaction.

        Returns:
            str: A message indicating whether the transaction was successful or failed.
        """
        if category in self.spending_categories:
            if amount <= self.spending_categories[category]:
                self.spending_categories[category] -= amount
                return f'Transaction completed: {amount} kr for {category}.'
            else:
                return f'You have exceeded your budget for {category}!'
        else:
            return f'Category {category} does not exist.'

    def get_remaining_budget(self):
        """
        Calculates the remaining budget after all transactions.

        Returns:
            float: The remaining budget.
        """
        return self.income - sum(self.spending_categories.values())

    def get_full_budget(self):
        """
        Retrieves the entire budget for the user.

        Returns:
            dict: A dictionary of budget categories and their amounts.
        """
        return self.spending_categories

def main():
    """
    Main function that runs the budget management program.
    
    Provides the user options to create a budget, make transactions,
    view the budget, and exit the program.
    """
    user = User('Ville')
    budget_created = False

    while True:
        selection = input(f'\nHello {user.name}! Welcome to the budget tracker! \nChoose an option:\n'
                          '1. Create your budget\n'
                          '2. Make a transaction\n'
                          '3. View your budget\n'
                          '4. Exit\n')

        if selection == '1':
            try:
                total_income = float(input('What is your income?\n'))
                if total_income <= 0:
                    print('Income must be a positive number.')
                    continue
                
                user.set_income(total_income)
                print(f'Your income has been set to {total_income} kr.')

                # Budget for categories
                saving = float(input('How much do you want to budget for Saving?\n'))
                loan = float(input('How much do you want to budget for Loan?\n'))
                essentials = float(input('How much do you want to budget for Essentials?\n'))
                leisure = float(input('How much do you want to budget for Leisure?\n'))

                total_budgeted = saving + loan + essentials + leisure
                if total_budgeted > total_income:
                    print('The total budget cannot exceed your income! Adjust your amounts and try again.')
                    continue

                user.set_categories({'Saving': saving, 'Loan': loan, 'Essentials': essentials, 'Leisure': leisure})
                budget_created = True
                print('Your budget has been saved!')

            except ValueError:
                print('Please enter valid numbers for the budget.')

        elif selection == '2':
            if not budget_created:
                print('You must create a budget before making transactions.')
                continue

            category = input('Which category would you like to make a transaction for?\n')
            try:
                amount = float(input('How much would you like to transact?\n'))
                message = user.add_transaction(amount, category)
                print(message)
            except ValueError:
                print('Please enter a valid amount for the transaction.')

        elif selection == '3':
            if not budget_created:
                print('You must create a budget before you can view it.')
                continue

            # Display the entire budget
            full_budget = user.get_full_budget()
            print('\nYour budget per category:')
            for category, amount in full_budget.items():
                print(f'{category}: {amount} kr')
            print(f'Total remaining budget: {user.get_remaining_budget()} kr.')

        elif selection == '4':
            print('Exiting...')
            break

        else:
            print('Invalid selection, please try again.')

if __name__ == '__main__':
    main()
