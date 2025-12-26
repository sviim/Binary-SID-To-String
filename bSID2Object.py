import sys
import struct

## Example: 0x01050000000000051500000027035A185996571BAD3724B801020000
## Example: 01050000000000051500000027035A185996571BAD3724B801020000

def main():
    if len(sys.argv) != 2:
        print(f"[+] Usage: python3 {sys.argv[0]} 'Binary-SID\n'")
        sys.exit(1)

    hex_sid = sys.argv[1]

    if hex_sid.startswith("0x"):
        hex_sid = hex_sid[2:]

    try:
        binary_sid = bytes.fromhex(hex_sid)
    except ValueError:
        print("[-] Invalid hex string. Binary SID must be hexadecimal.")
        sys.exit(1)

    if len(binary_sid) < 8:
        print("[-] Binary SID too short.")
        sys.exit(1)

    revision = binary_sid[0]
    if revision != 1:
        print("[-] Unsupported SID revision.")
        sys.exit(1)

    sb_authorityCount = binary_sid[1]
    id_authority = int.from_bytes(binary_sid[2:8], 'big')

    expected_len = 8 + (sb_authorityCount * 4)
    if len(binary_sid) != expected_len:
        print(f"[-] Invalid SID length. Expected {expected_len} bytes, got {len(binary_sid)}.")
        sys.exit(1)

    sub_authorities = []
    
    for i in range(sb_authorityCount):
        offset = 8 + (i * 4)
        jumps_struct = struct.unpack('<I', binary_sid[offset:offset+4])[0]
        sub_authorities.append(jumps_struct)

    sid_m = f"S-{revision}-{id_authority}"
    for sa in sub_authorities:
        sid_m += f"-{sa}"

    print(f"[+] String SID: {sid_m}")

if __name__ == "__main__":

    main()
