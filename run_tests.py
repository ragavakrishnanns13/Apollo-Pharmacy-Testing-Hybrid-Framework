import subprocess
from utilities.report import BeautifulReporter
from datetime import datetime as dt

def run_tests():
    start = dt.now()
    print("Starting test execution with Pytest in parallel...")
    subprocess.run(["pytest", "-n", "auto", "--maxfail=1", "--disable-warnings"])
    print(start)
    end = dt.now()
    print(end)
    print(end - start)

def create_reports():
    reporter = BeautifulReporter()
    reporter.generate_report()

if __name__ == "__main__":
    run_tests()
    create_reports()


