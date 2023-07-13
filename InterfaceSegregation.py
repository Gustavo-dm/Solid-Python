from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print_document(self):
        pass


class Faxable(ABC):
    @abstractmethod
    def send_fax(self):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass


class AllInOnePrinter(Printable, Faxable, Scanner):
    def print_document(self):
        print("Printing document...")

    def send_fax(self):
        print("Sending fax...")

    def scan_document(self):
        print("Scanning document...")


class FaxMachine(Faxable):
    def send_fax(self):
        print("Sending fax...")


class SimplePrinter(Printable):
    def print_document(self):
        print("Printing document...")
