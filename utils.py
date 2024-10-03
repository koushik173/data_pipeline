def read_data(file_path):
    # Step 1: Read data from a file
    with open(file_path, 'r') as file:
        data = file.read()
    return data


def process_data(data):
    # Step 2: Process the data (e.g., convert to uppercase)
    return data.lower()

def test_():
    print("hello from test")

def save_data(processed_data, output_path):
    # Step 3: Save the processed data to a new file
    with open(output_path, 'w') as file:
        file.write(processed_data)



def pipeline(file_path, output_path):
    # Pipeline style: step-by-step execution
    data = read_data(file_path)
    processed_data = process_data(data)
    save_data(processed_data, output_path)
    print("Pipeline completed successfully!")


