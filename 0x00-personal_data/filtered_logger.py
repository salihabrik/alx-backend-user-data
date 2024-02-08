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
    

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields