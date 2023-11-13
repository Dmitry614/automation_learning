import subprocess


def run_test(test_file, browsers, html_report):
    command = ["pytest", test_file]
    if test_file != "test_3.py":
        for browser in browsers:
            command.extend(["--browser", browser])
    command.extend(["--html", html_report.format(test_file)])

    subprocess.run(command)


if __name__ == "__main__":
    test_files = ["test_1.py", "test_2.py", "test_3.py"]
    browsers = ["chromium", "firefox"]
    html_report_template = "Reports/report_{}.html"

    for test_file in test_files:
        run_test(test_file, browsers, html_report_template)