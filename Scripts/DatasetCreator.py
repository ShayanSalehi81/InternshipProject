import pandas as pd

def create_dataset(dataset_path):
    train_df = pd.read_csv(dataset_path)
    result_df = pd.DataFrame({
        'Context': train_df['Context'],
        'Response': train_df['Response'],
        'Context_Translated': pd.NA,
        'Response_Translated': pd.NA
    })
    result_df.to_csv('Dataset/result.csv', index=False)

if __name__ == '__main__':
    create_dataset(dataset_path='Dataset/train.csv')