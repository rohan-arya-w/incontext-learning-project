import os
from scripts.prepare_data import prepare_data
from scripts.run_experiment import run_experiment
from scripts.evaluate import evaluate_results

def main():
    print("🔧 Preparing data...")
    prepare_data()

    print("🚀 Running experiment...")
    run_experiment()

    print("📊 Evaluating results...")
    evaluate_results()

if __name__ == "__main__":
    main()