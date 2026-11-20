import sys
import types

def read_files():
    print("Reading Files")

def calculate_stats():
    print("Calculating Statistics")

def write_reports():
    print("Writing Reports")

def percentage(present, total):
    return (present / total) * 100 if total else 0

print("A. ONE SCRIPT")
read_files()
calculate_stats()
write_reports()

print("\nB. ONE MODULE")
attendance_utils = types.ModuleType("attendance_utils")
attendance_utils.read_files = read_files
attendance_utils.calculate_stats = calculate_stats
attendance_utils.write_reports = write_reports
sys.modules["attendance_utils"] = attendance_utils
import attendance_utils
attendance_utils.read_files()
attendance_utils.calculate_stats()
attendance_utils.write_reports()

print("\nC. THREE MODULES")
reader, stats, report = (types.ModuleType(name) for name in ("reader", "stats", "report"))
reader.read_files = read_files
stats.calculate_stats = calculate_stats
report.write_reports = write_reports
sys.modules.update({"reader": reader, "stats": stats, "report": report})
import reader, stats, report
reader.read_files()
stats.calculate_stats()
report.write_reports()

print("\nD. PACKAGE ORGANISATION")
attendance = types.ModuleType("attendance")
attendance.__path__ = []
reader = types.ModuleType("attendance.reader")
stats = types.ModuleType("attendance.stats")
report = types.ModuleType("attendance.report")
reader.read_files = read_files
stats.calculate_stats = calculate_stats
stats.percentage = percentage
report.write_reports = write_reports
attendance.reader, attendance.stats, attendance.report = reader, stats, report
sys.modules.update({
    "attendance": attendance,
    "attendance.reader": reader,
    "attendance.stats": stats,
    "attendance.report": report
})
from attendance.reader import read_files as package_read_files
from attendance.stats import calculate_stats as package_calculate_stats
from attendance.report import write_reports as package_write_reports
package_read_files()
package_calculate_stats()
package_write_reports()
print("\nPercentage:", percentage(8, 10), "%")
