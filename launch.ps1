poetry install

$port = 8000
Get-NetTCPConnection -LocalPort $port | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }

$celeryProcess = Get-Process | Where-Object { $_.Path -like "*celery*" -and $_.CommandLine -like "*-A water worker --loglevel=info*" }
if ($celeryProcess) {
    $celeryProcess | Stop-Process -Force
}

Start-Process -NoNewWindow -Wait -FilePath "poetry" -ArgumentList "run", "celery", "-A water", "worker", "--loglevel=info" | Out-File -FilePath "celery.log" -Append

Start-Process -NoNewWindow -Wait -FilePath "poetry" -ArgumentList "run", "python", "manage.py", "runserver"

Set-Location -Path "webapp"
npm install
npm run dev
