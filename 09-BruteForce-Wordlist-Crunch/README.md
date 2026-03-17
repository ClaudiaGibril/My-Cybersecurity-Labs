# Lab 09: Generating Custom Wordlists with Crunch

## Description
In this lab, I used **Crunch** to create password dictionaries (wordlists) focused on brute-force attacks. The analysis focused on how to generate specific combinations to optimize attack time and disk space.

## Commands Used and Scenarios

### 1. Numerical Dictionary Attack (PINs)
Generating all 4-digit combinations (0000-9999):
`crunch 4 4 0123456789 -o pins_4_digitos.txt`

### 2. Pattern Matching Attack
Scenario: The target password has 8 characters, starts with "Admin" and ends with 3 numbers:
`crunch 8 8 -t Admin%%% -o wordlist_admin.txt`
*Note: The `%` symbol represents numbers in the Crunch pattern.*

## Challenges and Technical Observations
- **Space Management:** Before starting the generation, Crunch informs the final file size. I learned to monitor this to avoid storage exhaustion (Disk Full).

- **Character Optimization:** Instead of using the full charset (`mixalpha-numeric`), I focused on reduced sets based on prior information about the target (Social Engineering).

## Conclusion
Crunch is vital for offline brute-force attacks (such as cracking WPA2 hashes or ZIP files). Creating smaller, more precise wordlists dramatically increases the success rate of a penetration test.
