import pandas as pd
from schema import Schema, And, Use, Optional


class CSVValidator:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)

    def validate(self, rules):
        for column, rule in rules.items():
            if column not in self.data.columns:
                raise ValueError(f"Column '{column}' not found in the CSV.")

            self.data[column] = self.data[column].apply(lambda x: rule.validate(x))


user_rules = {
    'age': And(Use(int), lambda n: 0 < n < 150),
    'gender': And(str, lambda s: s.lower() in ['male', 'female']),
    'salary': And(Use(float), lambda n: n > 0),
}

if __name__ == "__main__":
    file_path = 'text.csv'
    validator = CSVValidator(file_path)
    validator.validate(user_rules)
    print("Validation successful.")
