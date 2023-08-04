#  [Factory Design Pattern] Build a logging system using the Factory Design Pattern.
# Create a LoggerFactory class that generates different types of loggers (e.g., FileLogger,
# ConsoleLogger, DatabaseLogger). Implement methods in each logger to write logs to
# their respective destinations. Show how the Factory Design Pattern helps to decouple
# the logging system from the application and allows for flexible log handling.


import logging
import datetime

class FileLogger:
    def __init__(self) -> None:
        print("File Logging")

    def logging(self, msg):
        return logging.info(f"File Logging {msg} at {datetime.datetime.now()}")

class ConsoleLogger:
    def __init__(self) -> None:
        print("Console Logging")

    def logging(self, msg):
        return logging.warning(f"Console Logging {msg} at {datetime.datetime.now()}")

class DatabaseLogger:
    def __init__(self) -> None:
        print("Database Logging")

    def logging(self, msg):
        return logging.info(f"Database Logging {msg} at {datetime.datetime.now()}")

def FactoryLogger(logger_type: str):
    """Factory Method"""

    loggers = {
        "File": FileLogger,
        "Console": ConsoleLogger,
        "Database": DatabaseLogger
    }
    return loggers[logger_type]()


logging.basicConfig(level=logging.INFO)

message = "secret"
file = FactoryLogger("File")
console_abc = FactoryLogger("Console")
database = FactoryLogger("Database")

file.logging(message)
console_abc.logging(message)
database.logging(message)

# [Builder Design Pattern] Design a document generator using the Builder Design
# Pattern. Create a DocumentBuilder that creates documents of various types (e.g., PDF,
# HTML, Plain Text). Implement the builder methods to format the document content and
# structure according to the chosen type. Demonstrate how the Builder Design Pattern
# allows for the creation of different document formats without tightly coupling the
# document generation logic.

class PDFDocument:

    def __init__(self) -> None:
        self.content = ""

    def add_heading(self, heading):
        self.content += f"<h1>{heading}</h1>\n"

    def add_paragraph(self, paragraph):
        self.content += f"<p>{paragraph}</p>\n"

    def __str__(self):
        return f"PDF Document:\n{self.content}"

class HTMLDocument:
    def __init__(self):
        self.content = ""

    def add_heading(self, heading):
        self.content += f"<h1>{heading}</h1>\n"

    def add_paragraph(self, paragraph):
        self.content += f"<p>{paragraph}</p>\n"

    def __str__(self):
        return f"HTML Document:\n{self.content}"

class PlainTextDocument:
    def __init__(self):

        self.content = ""

    def add_heading(self, heading):
        self.content += f"<h>{heading}</h>"

    def add_paragraph(self, paragraph):
        self.content += f"<p>{paragraph}</p>"

    def __str__(self):
        return f"Plain Text Document:\n {self.content}"

class DocumentBuilder:

    def add_heading(self, heading):
        pass

    def add_paragraph(self, paragraph):
        pass

    def get_document(self):
        pass

class PDFDocumentBuilder(DocumentBuilder):

    def __init__(self):
        self.document = PDFDocument()

    def add_heading(self, heading):
        self.document.add_heading(heading)

    def add_paragraph(self, paragraph):
        self.document.add_paragraph(paragraph)

    def get_document(self):
        return self.document


class HTMLDocumentBuilder(DocumentBuilder):

    def __init__(self):
        self.document = HTMLDocument()

    def add_heading(self, heading):
        self.document.add_heading(heading)

    def add_paragraph(self, paragraph):
        self.document.add_paragraph(paragraph)

    def get_document(self):
        return self.document

class PlainTextDocumentBuilder(DocumentBuilder):

    def __init__(self):
        self.document = PlainTextDocument()

    def add_heading(self, heading):
        self.document.add_heading(heading)

    def add_paragraph(self, paragraph):
        self.document.add_paragraph(paragraph)

    def get_document(self):
        return self.document

class DocumentGenerator:

    def __init__(self, builder):
        self.builder = builder

    def generate_document(self):
        self.builder.add_heading("Sample Document")
        self.builder.add_paragraph("This is the paragraph in the document.")
        self.builder.add_heading("Another Heading")
        self.builder.add_paragraph("Another paragraph")

        return self.builder.get_document()

def main():

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

#  [Singleton Design Pattern] Implement a configuration manager using the Singleton
# Design Pattern. The configuration manager should read configuration settings from a
# file and provide access to these settings throughout the application. Demonstrate how
# the Singleton Design Pattern ensures that there is only one instance of the
# configuration manager, preventing unnecessary multiple reads of the configuration file.

import json
import os

class ConfigurationManager:
    __instance = None
    __config_data = None

    def __new__(cls):

        input_file = "config.json"
        script_dir = os.path.dirname(os.path.abspath(__file__))
        input_file = os.path.join(script_dir, input_file)
        if cls.__instance is None:
            cls.__instance = super(ConfigurationManager,cls).__new__(cls)
            with open(input_file, 'r') as config_file:
                cls.__config_data = json.load(config_file)
        return cls.__instance

    def get_setting(self, section, setting_name):

        return self.__config_data.get(section, {}).get(setting_name)

    def set_setting(self, section, setting_name, value):
        input_file = "config.json"
        script_dir = os.path.dirname(os.path.abspath(__file__))
        input_file = os.path.join(script_dir, input_file)
        if section not in self.__config_data:
            self.__config_data[section] = {}
            self.__config_data[section][setting_name] = value
            with open(input_file, 'w') as config_file:
                json.dump(self.__config_data, config_file, ident=4)


if __name__ == '__main__':
    config_manager1 = ConfigurationManager()
    config_manager2 = ConfigurationManager()

    print(config_manager1 is config_manager2)

    setting1_value = config_manager1.get_setting('AppConfig', 'setting1')
    print(setting1_value)


    config_manager1.set_setting('AppConfig', 'setting1', 'new_value')


    setting1_updated_value = config_manager2.get_setting('AppConfig', 'setting1')
    print(setting1_updated_value)
