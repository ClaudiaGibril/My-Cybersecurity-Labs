# Lab 08: Recognition and Geolocation Tools

## Description
In this lab, I explored techniques for obtaining geographic coordinates and network information through two methods: Passive Reconnaissance (IPDrone) and Active Social Engineering (Storm-Breaker).

## Tools Used
1. **IPDrone:** Used to extract geolocation data (ISP, Latitude, Longitude) from an IP address, without direct interaction with the target.

2. **Storm-Breaker:** Social engineering framework for capturing precise location via browser GPS and access to peripherals (camera/microphone).

## Environment Challenges (Troubleshooting)
- **Python Externally Managed Environment:** Overcame the installation block of `pip` on Kali Linux 2026 using the `--break-system-packages` flag to ensure the functionality of the `requests` and `io` libraries.

- **Permissions Configuration:** Applying `chmod +x` to execute Python scripts.

## Lessons Learned
- Difference between IP geolocation accuracy (estimated) vs. GPS (accurate).

- Manipulating protected Python environments on modern operating systems.

- Importance of initial reconnaissance (footprinting) in a penetration test.

## Status
- [x] IPDrone Environment Configured
- [x] Social Engineering Dependencies Installed
