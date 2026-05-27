import os
from google.cloud import bigquery

# 1. Provide the exact name of your JSON key file
# Make sure "bigquery-key.json" matches your actual file name exactly!
key_path = "bigquery-key.json" 

if os.path.exists(key_path):
    print(f" Found key file locally at: {os.path.abspath(key_path)}")
    # Explicitly tell Python to use this file path for authentication
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.abspath(key_path)
else:
    print(f"❌ Cannot find '{key_path}' in this folder! Double-check your file name.")

try:
    # 2. Connect using your explicit project ID
    client = bigquery.Client(project="pipeline-assessment-sandbox")
    datasets = list(client.list_datasets())
    
    print("\n✅ Successfully connected! Found datasets:")
    for dataset in datasets:
        print(f" - {dataset.dataset_id}")
        
except Exception as e:
    print("\n❌ Connection failed. Error details:")
    print(e)