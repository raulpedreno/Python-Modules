from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):
    """Abstract base class for all stream types."""

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data and return a summary string."""
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter the data batch using a generic criteria match."""
        if criteria is None:
            return data_batch

        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return basic stream statistics."""
        return {
            "stream_id": self.stream_id,
            "processed_count": self.processed_count,
        }


class SensorStream(DataStream):
    """Stream specialized in environmental sensor data."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process sensor readings and calculate average temperature."""
        try:
            self.processed_count += len(data_batch)
            temps: List[float] = [
                float(item.split(":")[1])
                for item in data_batch
                if isinstance(item, str) and item.startswith("temp:")
            ]
            avg_temp: float = sum(temps) / len(temps) if temps else 0.0
            return (
                f"Sensor analysis: {len(data_batch)} readings "
                f"processed, avg temp: {avg_temp:.1f}°C"
            )
        except Exception as error:
            return f"Sensor processing failed: {error}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter only high temperature readings when requested."""
        if criteria == "high_temp":
            return [
                item
                for item in data_batch
                if isinstance(item, str)
                and item.startswith("temp:")
                and float(item.split(":")[1]) > 30
            ]

        return super().filter_data(data_batch, criteria)


class TransactionStream(DataStream):
    """Stream specialized in financial transaction data."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process transactions and calculate net flow."""
        try:
            self.processed_count += len(data_batch)
            total_amount: float = 0.0

            for item in data_batch:
                action, value = item.split(":")
                amount: float = float(value)

                if action == "buy":
                    total_amount += amount
                elif action == "sell":
                    total_amount -= amount

            return (
                f"Transaction analysis: {len(data_batch)} "
                f"operations, net flow: {total_amount:+.0f} units"
            )
        except Exception as error:
            return f"Transaction processing failed: {error}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter large transactions when requested."""
        if criteria == "large":
            return [
                item
                for item in data_batch
                if isinstance(item, str) and float(item.split(":")[1]) > 100
            ]

        return super().filter_data(data_batch, criteria)


class EventStream(DataStream):
    """Stream specialized in system event data."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process events and count error occurrences."""
        try:
            self.processed_count += len(data_batch)
            error_count: int = sum(
                1
                for item in data_batch
                if isinstance(item, str) and item.lower() == "error"
            )
            return (
                f"Event analysis: {len(data_batch)} events, "
                f"{error_count} errors detected"
            )
        except Exception as error:
            return f"Event processing failed: {error}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter critical events when requested."""
        if criteria == "critical":
            return [
                item
                for item in data_batch
                if isinstance(item, str) and item.lower() == "error"
            ]

        return super().filter_data(data_batch, criteria)


class StreamProcessor:
    """Manager that processes multiple stream types polymorphically."""

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """Add a new stream to the processor."""
        self.streams.append(stream)

    def process_all(self, data_batches: List[List[Any]]) -> List[str]:
        """Process all streams with their corresponding data batches."""
        results: List[str] = []

        for stream, data in zip(self.streams, data_batches):
            try:
                result: str = stream.process_batch(data)
                results.append(result)
            except Exception as error:
                results.append(
                    f"Processing failed for {stream.stream_id}: {error}")

        return results

    def show_stats(self) -> None:
        """Print statistics for all registered streams."""
        for stream in self.streams:
            print(stream.get_stats())


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor_stream: SensorStream = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor_stream.stream_id}, Type: Environmental Data")
    data_sensor: List[str] = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {data_sensor}")
    print(sensor_stream.process_batch(data_sensor))
    print()

    print("Initializing Transaction Stream...")
    transaction_stream: TransactionStream = TransactionStream("TRANS_001")
    print(f"Stream ID: {transaction_stream.stream_id}, Type: Financial Data")
    data_transaction: List[str] = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {data_transaction}")
    print(transaction_stream.process_batch(data_transaction))
    print()

    print("Initializing Event Stream...")
    event_stream: EventStream = EventStream("EVENT_001")
    print(f"Stream ID: {event_stream.stream_id}, Type: System Events")
    data_event: List[str] = ["login", "error", "logout"]
    print(f"Processing event batch: {data_event}")
    print(event_stream.process_batch(data_event))
    print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    processor: StreamProcessor = StreamProcessor()
    processor.add_stream(sensor_stream)
    processor.add_stream(transaction_stream)
    processor.add_stream(event_stream)

    print("Batch 1 Results:")
    data_batches: List[List[Any]] = [
        ["temp:28.0", "temp:32.5", "temp:25.0"],
        ["buy:200", "sell:50", "buy:150"],
        ["login", "error", "error", "logout"],
    ]

    results: List[str] = processor.process_all(data_batches)
    for result in results:
        print(f"- {result}")
    print()

    print("Stream filtering active: High-priority data only")
    high_temps: List[Any] = sensor_stream.filter_data(
        data_batches[0], "high_temp")
    large_transactions: List[Any] = transaction_stream.filter_data(
        data_batches[1], "large"
    )
    critical_events: List[Any] = event_stream.filter_data(
        data_batches[2], "critical"
    )

    print(
        f"Filtered results: "
        f"{len(high_temps)} critical sensor alerts, "
        f"{len(large_transactions)} large transactions, "
        f"{len(critical_events)} critical events"
    )
    print()

    print("All streams processed successfully. Nexus throughput optimal.")
