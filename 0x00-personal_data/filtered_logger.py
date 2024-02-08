#!/usr/bin/env python3
"""
Module for log filtering using regex
"""

import re

def filter_datum(fields: List[str], redaction: str,
                message: str, separator: str) -> str:
    """ Return: the log message obfuscated """
    return(re.sub(rf"({'|'.join(fields)})=.*?{separator}",
           rf"\1={redaction}{separator}", message))
