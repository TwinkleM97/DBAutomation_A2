#!/usr/bin/env python3
"""
PROG8850 Assignment 2 - Q1: Database Automation Script
Author: Twinkle Mishra
Date: 07-Jun-2025

This script automates the execution of SQL scripts using mysql-connector-python.
It ensures each SQL command is executed successfully and commits changes to the db.
"""

import mysql.connector
import os


def execute_sql_file(cursor, file_path):
    print(f"\n Executing SQL file: {file_path}")
    try:
        with open(file_path, 'r') as file:
            sql_script = file.read()
        statements = [stmt.strip()
                      for stmt in sql_script.split(';') if stmt.strip()]
        for i, statement in enumerate(statements, 1):
            try:
                print(f" Statement {i}/{len(statements)}")
                cursor.execute(statement)

                # Clear any unread result sets
                while cursor.nextset():
                    pass

            except mysql.connector.Error as e:
                print(f" MySQL error in statement {i}: {e}")
    except FileNotFoundError:
        print(f" File not found: {file_path}")
    except Exception as e:
        print(f" Unexpected error while reading {file_path}: {e}")


def main():
    config = {
        'host': os.getenv('DB_HOST', '127.0.0.1'),
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', 'Secret5555'),
        'database': os.getenv('DB_NAME', 'mysql')
    }

    print(" Starting Database Automation")
    print(f" Connecting to: {config['user']}@{config['host']}")

    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        print(" Connected to MySQL successfully")

        # Ensure companydb exists and switch to it
        cursor.execute("CREATE DATABASE IF NOT EXISTS companydb")
        while cursor.nextset():
            pass

        cursor.execute("USE companydb")
        while cursor.nextset():
            pass

        print("Switched to database: companydb")

        # List of SQL files to run
        sql_files = ['schema_changes.sql', 'add_departments.sql']
        for sql_file in sql_files:
            execute_sql_file(cursor, sql_file)

        connection.commit()
        print("\n All SQL files executed and committed successfully")

        # Verify tables
        cursor.execute("SHOW TABLES")
        if cursor.with_rows:
         tables = cursor.fetchall()
         print(f"\n Tables in 'companydb': {[t[0] for t in tables]}")
        else:
         print("\n No tables returned")

    except mysql.connector.Error as e:
        print(f" MySQL Error: {e}")
    except Exception as e:
        print(f" General Error: {e}")
    finally:
        try:
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals() and connection.is_connected():
                connection.close()
                print(" Database connection closed")
        except Exception as cleanup_error:
            print(f" Cleanup Error: {cleanup_error}")


if __name__ == "__main__":
    main()
