ETL Data Pipeline between SSMS and pgAdmin using Visual Studio Code
This project demonstrates the development and implementation of an ETL (Extract, Transform, Load) data pipeline between SQL Server Management Studio (SSMS) and pgAdmin using Visual Studio Code. The pipeline extracts data from SSMS, transforms it, and loads it into pgAdmin for further analysis or storage.

Prerequisites
Before using this project, ensure you have the following prerequisites installed:

Visual Studio Code: Download and install Visual Studio Code from here.
Python: Ensure Python is installed on your system. You can download it from here.
Required Python Libraries: Install the necessary Python libraries using pip:
bash
Copy code
pip install pandas sqlalchemy pyodbc psycopg2
Setup
Clone the Repository: Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/ssms-to-pgadmin-etl.git
Configure SSMS and pgAdmin:

Ensure you have access to the SQL Server instance in SSMS and the PostgreSQL database in pgAdmin.
Modify the connection details in the Python script (etl_pipeline.py) to match your SSMS and pgAdmin configurations.
Usage
Run the ETL Pipeline:

Open etl_pipeline.py in Visual Studio Code.
Review and modify the script if necessary.
Execute the script in Visual Studio Code or via the command line:
bash
Copy code
python etl_pipeline.py
Monitor Execution:

The script will extract data from SSMS, transform it, and load it into pgAdmin.
Monitor the script execution for any errors or warnings.
Script Overview
Extract Function:

Establishes a connection to the SQL Server database using SQLAlchemy.
Executes an SQL query to extract data from SSMS.
Returns the extracted data as a Pandas DataFrame.
Load Function:

Establishes a connection to the PostgreSQL database using SQLAlchemy.
Saves the DataFrame to the PostgreSQL database in pgAdmin.
