import logging
import datetime
import json
import os

""" [Factory Design Pattern]
Build a logging system using the Factory Design Pattern.
Create a LoggerFactory class that generates
different types of loggers (e.g., FileLogger,
ConsoleLogger, DatabaseLogger).
Implement methods in each logger to write logs to
their respective destinations.
Show how the Factory Design Pattern helps to decouple
the logging system from the application
and allows for flexible log handling."""
"""
This module contains examples of design patterns in Python.
"""


# Factory Design Pattern
class FileLogger:
    """File Logger"""
    def __init__(self) -> None:
        print("File Logging")

    def logging(self, msg):
        """Logging"""
        return logging.info(f"File Logging {msg} at {datetime.datetime.now()}")


class ConsoleLogger:
    """Console Logger"""
    def __init__(self) -> None:
        print("Console Logging")

    def logging(self, msg):
        """Logging"""
        return logging.warning(f"CLogging{msg}at{datetime.datetime.now()}")


class DatabaseLogger:
    """Database Logger"""
    def __init__(self) -> None:
        print("Database Logging")

    def logging(self, msg):
        """Logging"""
        return logging.info(f"Db Logging {msg} at {datetime.datetime.now()}")


def factory_logger(logger_type: str):
    """Factory Method"""

    loggers = {
        "File": FileLogger,
        "Console": ConsoleLogger,
        "Database": DatabaseLogger
    }
    return loggers[logger_type]()


logging.basicConfig(level=logging.INFO)

MESSAGE = "secret"
file = factory_logger("File")
console_abc = factory_logger("Console")
database = factory_logger("Database")

file.logging(MESSAGE)
console_abc.logging(MESSAGE)
database.logging(MESSAGE)

"""[Builder Design Pattern]
Design a document generator using the Builder Design Pattern.
Create a DocumentBuilder that creates documents of various types (e.g., PDF,
HTML, Plain Text).
Implement the builder methods to format the document content and
structure according to the chosen type.
Demonstrate how the Builder Design Pattern allows for the
creation of different document formats without tightly
coupling the document generation logic."""


class PDFDocument:
    """Pdf Documents."""
    def __init__(self) -> None:
        self.content = ""

    def add_heading(self, heading):
        """Add heading"""
        self.content += f"<h1>{heading}</h1>\n"

    def add_paragraph(self, paragraph):
        """Add paragraph"""
        self.content += f"<p>{paragraph}</p>\n"

    def __str__(self):
        return f"PDF Document:\n{self.content}"


class HTMLDocument:
    """HTML documents."""
    def __init__(self):
        self.content = ""

    def add_heading(self, heading):
        """Adding the heading"""
        self.content += f"<h1>{heading}</h1>\n"

    def add_paragraph(self, paragraph):
        """
        Adding the paragraph
        """
        self.content += f"<p>{paragraph}</p>\n"

    def __str__(self):
        return f"HTML Document:\n{self.content}"


class PlainTextDocument:
    """
        Plain Text.
    """
    def __init__(self):
        self.content = ""

    def add_heading(self, heading):
        """Adding the heading"""
        self.content += f"<h>{heading}</h>"

    def add_paragraph(self, paragraph):
        """Adding the paragraph"""
        self.content += f"<p>{paragraph}</p>"

    def __str__(self):
        return f"Plain Text Document:\n {self.content}"


class DocumentBuilder:
    """
        Document Builder.
    """
    def add_heading(self, heading):
        """Addng the heading"""

    def add_paragraph(self, paragraph):
        """Adding the paragraph"""

    def get_document(self):
        """Get the document"""


class PDFDocumentBuilder(DocumentBuilder):
    """
        PDF Document.
    """
    def __init__(self):
        self.document = PDFDocument()

    def add_heading(self, heading):
        self.document.add_heading(heading)

    def add_paragraph(self, paragraph):
        self.document.add_paragraph(paragraph)

    def get_document(self):
        return self.document


class HTMLDocumentBuilder(DocumentBuilder):
    """
        Html Document.
    """
    def __init__(self):
        self.document = HTMLDocument()

    def add_heading(self, heading):
        self.document.add_heading(heading)

    def add_paragraph(self, paragraph):
        self.document.add_paragraph(paragraph)

    def get_document(self):
        return self.document


class PlainTextDocumentBuilder(DocumentBuilder):
    """
        Plain text Document.
    """
    def __init__(self):
        self.document = PlainTextDocument()

    def add_heading(self, heading):
        self.document.add_heading(heading)

    def add_paragraph(self, paragraph):
        self.document.add_paragraph(paragraph)

    def get_document(self):
        return self.document


class DocumentGenerator:
    """
        Document Generator
    """
    def __init__(self, builder):
        self.builder = builder

    def generate_document(self):
        """Genrate the documents """
        self.builder.add_heading("Sample Document")
        self.builder.add_paragraph("This is the paragraph in the document.")
        self.builder.add_heading("Another Heading")
        self.builder.add_paragraph("Another paragraph")

        return self.builder.get_document()


def main():
    """
        Main Function
    """
    pdf_builder = PDFDocumentBuilder()
    pdf_generator = DocumentGenerator(pdf_builder)
    pdf_document = pdf_generator.generate_document()
    print(pdf_document)

    print("\n")

    html_builder = HTMLDocumentBuilder()
    html_generator = DocumentGenerator(html_builder)
    html_document = html_generator.generate_document()
    print(html_document)

    print("\n")

    plain_text_builder = PlainTextDocumentBuilder()
    plain_text_generator = DocumentGenerator(plain_text_builder)
    plain__text_document = plain_text_generator.generate_document()
    print(plain__text_document)


if __name__ == "__main__":
    main()

"""[Singleton Design Pattern] Implement a configuration
manager using the Singleton Design Pattern.
The configuration manager should read configuration settings from a
file and provide access to these settings throughout the application.
Demonstrate how
the Singleton Design Pattern ensures that there is only one instance of the
configuration manager,
preventing unnecessary multiple reads of the configuration file."""


class ConfigurationManager:
    """Config Manager"""
    __instance = None
    __config_data = None

    def __new__(cls):
        """
            New class
        """
        input_file = "config.json"
        script_dir = os.path.dirname(os.path.abspath(__file__))
        input_file = os.path.join(script_dir, input_file)
        if cls.__instance is None:
            cls.__instance = super(ConfigurationManager, cls).__new__(cls)
            with open(input_file, 'r', encoding='utf-8') as config_file:
                cls.__config_data = json.load(config_file)
        return cls.__instance

    def get_setting(self, section, setting_name):
        """Get Setting."""
        return self.__config_data.get(section, {}).get(setting_name)

    def set_setting(self, section, setting_name, value):
        """
            Set Setting.
        """
        input_file = "config.json"
        script_dir = os.path.dirname(os.path.abspath(__file__))
        input_file = os.path.join(script_dir, input_file)

        if section not in self.__config_data:
            self.__config_data[section] = {}
            self.__config_data[section][setting_name] = value
            with open(input_file, 'w', encoding='utf-8') as config_file:
                json.dump(self.__config_data, config_file, ident=4)


if __name__ == '__main__':
    config_manager1 = ConfigurationManager()
    config_manager2 = ConfigurationManager()

    print(config_manager1 is config_manager2)

    setting1_value = config_manager1.get_setting('AppConfig', 'setting1')
    print(setting1_value)

    config_manager1.set_setting('AppConfig', 'setting1', 'new_value')

    setting1_updated = config_manager2.get_setting('AppConfig', 'setting1')
    print(setting1_updated)
