# AirBnB Clone  Project - The Cnsole

## Description
This project is a simplified version of the AirBnB website,implemented as a command-line interface (CLI) application, developed as part of a learning exercise. It allows users to manage and interact with various objects such as states, cities, users, places, amenities, and reviews.

## Installation

To use this project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the console application by executing `python console.py`.


## Command Interpreter
The command interpreter is a Python script (`console.py`) that provides an interactive interface for managing AirBnB objects. It supports various commands for creating, retrieving, updating, and deleting objects.

## Usage
To start the command interpreter, simply run the `console.py` script using Python 3:

Once the console application is running, you can use various commands to interact with the system:

- `create`: Create a new instance of a specified class.
  Example: `create State`

- `show`: Display information about a specified object.
  Example: `show State 1234-5678-9012`

- `destroy`: Delete a specified object from storage.
  Example: `destroy City 9876-5432-1098`

- `all`: Display all objects or all objects of a specified class.
  Example: `all` or `all State`

- `update`: Update attributes of a specified object.
  Example: `update User 1234-5678-9012 email "example@example.com"`

- `quit`: Exit the command-line interface.

## Project Structure

The project structure is organized as follows:

- `models`: Contains the classes representing different objects in the system.
- `tests`: Contains unit tests for the project.
- `console.py`: The main command-line interface for interacting with the system.
- `README.md`: This file, providing an overview of the project and instructions for use.

## Contributors
- Daniel Godfred Junior (@Ntidaniel)

Contributions are welcome! Please fork the repository and submit a pull request.
