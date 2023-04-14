# Title: Server-Side Command Injection Vulnerability in CodeHS

## CVE-ID: N/A

### Affected Products: CodeHS online IDE or any other web application that allows users to execute shell commands on the server.

### Severity: High

### Description:
The Python script provided by the author allows the execution of arbitrary shell commands on the server-side. The script takes input from the user, which is then executed using the subprocess module without any sanitization or validation. As a result, an attacker can inject malicious shell commands as input and execute them on the server-side. This can lead to unauthorized access, data theft, and other malicious activities.

### Impact:
This vulnerability can allow attackers to execute arbitrary shell commands on the server-side, leading to unauthorized access, data theft, and other malicious activities.

### Solution:
To fix this vulnerability, the web application should implement input validation and sanitization to ensure that user input is not executed as shell commands on the server-side. The use of sandboxing and access controls can also be helpful in mitigating this vulnerability.

### Credit:
This vulnerability was discovered and reported by Mac Lawson.

Disclosure Timeline:

Report submitted to CodeHS: 14th April 2023
No response received from CodeHS as of 14th April 2023
