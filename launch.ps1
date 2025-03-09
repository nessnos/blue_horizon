poetry install

pg_restore -U postgres -h db -p 5422 --clean --create -d waterdata waterdata_backup.dump

$celeryProcess = Get-Process | Where-Object { $_.CommandLine -like "*celery -A water worker*" }
if ($celeryProcess) {
    Stop-Process -Id $celeryProcess.Id
}

Start-Process "poetry" "run celery -A water worker --loglevel=info" -RedirectStandardOutput "celery.log" -RedirectStandardError "celery.log" -NoNewWindow -WindowStyle Hidden

Start-Process "poetry" "run manage.py runserver" -NoNewWindow -WindowStyle Hidden

Set-Location -Path "webapp"
npm install

npm run dev
