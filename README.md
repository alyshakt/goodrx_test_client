# goodrx-test-client Test Project by Alysha Kester-Terry https://github.com/alyshakt

A Python based project to fulfill the GoodRx test project.

# Run `pip3 install -r requirements.txt` on the directory to install dependencies.

This project uses Selenium https://www.selenium.dev/ and Chrome or Firefox. -If you already have Chrome or Firefox on
your machine, you don't need to do anything special to use it.

I built this project to be able to run using pytest runners https://docs.pytest.org

Using IntelliJ's pytest runner, you can run tests. Find the runner under /tests.

-Note that the test runner is configured to run using the Python interpreter of the project, so you will need to define
your python interpreter for your project, or change the runner to refer to another interpreter.

-You must define an environment variable when running like `--environment='dev' or --environment='prod'`
-To add logging output to the console, add `-o log_cli=true` to arguments

-To get a junit XML report, add `--junitxml=<path to save the output file to>.xml`; I like to save reports to
\test-reports

-To get an HTML report, add `--html=<path to save the file to>.html`; I like to save reports to \test-reports

-Find screenshots and HTML reports in test-reports/screenshots.

My Test Runner configuration is:
```
<component name="ProjectRunConfigurationManager">
    <configuration default="false" name="Test Runner" type="tests" factoryName="py.test" singleton="false">
        <module name="goodrx_test_client"/>
        <option name="INTERPRETER_OPTIONS" value=""/>
        <option name="PARENT_ENVS" value="true"/>
        <option name="SDK_HOME" value="$PROJECT_DIR$/../venv/bin/python"/>
        <option name="WORKING_DIRECTORY" value="$PROJECT_DIR$"/>
        <option name="IS_MODULE_SDK" value="true"/>
        <option name="ADD_CONTENT_ROOTS" value="true"/>
        <option name="ADD_SOURCE_ROOTS" value="true"/>
        <option name="_new_keywords" value="&quot;&quot;"/>
        <option name="_new_parameters" value="&quot;&quot;"/>
        <option name="_new_additionalArguments"
                value="&quot;--environment\u003d\u0027Prod\u0027 -s -o log_cli\u003dtrue --html\u003dtest-reports/GoodRx_Test_User_Search_Coupon_Workflow_Report.html&quot;"/>
        <option name="_new_target" value="&quot;$PROJECT_DIR$/tests/search/test_amoxicillin.py&quot;"/>
        <option name="_new_targetType" value="&quot;PATH&quot;"/>
        <method v="2"/>
    </configuration>
</component>
```

I use the `record_xml_attribute` in my tests because I want useable xml reporting output to integrate with XRay
importing capabilities with Jira. It is not necessary to use it if you do not care for that output in your xml document.

To Run Headless with Chrome, open your test with the following code:

```
	options = Options()
	options.add_argument('--headless')
	driver = webdriver.Chrome(chrome_options=options)
```

To Run Headless with GeckoDriver, open your test with the following code:

```  
from selenium.webdriver.firefox.options import Options as FirefoxOptions
	  
	    options = FirefoxOptions()
        options.add_argument('-headless')
        driver = webdriver.Firefox(options=options)
```

You'll see an `App` class to define Enums for switching between types of web apps. This is simply an example of
how you could use Enums like this to standardize initial inputs and make things easier for testers to switch between
websites, environments or anything else you can think of. This Enum is used in `AppSetup.py` to define the URL
for the Enum and pass it on to navigate to that URL.

Screenshots are automatically named by the created date and saved in PNG format, with the option to add a name to append
to the date.

This Base Page object strategy was gleaned with much gratitude from
http://elementalselenium.com/tips/9-use-a-base-page-object

Reports
===
<b> If you need a neat and business-facing report of test output, I do not recommend compiling it from raw test output inside a framework like this.</b> 

The best test reporting is done with traceability and risk management in mind, showing component coverage by features
and prioritized past and future work.

Therefore, I suggest importing/exporting simple xml results from this framework into a project management system that is
linked up to a Test management system, for instance, Jira using XRay for Jira. Xray's reporting capabilities are far
more useful for Stakeholders, Managers, Quality Assurance reporting and even provides Developer-facing results of all
types. Their API is easy to use!

I'm a shameless supporter of their product as it has enhanced teams time and time again when I have been able to
implement it. <a href="https://www.getxray.app/">XRay for Jira</a>

Additional Test Case Consideration
==
Critical test flows should take into account information that is being displayed from backend API services. A critical test case would be to make sure that prices and pharmacies displayed for a particular drug name are matching what is served from the backend - for instance, that the pharmacy name "Smith's" has a price of 5.22 from the backend, and is displaying 5.22 and not potentially another pharmacy's prices.
I'd imagine a flow such as this:
For a given environment...
#GET pharmacies and prices for input: drug name
#When results return, perhaps verify the count of results.
#Parse and save the results to variables to be verified further in the test
#Access the UI and search for the same drug name input 
#Verify the count of results is the same on UI as backend
#Verify that for each pharmacy result, the name and price matches the backend results.
#If there's a mis-match or not all results are being shown on UI, return a comparison of the backend to UI results.
