#!/usr/bin/env python3
import argparse
import csv
import random

def generate_mock():
    users = [f"user{i}" for i in range(1, 11)]
    groups = ["Domain Admins", "Sales", "IT", "Finance", "HR"]
    computers = [f"PC-{i}.domain.local" for i in range(1, 6)]

    with open('users.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['cn', 'samAccountName', 'memberOf', 'enabled'])
        for u in users:
            w.writerow([u, u, random.choice(groups), random.choice(['TRUE', 'FALSE'])])

    with open('groups.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['cn', 'member'])
        for g in groups:
            w.writerow([g, random.choice(users)])

    with open('computers.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['cn', 'operatingSystem', 'enabled'])
        for c in computers:
            w.writerow([c, random.choice(['Windows 10', 'Windows Server 2019']), 'TRUE'])

    print("[*] Mock data generated: users.csv, groups.csv, computers.csv")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mock", action="store_true", help="Generate mock data")
    args = parser.parse_args()
    if args.mock:
        generate_mock()
    else:
        print("Use --mock to generate sample data.")