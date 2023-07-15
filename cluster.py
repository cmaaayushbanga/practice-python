import os

def clear_folder_clutter(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    # Create a dictionary to store the count for each file extension
    count_dict = {}
    
    # Iterate over each file in the folder
    for file in files:
        # Check if the item is a file (not a folder)
        if os.path.isfile(os.path.join(folder_path, file)):
            # Get the file extension
            _, extension = os.path.splitext(file)
            
            # Increment the count for the extension in the dictionary
            count_dict[extension] = count_dict.get(extension, 0) + 1
            
            # Generate the new file name with the count and extension
            new_name = str(count_dict[extension]) + extension
            
            # Rename the file
            os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))

# Example usage
folder_path = "D:\coding\python"
clear_folder_clutter(folder_path)
