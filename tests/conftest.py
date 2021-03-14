import time


def pytest_addoption(parser):
    parser.addoption("--environment",
                     action="store",
                     default="local",
                     help="Environment to run tests in")


def pytest_generate_tests(metafunc):
    if 'environment' in metafunc.fixturenames:
        print(metafunc.config.option.environment)
        metafunc.parametrize("environment",
                             [str(metafunc.config.option.environment)])


def pytest_sessionfinish(session, exitstatus):
    reporter = session.config.pluginmanager.get_plugin('terminalreporter')
    duration = time.time() - reporter._sessionstarttime
    reporter.write_sep('=',
                       'duration: {} seconds'.format(duration),
                       yellow=True,
                       bold=True)


def pytest_unconfigure(config):
    reporter = config.pluginmanager.get_plugin('terminalreporter')
    duration = time.time() - reporter._sessionstarttime
    reporter.write_sep('=',
                       'duration: {} seconds'.format(duration),
                       yellow=True,
                       bold=True)
