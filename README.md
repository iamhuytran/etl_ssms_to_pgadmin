# SSMS to pgAdmin ETL Data Pipeline - README

This repository contains code for an ETL (Extract, Transform, Load) data pipeline project that facilitates transferring data from SQL Server Management Studio (SSMS) to pgAdmin using Visual Studio Code (VSC) as the development environment.

## Project Overview

The project aims to automate the process of extracting data from SSMS, transforming it if necessary, and loading it into pgAdmin. This pipeline simplifies the movement of data between different database systems, enabling seamless integration and analysis.
![image](https://github.com/iamhuytran/ssms_to_pgadmin_etl/assets/102829980/181bf5a6-48cb-4106-8d3f-0c715f7ec21b)


## Code Overview

The code provided in this repository consists of a single Python script `etl_pipeline.py`. Here's a brief overview of its functionality:

- **`etl_pipeline.py`**: This script contains functions for extraction, transformation, and loading of data.
  - **Extract Function**: Establishes a connection to the SQL Server database using SQLAlchemy, executes an SQL query to extract data from SSMS, and returns the extracted data as a Pandas DataFrame.
  - **Load Function**: Establishes a connection to the PostgreSQL database using SQLAlchemy, saves the DataFrame to the PostgreSQL database in pgAdmin, and handles any errors that occur during the data loading process.

## Prerequisites

Before running the code, ensure you have the following prerequisites installed:

1. **Visual Studio Code**: Download and install Visual Studio Code from [here](https://code.visualstudio.com/).
2. **Python**: Ensure Python is installed on your system. You can download it from [here](https://www.python.org/downloads/).
3. **Required Python Libraries**: Install the necessary Python libraries using pip:
    ```bash
    pip install pandas sqlalchemy
    ```

## Usage


1. **Configure SSMS and pgAdmin**:
    - Ensure you have access to the SQL Server instance in SSMS and the PostgreSQL database in pgAdmin.
    - Modify the connection details within the script `etl_pipeline.py` to match your SSMS and pgAdmin configurations.

2. **Run the ETL Pipeline**:
    - Open `etl_pipeline.py` in Visual Studio Code.
    - Review and modify the script if necessary.
    - Execute the script in Visual Studio Code or via the command line:
        ```bash
        python etl_pipeline.py
        ```

3. **Monitor Execution**:
    - The script will extract data from SSMS, transform it if required, and load it into pgAdmin.
   

