# Passwords
Developed a Python-based password-space research tool that generates secure synthetic test strings, calculates theoretical combinations, and exports customizable samples to CSV. Built with secrets, string, and csv, featuring configurable length limits and sample validation.


## Passwords

A Python-based password-space research tool for generating synthetic password samples, calculating theoretical combinations, and exporting test data to CSV.

## Overview

Passwords is a lightweight, command-line Python project designed for password research and educational experiments. It calculates the theoretical number of possible strings within a configurable length range, generates random synthetic test strings, and saves the results in a CSV file for further analysis.

The project uses Python's built-in libraries, requires no third-party dependencies, and is designed to be simple to run and extend.

Important :- This tool generates synthetic test strings. It does not discover passwords that have actually been used, retrieve private credentials, or determine which passwords are associated with real accounts.

## Features
* Theoretical password-space calculation: Calculates the number of possible strings for a given alphabet and length range.
* Secure random generation: Uses Python's secrets module to generate random test strings.
* Configurable character set: Supports lowercase letters, uppercase letters, digits, and selected symbols.
* Variable password lengths: Generates strings within a configurable minimum and maximum length.
* CSV export: Saves generated samples in a structured CSV file.
* Input validation: Checks length ranges, alphabet validity, and sample-count limits.
* No external dependencies: Uses only Python's standard library.
* Research-friendly output: Includes sample IDs and string lengths for analysis.

## Built With

* Language :- Python 3
* Standard libraries :- csv, secrets, string, and pathlib
* Output format :- CSV
* Interface :- Command line

## Project Structure

passwords/
├── passwords.py
├── password_test_samples.csv
└── README.md


The CSV file is generated automatically when the script runs successfully.

## Requirements

* Python 3.8 or later recommended
* A terminal or command prompt
* No third-party Python packages required

Check your Python installation :-

```
python --version
```

On some systems, you may need to use python3 instead of python.

## Getting Started

1. Clone the Repository

```
git clone https://github.com/Abhinav-cloud482/passwords.git
```

2. Navigate to the Project Directory

```
cd passwords
```

3. Run the Script

```
python passwords.py
```

If your system uses python3, run :-

```
python3 passwords.py
```

4. View the Generated CSV

After successful execution, the program creates:

```
password_test_samples.csv
```

Open the file using a text editor, Microsoft Excel, LibreOffice Calc, or another CSV-compatible application.

## Configuration

The project's settings are defined near the beginning of passwords.py.

Variable	Default	Description
MIN_LENGTH	8	Minimum generated string length
MAX_LENGTH	16	Maximum generated string length
SAMPLE_COUNT	1000	Number of synthetic samples to generate
OUTPUT_FILE	password_test_samples.csv	Destination CSV file
MAX_SAMPLES	10000	Maximum allowed samples per run
CHARACTERS	Letters, digits, selected symbols	Alphabet used for generation

## Change the Sample Count

To generate 5,000 samples, change :-

SAMPLE_COUNT = 5_000

## Change the Length Range

To generate strings between 10 and 20 characters long, change :

MIN_LENGTH = 10
MAX_LENGTH = 20

## Change the Output Filename

```
OUTPUT_FILE = Path("research_results.csv")
```


Note: The current implementation overwrites the output file on each successful run rather than appending to existing data.

## How Password-Space Calculation Works

The number of possible strings of a fixed length is calculated using:

𝑁 = 𝐴 ^𝐿

Where :-

𝑁
 is the number of possible strings.
𝐴
 is the number of distinct characters in the alphabet.
𝐿
 is the string length.

For a range of lengths from 
𝑚
 to 
𝑛
, the total number of possible strings is:

𝑁
total
=
∑
𝐿
=
𝑚
𝑛
𝐴
𝐿

The script calculates this total using the calculate_space() function.

For example, if an alphabet contains 10 characters, the number of possible strings of exactly four characters is:

10
4
=
10
,
000

The theoretical total represents the size of the defined search space. It does not mean that the program generates or stores every possible string.

## How Generation Works

The generate_test_string() function uses Python's secrets.choice() to select characters randomly from the configured alphabet.

The script selects a random length between MIN_LENGTH and MAX_LENGTH for each sample, inclusive.

Characters may repeat, and different samples may occasionally be identical. The program does not enumerate the entire theoretical space or guarantee unique output.

## CSV Output Format

The generated CSV contains three columns :-

Column	Description
sample_id	Sequential identifier for each generated sample
length	Number of characters in the generated string
test_string	Generated synthetic test string

Example structure:

sample_id,length,test_string
1,12,ExampleValue1
2,8,Example2
3,16,ExampleTestValue


The rows above are illustrative examples, not actual generated output.

The CSV uses UTF-8 encoding and a header row, making it convenient to import into common data-analysis tools.

Privacy note: Generated strings are synthetic, but they may coincidentally match a real password. Treat exported datasets appropriately, especially if sharing them publicly.

## Code Architecture

The script is organized into four main functions.

calculate_space(alphabet_size, min_length, max_length)

Calculates the total number of possible strings for the specified alphabet size and length range. It validates the alphabet size and length bounds.

generate_test_string(length, alphabet)

Generates one random synthetic string of the requested length using the supplied alphabet.

export_samples(count, min_length, max_length, alphabet, output_file)

Validates the generation parameters, creates the CSV file, writes its header, generates the requested samples, and reports the output location.

main()

Coordinates the workflow:

Determines the alphabet size.
Calculates the theoretical search-space size.
Displays the configuration and combination count.
Generates the samples.
Exports them to CSV.

The if __name__ == "__main__": guard allows the script to be imported as a module without automatically executing the main workflow.

## Limitations

* The program generates random samples rather than enumerating all possible strings.
* It cannot identify which strings have been used as real passwords.
* It does not retrieve credentials from websites, services, databases, or user accounts.
* The current implementation does not guarantee unique samples.
* Large theoretical combination counts are mathematical results, not practical generation targets.
* The CSV export is not encrypted.
* The current implementation does not provide a command-line argument parser; configuration is changed directly in the source file.
* The character set is customizable, but the script does not enforce specific password-complexity rules, such as requiring at least one digit or symbol in every sample.

## Security and Responsible Use

This project is intended for educational use, password-space research, synthetic test-data generation, and authorized security testing.

* Do not use generated samples to attempt unauthorized access to accounts or systems.
* Do not collect, publish, or distribute real people's private credentials.
* Do not treat generated strings as a database of known or previously used passwords.
* Do not store real account passwords in plaintext CSV files.
* Use synthetic data and systems you own or are explicitly authorized to test.

The secrets module provides cryptographically strong random selection, but this research script is not a password manager or an authentication-testing framework.

## Future Improvements

Potential enhancements include :-

* Command-line arguments for configurable length, sample count, and output path.
* Progress reporting for larger experiments.
* Duplicate detection and uniqueness statistics.
* Export metadata, including the alphabet size and selected length range.
* Automated unit tests and validation tests.
* Benchmarking generation speed and output size.
* Additional character-set profiles.
* Streaming CSV export for memory-efficient processing.
* Optional analysis of authorized, appropriately sourced password research datasets.

## Contributing

Contributions, suggestions, and bug reports are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test your changes locally.
5. Open a pull request describing the improvement.

Please keep contributions focused on responsible password research, secure software development, and reproducible experiments.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

Abhinav Dixit

GitHub: @Abhinav-cloud482
