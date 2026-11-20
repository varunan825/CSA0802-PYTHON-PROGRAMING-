from decimal import Decimal, InvalidOperation
from io import StringIO

def process_file(data):
    total = Decimal("0.00")
    report, rejected = [], []
    with StringIO(data) as file:
        for line_no, line in enumerate(file, 1):
            if not line.strip():
                continue
            try:
                parts = line.strip().split(",")
                if len(parts) != 3:
                    raise ValueError("Invalid fields")
                name = parts[1].strip()
                amount = Decimal(parts[2].strip())
                total += amount
                report.append(f"{name} {amount:.2f}")
            except (ValueError, InvalidOperation) as error:
                rejected.append((line_no, str(error)))
    print("Mess Bill Report")
    for item in report:
        print(item)
    print("Total:", total)
    print("Rejected Lines:", rejected)

data = """101,Arun,1250.50
102,Priya,1500.00
103,Rahul,1000.00"""
process_file(data)
