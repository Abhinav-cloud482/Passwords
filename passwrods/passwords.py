
import csv
import secrets
import string
from pathlib import Path

# Research configuration
MIN_LENGTH = 8
MAX_LENGTH = 16
SAMPLE_COUNT = 1_000
OUTPUT_FILE = Path("password_test_samples.csv")
MAX_SAMPLES = 10_000

# Selected symbols avoid spreadsheet formula-prefix characters.
CHARACTERS = (
    string.ascii_lowercase
    + string.ascii_uppercase
    + string.digits
    + "!#$%&*?"
)


def calculate_space(alphabet_size, min_length, max_length):
    """Count all possible strings within the length range."""
    if alphabet_size < 1:
        raise ValueError("Alphabet must not be empty.")
    if min_length < 1 or max_length < min_length:
        raise ValueError("Invalid length range.")

    return sum(
        alphabet_size ** length
        for length in range(min_length, max_length + 1)
    )


def generate_test_string(length, alphabet):
    """Generate a random synthetic test string."""
    return "".join(
        secrets.choice(alphabet)
        for _ in range(length)
    )


def export_samples(count, min_length, max_length,
                   alphabet, output_file):
    """Generate a bounded sample and save it as CSV."""
    if not 1 <= count <= MAX_SAMPLES:
        raise ValueError(
            f"Sample count must be between 1 and {MAX_SAMPLES}."
        )

    if min_length < 1 or max_length < min_length:
        raise ValueError("Invalid length range.")

    if not alphabet:
        raise ValueError("Alphabet must not be empty.")

    with output_file.open(
        "w", newline="", encoding="utf-8"
    ) as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=["sample_id", "length", "test_string"]
        )
        writer.writeheader()

        for sample_id in range(1, count + 1):
            length = secrets.randbelow(
                max_length - min_length + 1
            ) + min_length

            test_string = generate_test_string(
                length, alphabet
            )

            writer.writerow({
                "sample_id": sample_id,
                "length": length,
                "test_string": test_string,
            })

    print(f"Saved {count:,} samples to {output_file}")


def main():
    alphabet_size = len(CHARACTERS)

    total = calculate_space(
        alphabet_size, MIN_LENGTH, MAX_LENGTH
    )

    print("Password-space research")
    print("-----------------------")
    print(f"Alphabet size: {alphabet_size}")
    print(f"Minimum length: {MIN_LENGTH}")
    print(f"Maximum length: {MAX_LENGTH}")
    print(f"Theoretical combinations: {total:,}")
    print(f"Requested sample count: {SAMPLE_COUNT:,}")

    export_samples(
        SAMPLE_COUNT,
        MIN_LENGTH,
        MAX_LENGTH,
        CHARACTERS,
        OUTPUT_FILE,
    )


if __name__ == "__main__":
    main()
