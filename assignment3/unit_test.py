""" Create a function that validates email addresses based on following set of rules:
- Proper email format such as presence of “@”, no space in the address
- Presence of valid email providers such as yahoo, gmail and outlook. Make sure
there are no no disposable email providers such as yopmail.
Write unit tests to validate different email addresses against the rules, including valid and
invalid addresses (Use unittest module). """

import unittest
import re

def validate_email(email):
    """
        Validate an email address based on specific rules.

        Args:
            email (str): Email address to validate.

        Returns:
            bool: True if the email is valid, False otherwise.
        """
        # Check for proper email format
    if not re.match(r'^[\w\.-]+@[\w\.-]+$', email):
        return False

    #Check for valid email providers
    valid_providers = ['yahoo.com', 'gmail.com', 'outlook.com']
    domain = email.split('@')[-1]
    if domain not in valid_providers:
        return False

    #Check for disposal email providers
    disposal_providers = ['yopmail.com']
    if domain in disposal_providers:
        return False

    return True

class TestEmailValidation(unittest.TestCase):
    def test_validate_emails(self):
        self.assertTrue(validate_email('upama@gmail.com'))
        self.assertTrue(validate_email('yt@yahoo.com'))
        self.assertTrue(validate_email('mark.j@outlook.com'))

    def test_invalid_emails(self):
        self.assertFalse(validate_email('inavli.com'))
        self.assertFalse(validate_email('hey@nothing.com'))
        self.assertFalse(validate_email('upama sree@gmail.com'))
        self.assertFalse(validate_email('test@yopmail.com'))


if __name__ == '__main__':
    unittest.main()


""" Design a function that takes a list of numerical data and performs calculations for mean,
median and standard deviation. Write unit tests to verify the correctness of the statistical
calculations for various inputs, including edge cases like an empty list or a list with one
element (Use unittest module. """

import unittest
import statistics

def calculate_statistics(data):
    """
    Calculate mean, median, and standard deviation of numerical data.

    Args:
        data (list): List of numerical data.

    Returns:
        dict: Dictionary containing mean, median, and standard deviation.
    """
    result = {}

    if not data:
        raise ValueError("Input list is empty")

    result['mean'] = sum(data) / len(data)
    result['median'] = statistics.median(data)
    result['std_dev'] = statistics.stdev(data)

    return result


class TestStatisticsCalculation(unittest.TestCase):
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_statistics([])

    def test_single_element(self):
        result = calculate_statistics([5])
        self.assertEqual(result['mean'], 5)
        self.assertEqual(result['median'], 5)
        self.assertEqual(result['std_dev'], 0)

    def test_normal_data(self):
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        result = calculate_statistics(data)
        self.assertEqual(result['mean'], statistics.mean(data))
        self.assertEqual(result['median'], statistics.median(data))
        self.assertEqual(result['std_dev'], statistics.stdev(data))


if __name__ == '__main__':
    unittest.main()
