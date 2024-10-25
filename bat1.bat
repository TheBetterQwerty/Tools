# Simple PowerShell script to display a message

# Function to display a greeting
function Show-Greeting {
    param (
        [string]$Name = "User"
    )
    Write-Host "Hello, $Name! Welcome to the PowerShell script."
}

# Call the function
Show-Greeting -Name "YourName"
