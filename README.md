# Binary-SID-To-String

A simple Python tool to parse and convert Windows binary SIDs into their standard string representation (S-1-…).

This utility is useful for Active Directory analysis, forensics, pentesting, and security research, where SIDs often appear in binary form (LDAP attributes, registry, memory dumps, etc.).

Features

- Parses raw binary SID structures
- Supports hexadecimal input with or without 0x
- Validates SID length and structure
- Outputs a standard Windows SID string
- Pure Python (no external dependencies)
- Binary SID obtained from MSSQL `SUSER_SID()`

Installation
```
git clone https://github.com/sviim/Binary-SID-To-String
cd Binary-SID-To-String
```

Usage
```
python3 bSID2Object.py "0x01050000000000051500000027035A185996571BAD3724B801020000" // Without 0x if it's the case

Output:
S-1-5-21-4089195535-461858384-3001900321-513
```
