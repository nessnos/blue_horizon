#!/bin/bash

export PGPASSWORD="waterize"

DB_NAME="waterdata"
DB_USER="postgres"
DB_HOST="localhost"
DB_PORT="5422"
BACKUP_FILE="waterdata_backup.dump"

psql -U $DB_USER -h $DB_HOST -p $DB_PORT -c "DROP DATABASE IF EXISTS $DB_NAME;"
psql -U $DB_USER -h $DB_HOST -p $DB_PORT -c "CREATE DATABASE $DB_NAME;"
pg_restore -U $DB_USER -h $DB_HOST -p $DB_PORT --clean --create --verbose -d $DB_NAME $BACKUP_FILE

for VIEW in chat_data dashboard_data filters country_stats cleaned_data; do
    psql -U $DB_USER -h $DB_HOST -p $DB_PORT -d $DB_NAME -c "REFRESH MATERIALIZED VIEW $VIEW;"
done
