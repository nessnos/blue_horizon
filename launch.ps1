poetry install

$port = 8000
$connection = Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue

Write-Host "Checking if port $port is in use..."
if ($connection) {
    Write-Host "Connection found on port $port. Stopping process..."
    $connection | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }
} 
else {
    Write-Host "No connection found on port $port."
}

Write-Host "Checking for running Celery workers..."
$celeryProcess = Get-Process | Where-Object { $_.Path -like "*celery*" -and $_.CommandLine -like "*-A water worker --loglevel=info*" }
if ($celeryProcess) {
    Write-Host "Stopping celery process..."
    $celeryProcess | Stop-Process -Force
}
else {
    Write-Host "No celery process found."
}

Write-Host "Starting Celery worker..."
Start-Process -NoNewWindow -FilePath "poetry" -ArgumentList "run", "celery", "-A water", "worker", "--loglevel=info" | Out-File -FilePath "celery.log" -Append

Write-Host "Starting Django development server..."
Start-Process -NoNewWindow -FilePath "poetry" -ArgumentList "run", "python", "manage.py", "runserver"

Write-Host "Installing and running the webapp..."
Set-Location -Path "webapp"
npm install
npm run dev
