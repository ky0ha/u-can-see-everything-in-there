import pandas as pd

origin_data = pd.read_csv(r"test.csv")
print(f'origin data is:\n{origin_data}')
multiply_data = origin_data * 2
print(f'the origin data after multiply by 2 is:\n{multiply_data}')
multiply_data.to_csv("test_with_multiply.csv", index=False)
print("and then, the multiply data has been saved as a new csv file named 'test_with_multiply.csv'")