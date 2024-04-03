
SSMS to pgAdmin ETL Data Pipeline - README
This repository contains code for an ETL (Extract, Transform, Load) data pipeline project that facilitates transferring data from SQL Server Management Studio (SSMS) to pgAdmin using Visual Studio Code (VSC) as the development environment.

Project Overview
The project focuses on automating the process of extracting data from SSMS, transforming it if necessary, and loading it into pgAdmin. This pipeline simplifies the movement of data between different database systems, enabling seamless integration and analysis.

Code Structure
etl_pipeline.py: This Python script orchestrates the entire ETL process. It includes functions for extraction, transformation, and loading of data.

config.json: This JSON file stores configuration parameters such as database connection details. Modify this file according to your database setup.

Prerequisites
Before running the code, ensure you have the following prerequisites installed:

Visual Studio Code: Download and install Visual Studio Code from here.
Python: Ensure Python is installed on your system. You can download it from here.
Required Python Libraries: Install the necessary Python libraries using pip:
bash
Copy code
pip install pandas sqlalchemy
Usage
Clone the Repository: Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/iamhuytran/ssms_to_pgadmin_etl.git
Configure SSMS and pgAdmin:

Ensure you have access to the SQL Server instance in SSMS and the PostgreSQL database in pgAdmin.
Modify the connection details in the config.json file to match your SSMS and pgAdmin configurations.
Run the ETL Pipeline:

Open etl_pipeline.py in Visual Studio Code.
Review and modify the script if necessary.
Execute the script in Visual Studio Code or via the command line:
bash
Copy code
python etl_pipeline.py
Monitor Execution:

The script will extract data from SSMS, transform it if required, and load it into pgAdmin.
Monitor the script execution for any errors or warnings.
