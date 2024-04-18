# Scrapy Interview Test
Scrapy is a Python framework designed to crawl/extract information from websites. During your interview, you will be given a small challenge designed to test your scraping and problem-solving abilities. 
## Setup:
Set up an environment and install Scrapy. 
- We **strongly recommend** using [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/), since installing Scrapy in Windows [requires separate install of C++ build tools](https://docs.scrapy.org/en/latest/intro/install.html#windows)
- We recommend using python 3.10.
- Once you have installed Anaconda/Miniconda, install Scrapy with: 
 
        conda install -c conda-forge scrapy
- IMPORTANT: Submissions not using Scrapy will not be accepted.
## Test Run
Run the provided `sweetwaterscoffeetea.py` Scrapy Spider to make sure your setup is working.
- To run a Spider, navigate to this folder:
  ```
        cd GitHub\scrapy_interview
  ```
- Run the command:
  ```
        scrapy crawl sweetwaterscoffeetea -o sweetwaterscoffeetea.csv
  ```
- After the Spider finishes running, should see this as the last line on on your console:
```
        [scrapy.core.engine] INFO: Spider closed (finished)
```
- and this log:
  ![image](https://github.com/ChainXY/scrapy_interview/assets/22741899/3350911d-5609-4d06-acf9-555002e0d4a7)

There should be no errors and the CSV file should be populated with data.

## Troubleshooting
If you are encountering issues with the set-up or the test, please reach out to us and include the following: the console log or a relevant screenshot of the error, with a short explanation. We will get back to you as soon as possible.

## Useful Links
[XPath cheatsheet](https://devhints.io/xpath)

[Scrapy Selectors](https://docs.scrapy.org/en/latest/topics/selectors.html)

- Note: `.get()` and `.getall()` are equivalent to `.extract_first()` and `.extract()`, respectively.

## Debugging Scrapy in VSCode
This step is optional but highly recommended as it is very helpful when troubleshooting errors.

1. Go to the debugging menu on the left-side of the UI, and click create a launch.json file

    <img src="images/2022-05-24 10_16_13-OverlayWindow.png" width = 300px/>

2. Paste the code below into the launch.json file
    ```
    {
        "version": "0.1.0",
        "configurations": [
            {
                "name": "Python: Launch Scrapy Spider",
                "type": "python",
                "request": "launch",
                "module": "scrapy",
                "args": [
                    "runspider",
                    "${file}"
                ],
                "console": "integratedTerminal"
            }
        ]
    }
    ```
3. Set up breakpoints in your Spider (e.g., on yielding an item) and start the debugger by clicking Python: Launch Scrapy Spider in the debug menu:

    <img width="604" alt="image" src="https://github.com/ChainXY/scrapy_interview/assets/22741899/b16c3718-56e6-41cc-a61b-df601615d73f">


## Next Steps
Once you have the environment set up and Scrapy is working on your computer, reach out to us to <b>*confirm that you have completed the pre-interview set-up*</b>. During your scheduled interview, you will be asked to scrape a different website. Please note that if you have not completed set-up by then, we cannot proceed with the interview.


## Important considerations:
- Use the provided item definitions (fields/columns) for your scrape. **DO NOT** create custom item fields. For instance, the addresses should be in `item['address']`, etc.
- We strongly recommend learning about the Scrapy Selectors for HTML scraping. Look at the provided `sweetwaterscoffeetea.py` Spider for examples.

## Tips
- When evaluating a website for scraping, think about the most efficient way to extract information from it. Should you get the information from the source HTML using Selectors, like in `sweetwaterscoffetea`? Could there be an API call whose response contains the information you want in a structured object, and if so, how can you extract it?
- When dealing with a website that spreads store information across many pages, for instance a Directory of links that go from states/provinces to cities to stores, the callback function in Scrapy Requests allows you to "crawl" multiple webpages asynchronously and process them separately.
