import os

import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    extra.append(pytest_html.extras.text(call, name="Failure Output"))
    if report.when == "call":
        file_path = os.path.abspath("../test-reports/screenshots/*")
        images_path = 'test-reports/screenshots/'
        for root, dirs, files in os.walk(file_path):
            print(files)
            for file in files:
                if file.endswith('.png'):
                    image = os.path.abspath('../{}{}'.format(images_path, file))
                    extra.append(pytest_html.extras.image(image))
    report.extra = extra
