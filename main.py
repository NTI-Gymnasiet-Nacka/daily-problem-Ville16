class User:
    def __init__(self, name, income):
        self.name = name
        self.income = income
        self.spending_categories = {}
        self.transactions = []
        return None
    
    def set_categories(self, categories):
        self.spending_categories = categories

    def add_transaction(self, amount, category):
        self.transactions.append({'amount': amount, 'category': category})

        # Lower the amount for the category.
        if category in self.spending_categories:
            self.spending_categories[category] -= amount
            if self.spending_categories[category] < 0:
                return f'Du har överskridit din budget för {category}!'
        else:
            return f'Kategori {category} finns inte.'

    def get_total_spent(self):
        return sum([i['amount'] for i in self.transactions])

def main():
    user = User('Ville', 1000,)
    user.set_categories({'Förnödenheter': 500, 'Behov': 200, 'Sparande': 300})

    user.add_transaction(100, 'Behov')
    print(user.spending_categories)

if __name__ == "__main__":
    main()