# Enable debug output
$DebugPreference = 'Continue'

# Define the path pattern for config files and exclude metaconfig files
$pattern = '*ports.json'
$excludePattern = 'metaconfig\.json'

# Initialize an empty array to hold the merged content
$mergedContent = @()

# Get all matching files recursively, excluding excluded ones
$files = Get-ChildItem -Path .\ -Filter $pattern -Recurse # -Exclude $excludePattern

# Debug print for the files found
Write-Debug "Found $($files.Count) files matching the pattern '$pattern'"

foreach ($file in $files) {
    # Debug print for processing each file
    Write-Debug "Processing file: $($file.FullName)"

    # Read the content of the file and convert it to an object
    $content = Get-Content $file.FullName | ConvertFrom-Json

    # Add the converted object to the merged content array
    $mergedContent += $content
}

# Convert the merged content array back to JSON format
$mergedJson = $mergedContent | ConvertTo-Json -Depth 100

# Debug print for the merged JSON content
# Write-Debug "Merged JSON content:"
# $mergedJson | Format-Table -AutoSize

# Save the merged JSON to a file
$mergedJson | Set-Content -Path './merged.json' -Encoding utf8

# Disable debug output
$DebugPreference = 'SilentlyContinue'
