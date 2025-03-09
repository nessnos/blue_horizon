$env:PGPASSWORD = "waterize"
poetry install

$port = 8000
Get-NetTCPConnection -LocalPort $port | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }

$DB_NAME = "waterdata"
$DB_USER = "postgres"
$DB_HOST = "localhost"
$DB_PORT = "5422"
$BACKUP_FILE = "waterdata_backup.dump"

psql -U $DB_USER -h $DB_HOST -p $DB_PORT -c "DROP DATABASE IF EXISTS $DB_NAME;"
psql -U $DB_USER -h $DB_HOST -p $DB_PORT -c "CREATE DATABASE $DB_NAME;"
pg_restore -U $DB_USER -h $DB_HOST -p $DB_PORT --clean --create --verbose -d $DB_NAME $BACKUP_FILE

psql -U postgres -h $DB_HOST -p $DB_PORT -d $DB_NAME -c "REFRESH MATERIALIZED VIEW chat_data;"
psql -U postgres -h $DB_HOST -p $DB_PORT -d $DB_NAME -c "REFRESH MATERIALIZED VIEW dashboard_data;"
psql -U postgres -h $DB_HOST -p $DB_PORT -d $DB_NAME -c "REFRESH MATERIALIZED VIEW filters;"
psql -U postgres -h $DB_HOST -p $DB_PORT -d $DB_NAME -c "REFRESH MATERIALIZED VIEW country_stats;"
psql -U postgres -h $DB_HOST -p $DB_PORT -d $DB_NAME -c "REFRESH MATERIALIZED VIEW cleaned_data;"

$celeryProcess = Get-Process | Where-Object { $_.Path -like "*celery*" -and $_.CommandLine -like "*-A water worker --loglevel=info*" }
if ($celeryProcess) {
    $celeryProcess | Stop-Process -Force
}

Start-Process -NoNewWindow -FilePath "poetry" -ArgumentList "run", "celery", "-A water", "worker", "--loglevel=info" | Out-File -FilePath "celery.log" -Append
Start-Process -NoNewWindow -FilePath "poetry" -ArgumentList "run", "python", "manage.py", "runserver"

Set-Location -Path "webapp"
npm install
npm run dev
