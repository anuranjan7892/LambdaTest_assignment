# Problem statement

1. amazon.in
2. search "lg soundbar"
3. select lg brand checkbox
4. read product price and name
5. print product price and name in desc order of price via code.
6. if price is not present then consider price as zero
eg:- 
12000 : lg soundbar slbajsbd
42000 : lg soundbar Eh12368



I have used Python to test this scenario. There might be some extra utility files as well in the repository which gets created along with the project.
You can run the 'test_amazon.py' file to print the results.



Instructions to execute the testcase locally:

1. Install any latest version of Python3
2. Install PyCharm(recommended) or any other IDE which supports python.
3. Clone the repository into PyCharm
4. Go to Interpreter settings and Set the interpreter:
  - Add a new interpreter
  - In Virtualenv Environment, set the Base Interpreter to the location where python.exe is installed
  - Click Apply or OK
  - Ensure the Interpreter set in the above steps is displayed at the footer
5. To run the testcase, Open Terminal and write 'pytest' and enter. If no errors or warning is displayed, then the testcase will execute successfully.
  - If any error or warning is displayed, then run the folllowing command: pip install pytest-pycharm
  - If pytest is not installed using the above command then just write 'import pytest' in the 'test_coding_assignments' file, then hover over 'pytest' word and then install pytest from the suggestion box
6. Finally, to execute the testcase, we can either enter 'pytest' in the Terminal or right click on the Run button in the testcase and select 'Run Python tests for...'
