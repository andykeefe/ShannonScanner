# ShannonScanner: an open-source tool for cryptographic inventory, compliance, and auditing.


ShannonScanner searches through source code and extracts information about any cryptographic algorithms, hash functions, and libraries. It is useful in several cases:

1. Constructing a cryptographic inventory for security awareness

2. Auditing application source code to ensure preliminary FIPS compliance

3. Remediating instances of deprecated or lackluster algorithm usage.


Cryptographic algorithms are found in all sorts of software, not just security-focused applications. Therefore, it's useful to have an application to parse out where cryptographic materials are used in source code. 

## Installation

I'd highly recommend using this application in a virtual environment, especially since pip installed packages are known to cause issues on some distributions of Linux.

The first thing you're going to want to do is install packages "exrex" and "pyahocorasick" using pip.

        pip install exrex pyahocorasick

Confirm they're installed with

        pip list

Then, to actually get ShannonScanner, clone this repository using git (make sure you have git installed).

        git clone https://github.com/andykeefe/ShannonScanner.git

## Usage 

### Scan for inventory

        python cryptoscan.py -s /path/to/source_code
or  

        python3 cryptoscan.py -s /path/to/source_code


This is the general scan. It collects all instances of cryptographic algorithms, libraries, and hash functions. 

The output is sent to the **tests** directory as **{source code name}_cryptoscan.txt** and looks like:

        Location: path/to/file/with/crypto 
            Symmetric algorithms:
                - AES 
                - RC4
            Hash functions:
                - SHA2
                - MD5
            Modes of operation:
                - CBC 
                - GCM
                - ECB
            Digital Signatures:
                - RSA
                - ECDSA

### FIPS 140 compliance check

        python cryptoscan.py -c /path/to/source_code

or  

        python3 cryptoscan.py -c /path/to/source_code



This the compliance check function. It conducts a typical scan but outputs only non-compliant cryptographic materials.

The output is sent to the **tests** directory as **{source code name}_compliance.txt** and looks like:

        ***

        NONCOMPLIANT ALGORITHM: RC4 
            - REASON: *reasons why algorithm is non-compliant*
                - Has never been FIPS compliant
            - COMPLIANCE RECOMMENDATION: Use AES for FIPS approval.
            - AFFECTED FILES:
                - /path/where/non_compliant/appears/1
                - /path/where/non_compliant/appears/2

        ***

### Recommendation for cryptographic improvement

        python cryptoscan.py -r /path/to/source_code

or 

        python3 cryptoscan.py -r /path/to/source_code

The output of this argument is sent to the **tests** directory as **{source code name}_recommendations.txt** and looks like:

This argument will give recommendations not necessarily based on FIPS 140 compliance, and will give references to academic papers about the found algorithm.

For example, ECB mode is compliant with FIPS. However, best practices dictate that ECB should not be used because it is highly deterministic (see Tux the Penguin encrypted in ECB for a good example).
Therefore, it is recommended that ECB not be used. 

A similar idea occurs with CBC mode, which is FIPS compliant, but often not recommended for use because of potential padding oracle attacks.


        NONRECOMMENDED CRYPTOGRAPHIC MATERIAL: ECB 
          - Why ECB should not be used: Highly deterministic blah blah blah
          - RECOMMENDATION: Use Galois/Counter Mode (GCM)
          - RECOMMENDATION REASONING: Authenticated encryption blah blah blah
            - Parallelizable blah blah
            - Blah blah blah
          - REFERENCE:
            - Book chapter
            - GCM standard
            - blah blah
          - AFFECTED FILES:
            - /path/to/affected_file/1
            - /path/to/affected_file/2

### Adding your own regular expressions

If there's an algorithm, library, mode of operation, or some other category of cryptography-related operations you'd like to add, the first thing you should do is find a regular expression that captures what you think will encompass as many probable strings as possible. You should then test this regex in the dummy reverse_regex.py program, which is in utils/dummy/reverse_regex.py. You should see the possible matching strings in your terminal output.

Once you've settled on the regex, add it to the corresponding file in crypto/exp/$category$.py.

If you wish to see more categories added, i.e., RNGs or MAC functions, reach out to me and I will see if I can develop a solution.

## Etymology

The name ShannonScanner in honor of Claude Shannon, the father of Information Theory whose sparse contributions to studying cryptography and secrecy were incredibly influential. For a good book on Claude Shannon, check out **_A Mind at Play: How Claude Shannon Invented the Information Age_** by Jimmy Soni and Rob Goodman. 
