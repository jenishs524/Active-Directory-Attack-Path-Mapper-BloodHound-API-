📁 Active Directory Attack Path Mapper (BloodHound API)

Description
Extracts Active Directory structure (users, groups, computers) via LDAP queries and generates CSV files compatible with BloodHound. Includes a mock data generator for demonstration.

Key Features

    Queries LDAP for AD objects (if credentials provided).

    Generates users.csv, groups.csv, computers.csv.

    Mock mode creates fake data to visualise attack paths.

    Output can be imported into BloodHound (Neo4j).

Technologies

    Python, ldap3, csv, random.

Prerequisites

    Python 3, optionally a real AD environment for live queries.

Installation
bash

pip install ldap3

Usage
bash

# Generate mock data
python ad_mapper.py --mock

# Real LDAP (placeholder – extend the script)
python ad_mapper.py --ldap-server xxx.xxx.x.x(IP) --username admin --password pass

Sample Output
text

[*] Mock data generated: users.csv, groups.csv, computers.csv

Notes

    Install BloodHound and Neo4j to visualise attack paths.

    Use SharpHound in real environments to collect AD data.
