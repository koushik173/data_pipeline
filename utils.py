# Modify functions to accept dbutils as a parameter
def read_data(file_path, dbutils):
    # Step 1: Read data from a file
    data = dbutils.fs.head(file_path)
    return data

def process_data(data):
    # Step 2: Process the data (e.g., convert to uppercase)
    return data.upper()

def save_data(processed_data, output_path, dbutils):
    # Step 3: Save the processed data to a new file
    dbutils.fs.put(output_path, processed_data, overwrite=True)

def pipeline(file_path, output_path, dbutils):
    # Pipeline style: step-by-step execution
    data = read_data(file_path, dbutils)
    processed_data = process_data(data)
    save_data(processed_data, output_path, dbutils)
    print("Pipeline completed successfully!")

def test_():
    print("hello from test")