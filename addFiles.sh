#!/bin/bash

# Number of folders
num_folders=25

# Initialize an empty array
folders=()

# Generate folder names and add them to the array
for ((i=5; i<=$num_folders; i++))
do
    folders+=("day_$i")
done

# File to be added
file="task_"
# fileExample="Exampledata"

# Loop through each folder and add the file
for folder in "${folders[@]}"
do
    # Create the file path
    file_path="$folder/$file${folder: -1}.js"
    # file_path_example="$folder/$fileExample${folder: -1}.txt"
    
    # Add the file to the folder
    echo "" > "$file_path"  # You can replace "Your content" with the actual content of the file
    # echo "" > "$file_path_example"  
    echo "Added $file_path"
done
