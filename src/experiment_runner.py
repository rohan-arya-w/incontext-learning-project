from config.settings import CONFIG
from src.models import load_model
from src.preprocessor.preprocessor import load_dataset
from src.prompt_utils import create_prompt, create_test
from src.evaluator import extract_number, evaluate
from sklearn.model_selection import train_test_split

# Load config
model_name = CONFIG["model_name"]
dataset_name = CONFIG["dataset_name"]
num_shots = CONFIG["num_shots"]

# Load resources
df = load_dataset(dataset_name)
train_df, test_df = train_test_split(df, test_size=0.2)
model = load_model(model_name)

# Run experiment on first test row
prompt = create_prompt(train_df, num_shots)
test_input = create_test(test_df.iloc[0])
full_prompt = prompt + "\n" + test_input

# Inference
response = model.query(full_prompt)
prediction = extract_number(response)
actual = test_df.iloc[0]["target"]
error = evaluate(prediction, actual)

print(f"Prediction: {prediction}, Actual: {actual}, Error: {error:.4f}")

