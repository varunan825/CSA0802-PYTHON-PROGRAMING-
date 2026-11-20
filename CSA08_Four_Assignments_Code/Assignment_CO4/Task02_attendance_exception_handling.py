from io import StringIO

class InvalidRecord(Exception):
    pass

def parse_line(line):
    parts = line.strip().split(",")
    if len(parts) != 3:
        raise InvalidRecord(f"expected 3 fields, found {len(parts)}")
    reg, date, status = parts
    if status not in ("P", "A"):
        raise InvalidRecord(f"invalid status '{status}'")
    return reg, date, status

def summarise(data):
    present = absent = 0
    errors = []
    try:
        with StringIO(data) as file:
            for line_no, line in enumerate(file, 1):
                if not line.strip():
                    continue
                try:
                    reg, date, status = parse_line(line)
                    if status == "P":
                        present += 1
                    else:
                        absent += 1
                except InvalidRecord as error:
                    errors.append((line_no, str(error)))
    except (PermissionError, UnicodeDecodeError, OSError) as error:
        raise RuntimeError("Attendance processing failed") from error
    else:
        print("File processed successfully")
    finally:
        print("Processing completed")
    return present, absent, errors

data = (
    "192311001,2026-10-08,P\n"
    "192311002,2026-10-08,A\n"
    "192311003,2026-10-08\n"
    "192311004,2026-10-08,L\n"
)
print(summarise(data))
