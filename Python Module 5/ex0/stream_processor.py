from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """Abstract base class for all data processors."""

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process input data and return a result string."""

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate whether the input data is supported."""

    def format_output(self, result: str) -> str:
        """Format the processor output."""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Processor for numeric list data."""

    def validate(self, data: Any) -> bool:
        """Check that data is a non-empty numeric list."""
        if not isinstance(data, list) or len(data) == 0:
            return False
        return all(isinstance(i, (int, float)) for i in data)

    def process(self, data: Any) -> str:
        """Process numeric data and return summary statistics."""
        if not self.validate(data):
            raise ValueError("Invalid numeric data")

        total: float = sum(data)
        count: int = len(data)
        avg: float = total / count

        return f"Processed {count} numeric values, sum={total}, avg={avg}"


class TextProcessor(DataProcessor):
    """Processor for text data."""

    def validate(self, data: Any) -> bool:
        """Check that data is a string."""
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        """Process text data and return text statistics."""
        if not self.validate(data):
            raise ValueError("Invalid text data")

        char_count: int = len(data)
        word_count: int = len(data.split())

        return f"Processed text: {char_count} characters, {word_count} words"


class LogProcessor(DataProcessor):
    """Processor for log entry data."""

    def validate(self, data: Any) -> bool:
        """Check that data is a log string with a level separator."""
        return isinstance(data, str) and ":" in data

    def process(self, data: Any) -> str:
        """Process log data and return a formatted alert or info message."""
        if not self.validate(data):
            raise ValueError("Invalid log data")

        level, message = data.split(":", 1)
        level = level.strip().upper()
        message = message.strip()

        if level == "ERROR":
            return f"[ALERT] {level} level detected: {message}"

        return f"[INFO] {level} level detected: {message}"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    numeric = NumericProcessor()
    print("\nInitializing Numeric Processor...")
    print("Processing data: [1, 2, 3, 4, 5]")
    try:
        if numeric.validate([1, 2, 3, 4, 5]):
            print("Validation: Numeric data verified")
        result = numeric.process([1, 2, 3, 4, 5])
        print(numeric.format_output(result))
    except ValueError as error:
        print(f"Error: {error}")

    text = TextProcessor()
    print("\nInitializing Text Processor...")
    print('Processing data: "Hello Nexus World"')
    try:
        if text.validate("Hello Nexus World"):
            print("Validation: Text data verified")
        result = text.process("Hello Nexus World")
        print(text.format_output(result))
    except ValueError as error:
        print(f"Error: {error}")

    log = LogProcessor()
    print("\nInitializing Log Processor...")
    print('Processing data: "ERROR: Connection timeout"')
    try:
        if log.validate("ERROR: Connection timeout"):
            print("Validation: Log entry verified")
        result = log.process("ERROR: Connection timeout")
        print(log.format_output(result))
    except ValueError as error:
        print(f"Error: {error}")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors: list[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]

    data_samples: list[Any] = [
        [1, 2, 3],
        "Hello Nexus!",
        "INFO: System ready",
    ]

    for i, (processor, data) in enumerate(zip(processors, data_samples),
                                          start=1):
        try:
            result = processor.process(data)
            print(f"Result {i}: {result}")
        except ValueError as error:
            print(f"Result {i}: Error - {error}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")
