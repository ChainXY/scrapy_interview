# Scrapy Interview Test
This is a small challenge designed to test your scraping abilities.
## Setup:
Set up an environment and install scrapy. 
- We **strongly recommend** using miniconda for install, since installing scrapy in windows requires separate install of C++ build tools (https://docs.scrapy.org/en/latest/intro/install.html#windows)
- We recommend using python 3.9.
- You only need to install scrapy to do this task.
- Submissions not using scrapy will not be accepted.
## Test Run
Run the provided londondrugs scrapy spider to make sure your setup is working.
- To run a spider cd into this (\GitHub\scrapy_interview) folder, and run `scrapy crawl londondrugs -o londondrugs.csv` in the terminal.


## Useful links:
https://devhints.io/xpath

https://docs.scrapy.org/en/latest/topics/selectors.html .get()/.getall() are equivalent to extract_first()/extract()

## Debugging scrapy in vscode

1. Go to debugging menu on the left-side of the UI, and click create a launch.json file

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
3. Set up breakpoints in your spider (e.g., on yielding an item) and start the debugger by clicking Python: Launch Scrapy Spider in the debug menu:

    <img src="images/2022-05-24 10_19_57-anthropologie.py - ChainXY_Production - Visual Studio Code.png" width = 600px/>

## Next Steps
Once you have the envrionment set up and scrapy is working on your computer, reach out to us for the list of websites for your test.
### Important considerations:
- Use the provided item definition (fields/columns) for your scrape. **DO NOT** create custom item fields. For instance, store hours should be in `item['store_hours']`, address in `item['address']` etc.
- We strongly recommend using the html selectors for scraping. Look at the provided londondrugs spider for examples.

