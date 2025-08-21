#!/bin/bash

if [ -d "dist" ]; then
    echo "Removing old dist directory"
    rm -rf dist
fi

# Check if a buildenv exists  
if [ -d "buildenv" ]; then
    echo "Buildenv already exists"
    source buildenv/bin/activate
else
    echo "Creating buildenv"
    python3 -m venv buildenv
    source buildenv/bin/activate
    pip3 install build
fi

# Create a buildenv
python3 -m venv buildenv

# Build the Python package
echo "Building Python package"
python3 -m build

if [ $? -ne 0 ]; then
    echo "Python package build failed. Exiting."
    exit 1
fi