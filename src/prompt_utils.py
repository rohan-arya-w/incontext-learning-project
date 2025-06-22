def create_prompt(df, num_examples=5):
    prompt = "Predict the target based on features.\n\n"
    for i in range(num_examples):
        row = df.iloc[i]
        features = ", ".join([f"{k}: {row[k]}" for k in df.columns if k != 'target'])
        prompt += f"Input: {features} => Output: {row['target']}\n"
    return prompt

def create_test(row):
    features = ", ".join([f"{k}: {row[k]}" for k in row.index if k != 'target'])
    return f"Input: {features} => Output:"