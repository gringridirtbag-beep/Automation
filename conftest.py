import os
import pytest

from core.driver import Driver


@pytest.fixture
def driver():
    driver = Driver.get_driver()

    yield driver

    driver.quit()


os.makedirs("screenshots", exist_ok=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            try:

                screenshot_path = os.path.abspath(
                    f"screenshots/{item.name}.png"
                )

                print(f"Saving screenshot to: {screenshot_path}")

                success = driver.save_screenshot(
                    screenshot_path
                )

                print(f"Screenshot saved: {success}")

            except Exception as e:
                print(
                    f"Error taking screenshot: {e}"
                )