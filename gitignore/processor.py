import json
import sys
import os
import switch 

def process_geo(json_file):
    with open(json_file) as f:
        data = json.load(f)
        print(f"Country: {data['countryName']}")
        print(f"ISP: {data['isp']}")  # Integrasi data ISP

if __name__ == "__main__":
    process_geo(sys.argv[1])

<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $target = escapeshellarg($_POST['target']);
    $output = shell_exec("./connector.sh $target");
    header("Location: results.php?target=$target");
}
?>
<form method="POST">
    <input type="text" name="target" placeholder="Domain/IP">
    <button>Analyze</button>
</form>

*.log
.env
__pycache__
venv
echo"("reports/*")"
}
    {!reports/.gitkeep
}

import os
import sys
import requests
import network switch
import switch 

def toggle_port(port, state):
    requests.post(
        "https://switch-api/port",
        json={"port": port, "state": state},
        auth=("admin", "password")
    )
