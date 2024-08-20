# Introduction

This `README.md` provides instructions on how to use a Python script to automatically update table descriptions in BigQuery by reading data from a CSV file stored in a Cloud Storage bucket.

## How to Use Locally

For testing purposes outside of Cloud Storage, you can use the `local.py` file. Follow these steps to set up and run the script locally:

1. **Create a Virtual Environment:**

   Create a virtual environment to isolate your dependencies.

   ```bash
   python -m venv venv
   ```

2. **Install the Requirements:**

   Install the necessary Python packages listed in the `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```

3. **Set the Environment Variable:**

   Set the environment variable to point to your Google Cloud service account credentials. (If you need to perform tests, request the necessary credentials.)

   ```bash
   $env:GOOGLE_APPLICATION_CREDENTIALS="service_account_key.json"
   ```

4. **Upload Files to the Selected Bucket:**

   Ensure that the relevant CSV files are uploaded to the specified Cloud Storage bucket.

5. **Run the Script:**

   Execute the `local.py` script to update the table descriptions in BigQuery.

   ```bash
   python local.py
   ```

## How to Deploy on Cloud Functions

To deploy the script as a Cloud Function, follow these steps:

1. **Create the Cloud Function:**

   - Choose the 1st generation Cloud Function.
   - Specify the region where you want to deploy.
   - Set the event type to `"On finalize/create"` for files in the selected bucket.
   - Select the bucket that will trigger the function.

2. **Add Environment Variables:**

   Add the necessary environment variables, such as:

   - `tag_template_id`: The ID of the tag template to use.
   - `location`: The location of your data.

3. **Deploy the Script:**

   Deploy the `main.py` file to the Cloud Function. The function will automatically trigger when a file is uploaded to the specified bucket, and it will update the table descriptions in BigQuery accordingly.

## Notes

- **Error Handling:** If there are any issues during the retrieval of policy tags or the updating of table descriptions, errors will be logged for further investigation.
- **Tag Application:** Be cautious when applying the same tag multiple times, as it may result in errors in the logs.

This guide should help you set up, test, and deploy the Python script to update table descriptions in BigQuery effectively.