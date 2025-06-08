# PROG8850 Assignment 2 - Database Automation & CI/CD

## Student: Twinkle Mishra  - 8894858

---

## Overview

This project automates MySQL database schema changes and simulates a CI/CD pipeline using GitHub Actions. It includes:

- SQL scripts for schema creation and safe updates
- A Python script for executing the SQL changes
- GitHub Actions workflow for deployment automation
- Dockerized MySQL environment with Adminer interface

---

## Project Structure

```
.
├── automate_db.py              # Python script to apply schema & data
├── schema_changes.sql          # Creates and alters 'projects' table
├── add_departments.sql         # Inserts department records
├── up.yml                      # Ansible playbook to start MySQL & Adminer
├── down.yml                    # Ansible playbook to stop services
├── mysql-adminer.yml           # Docker Compose for MySQL + Adminer
├── bin/act                     # ACT binary to test GitHub Actions locally
└── .github/workflows/ci_cd_pipeline.yml  # CI/CD workflow 
```

---

## Setup & Testing

### Start MySQL & Adminer

```bash
ansible-playbook up.yml
```

Access Adminer at: [http://localhost:8080]

---

### Run Automation Script

```bash
python automate_db.py
```

---

### Verify via MySQL CLI

```bash
mysql -u root -h 127.0.0.1 -p
# Password: Secret5555
```

Inside MySQL:
```sql
USE companydb;
SHOW TABLES;
DESCRIBE projects;
DESCRIBE departments;
SELECT * FROM projects;
SELECT * FROM departments;
```

---

### Test GitHub Actions Locally

```bash
bin/act
```

### Push to GitHub

```bash
git add .
git commit -m "Assignment 2 - Complete implementation"
git push origin main
```

---

## CI/CD Pipeline Summary

- Triggers on push or manually
- Builds MySQL client and installs dependencies
- Runs SQL and Python scripts
- Verifies inserts and structure
- Outputs final deployment report

---

## Cleanup

```bash
ansible-playbook down.yml
```

---