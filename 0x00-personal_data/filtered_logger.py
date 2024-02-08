#!/usr/bin/env python3
"""
Module for log filtering using regex
"""

import re

def filter_datum(fields, redaction, message, separator):

   """
    Obfuscate log message based on specified fields
    Returns:
        str: Obfuscated log message
    """
    regex = '|'.join(fields)
    return re.sub(f'(?<=\\b{regex}=)[^{separator}]+', redaction, message)
