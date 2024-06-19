class CustomTime:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize_time()

    def normalize_time(self):
        total_seconds = self.to_seconds()
        self.hours = total_seconds // 3600
        total_seconds %= 3600
        self.minutes = total_seconds // 60
        self.seconds = total_seconds % 60

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def add_time(self, other):
        total_seconds = self.to_seconds() + other.to_seconds()
        self.hours = total_seconds // 3600
        total_seconds %= 3600
        self.minutes = total_seconds // 60
        self.seconds = total_seconds % 60

    def subtract_time(self, other):
        total_seconds = self.to_seconds() - other.to_seconds()
        if total_seconds < 0:
            total_seconds = 0
        self.hours = total_seconds // 3600
        total_seconds %= 3600
        self.minutes = total_seconds // 60
        self.seconds = total_seconds % 60

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

# Example usage:
time1 = CustomTime(1, 30, 45)
time2 = CustomTime(0, 45, 15)

print(f"Time 1: {time1}")
print(f"Time 2: {time2}")

time1.add_time(time2)
print(f"Time 1 after adding Time 2: {time1}")

time1.subtract_time(time2)
print(f"Time 1 after subtracting Time 2: {time1}")

print(f"Time 1 in seconds: {time1.to_seconds()}")
