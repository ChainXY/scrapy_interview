# Scrapy Interview Test
Scrapy is a Python framework designed to crawl/extract information from websites. This is a small challenge designed to test your scraping abilities. 
## Setup:
Set up an environment and install Scrapy. 
- We **strongly recommend** using [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/), since installing Scrapy in Windows [requires separate install of C++ build tools](https://docs.scrapy.org/en/latest/intro/install.html#windows)
- We recommend using python 3.10.
- Once you have installed Anaconda/Miniconda, install Scrapy with: 
 
        conda install -c conda-forge scrapy
- IMPORTANT: Submissions not using Scrapy will not be accepted.
## Test Run
Run the provided `sweetwaterscoffeetea.py` Scrapy Spider to make sure your setup is working.
- To run a Spider, navigate to this folder in Terminal:
  ```
        cd GitHub\scrapy_interview
  ```
  and run the command:
  ```
        scrapy crawl sweetwaterscoffeetea -o sweetwaterscoffeetea.csv
  ```

## Useful Links
[XPath cheatsheet](https://devhints.io/xpath)

[Scrapy Selectors](https://docs.scrapy.org/en/latest/topics/selectors.html)

- Note: `.get()` and `.getall()` are equivalent to `.extract_first()` and `.extract()`, respectively.

## Debugging Scrapy in VSCode

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

    <img src="images/2022-05-24 10_19_57-anthropologie.py - ChainXY_Production - Visual Studio Code.png" width = 600px/>

## Next Steps
Once you have the environment set up and Scrapy is working on your computer, reach out to us for the list of websites for your test. Once you receive the list of websites to scrape, you will have <b>*two (2) hours*</b> to complete the challenge.

## Submission

Compress the scrapy_interview folder (containing the csvs and Spiders) and email the ZIP file.

## Important considerations:
- Use the provided item definitions (fields/columns) for your scrape. **DO NOT** create custom item fields. For instance, store hours should be in `item['store_hours']`, address in `item['address']`, etc.
- We strongly recommend using the Scrapy Selectors for HTML scraping. Look at the provided `londondrugs.py` Spider for examples.

## Tips
- When evaluating a website, think about the most efficient way to extract information from it. Should you get the information from the source HTML using Selectors? Could there be an API call whose response contains the information you want in a structured object, and if so, can you extract it?
- When dealing with a website that spreads store information across many pages, think about a way to extract the store URLs, and only then use the callback function in Scrapy Requests on each individual page.
