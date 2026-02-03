# Lab 07: C2 Framework Configuration for Android (AhMyth)

## Description
In this lab, I explored the AhMyth tool, a Remote Administration Tool (RAT) focused on Android devices. The objective was to configure the server environment (C2) and understand the process of generating malicious artifacts (.apk).

## Technical Challenges and Troubleshooting
During the installation in a modern Linux environment (Kali 2026), the following problems were encountered and resolved:

- **Dependency Resolution:** Correction of 404 errors in `npm` through synchronization of system repositories.

- **Directory Structure:** Identification of the server core in the `AhMyth-Server` subfolder.

- **Sandbox Permissions:** Resolution of the Electron fatal error using the `--no-sandbox` flag.

## Results
- **C2 Server:** Configured and operating successfully on port `42474`.

- **Builder:** The APK compilation module showed incompatibility with the tool's legacy libraries, a common scenario in discontinued open-source tools.

## Conclusion
The lab demonstrated the importance of dependency management (Node.js/Java) and how to configure a listener to receive reverse connections from mobile devices.
