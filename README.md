# Distributed Web Crawler

The Distributed Web Crawler is a Python project that allows users to crawl and scrape websites. The project is distributed across multiple nodes, each running on a separate port, and utilizes Flask to serve as the endpoint for the scraper and crawler. The project allows users to specify a website and the number of levels of child pages to crawl, with each node taking on a portion of the crawling workload. Additionally, the project includes functionality to create a graph of the website and its child pages, and to check the health of each node in the network. The project provides a distributed solution for web scraping and crawling, allowing for efficient and scalable data collection.
<br />
#### [Project Demo Link](https://unioulu-my.sharepoint.com/:v:/g/personal/wsandadu22_student_oulu_fi/EXZSVGX550RNlrSAfGlIUgIBhZjoEITFYo8uYiDe_kTL1Q?e=UQpDsa)
<br />

`Group O`

`Kavindu Ravishan -  2208084`<br />
`Windula Kularatne - 2207601`

There were three members in the group, but one member dropped out at the beginning.

<br />
Project Structure:
<br />
<br />
├── main.py<br />
├── content.py<br />
├── crawler.py<br />
├── generate_urls.py<br />
├── health_monitor.py<br />
├── make_graph_function.py<br />
├── node.py<br />
├── storage/<br />
└── util.py<br />
<br />

`main.py`: The main script for the project and this work as master node. This script allows the user to interact with the command-line interface and choose between scraping or crawling.<br />
`content.py`: A module that contains a function to check if a file exists and print its content.<br />
`crawler.py`: A module that contains functions for crawling a website.<br />
`generate_urls.py`: A module that generates a list of URLs for the crawler to use.<br />
`node.py`: A module that defines a Flask app and serves as the endpoint for the scraper and crawler.<br />
`scraper.py`: A module that contains functions for scraping a website.<br />
`storage/`: A directory where the scraped data is stored.<br />
`README.md`: A file that contains information about the project.<br />
`requirements.txt`: A file that lists the required packages for the project.<br />
`health_monitor.py`: A module that monitors the health of the crawler and scraper and sends alerts if any issues are detected.<br />
`make_graph_function.py`: A module that contains a function to visualize the scraped data in a graph.<br />
`util.py`: A module that contains utility functions used throughout the project.

## Requirements:
Before running the application, you need to have the all packages installed. Mostly we use these packages to do our task:

- `requests`
- `beautifulsoup4`
- `flask`

You can install these packages by running the following command:
`pip install -r requirements.txt`
<br />Make sure to run this command in the project directory, where the requirements.txt file is located. This will install all the necessary packages for running the application.

## How to Run:

To run the distributed web crawler, you need to run the main.py file. The program will automatically start the necessary number of instances of the node.py file and the Prometheus server.

To run the program, open a terminal window, navigate to the project directory, and run the following command (Remeber to be in top level and not in code directory):
<br />

#### `python code/main.py`
<br />

## main.py
This is the main module of the project which serves as the entry point to the application. It contains a loop that waits for user input to either crawl, make a graph, show html, or exit the program.

### Functions

- `make_urls(number_of_ports)`: This function takes in the number of ports and returns a list of URLs based on the number of ports.
- `get_random_url(list_of_urls)`: This function takes in a list of URLs and returns a random URL from the list.
- `start_all_nodes(number_of_ports)`: This function takes in the number of ports and starts all the nodes.
- `start_health_monitor(number_of_ports)`: This function takes in the number of ports and starts the health monitor.
- `check_if_exists_and_print_html(name)`: This function takes in the name of the file and checks if it exists in the storage directory. If it exists, it prints the HTML content of the file.
- `make_graph_from_adjacency_list(response_dict)`: This function takes in a dictionary containing the adjacency list representation of a graph and generates a line graph.

### Main Code

The main code starts by asking the user to enter the number of nodes to create. It then calls the `make_urls` function to generate the URLs for the nodes. If the number of nodes entered by the user exceeds the maximum number of nodes allowed, the code creates the maximum number of nodes allowed. The code then starts all the nodes and the health monitor.

The code then enters a loop where it waits for user input. If the user enters "crawl", the code prompts the user to enter a website and the number of levels to crawl. It then chooses a random URL from the list of URLs generated earlier and sends a request to that URL with the website and levels as parameters.

If the user enters `make_graph`, the code prompts the user to enter a website and the depth for the graph. The code then sends requests to all the URLs in the list with the website and depth as parameters. The responses from all the requests are combined into a dictionary containing the adjacency list representation of the graph, which is then passed to the `make_graph_from_adjacency_list` function.

If the user enters `show_html`, the code prompts the user to enter a website. It then checks if the HTML file for that website exists in the storage directory and if it does, prints the HTML content.

If the user enters `exit`, the program exits. If the user enters an invalid command, the program prompts the user to enter a valid command.

## node.py

This is the node.py file, which is a Python Flask application that serves as a node in a distributed web crawler system. The node exposes several REST endpoints that allow other nodes to initiate crawls and receive the results of previous crawls.

### Endpoints

- `/check`: Returns the HTML content of all the websites in the system except the current website.
- `/`: Returns the current website.
- `/health`: Returns the status of the node.
- `/crawl`: Initiates a crawl of a given website and stores the results in a table. It also sends out further crawls for each child URL found during the initial crawl.
- `/make_graph`: Generates a graph of the websites in the system based on the child URLs discovered during previous crawls.

### Variables
- `URLS`: A list of URLs for each node in the system.
- `number_of_ports`: The number of ports available on each node.
- `number_of_nodes`: The total number of nodes in the system.
- `limiter`: The maximum number of child URLs to be stored for each parent URL.
- `child_adjacency`: A dictionary that stores the child URLs and their associated workers for each parent URL in the system.

### Functions
- `crawl(website)`: This function takes in a website and initiates a crawl of it. It returns a list of child URLs found during the crawl.
- `make_urls(number_of_nodes)`: This function takes in the number of nodes and generates a list of URLs for each node.
- `get_random_url(URLS)`: This function takes in a list of URLs and returns a random URL from the list.

The `node.py` file uses the Flask library to define a web application. The `/check`, `/`, and `/health` endpoints simply return the current website or the HTML content of the other websites in the system. The `/crawl` endpoint initiates a crawl of a given website and sends out further crawls for each child URL discovered during the initial crawl. The `/make_graph` endpoint generates a graph of the websites in the system based on the child URLs discovered during previous crawls.

The `crawl(website)` function initiates a crawl of a given website using the `crawl()` function from the crawler module. It then returns a list of child URLs found during the crawl.

The `make_urls(number_of_nodes)` function generates a list of URLs for each node in the system. It takes in the total number of nodes and returns a list of URLs in the format http://localhost:{port}.

The `get_random_url(URLS)` function takes in a list of URLs and returns a random URL from the list. It is used to select a worker node for each child URL found during a crawl.

## content.py
This module contains a function to check if a file exists and print its HTML content.
### Functions
`check_if_exists_and_print_html(name)`: This function takes in a file name and checks if the file exists. If it exists, it prints its HTML content. If it does not exist, it prints a message saying that the file is not accessible.

## crawler.py
This module contains functions to crawl a given URL and extract text content from its HTML.
### Functions
- `validate_url(url)`: This function takes in a URL and returns True if the URL is valid and False otherwise.
- `extract_text(html)`: This function takes in an HTML string and extracts the title and text content from it.
- `hard_disk_store(html, url)`: This function takes in an HTML string and a URL, and stores the HTML content on disk with a filename based on the URL.
- `crawl(url)`: This function takes in a URL, crawls the website, and returns a list of child URLs. It first checks if the URL is valid using `validate_url()`. Then, it requests the page using the requests library, and extracts the HTML content using the `extract_text()` function. The HTML content is then stored on disk using `hard_disk_store()`. Finally, the function uses `beautifulsoup4` to parse the HTML and extract all child URLs, which are returned as a list.

## health_monitor.py

The `health_monitor.py` module contains a function to periodically check the health of multiple nodes in a distributed system. The function uses the `requests` module to send a GET request to the `/health` endpoint of each node in the system. If a node responds with a status code other than 200, it is added to a list of nodes to retry. Nodes in the retry list are retried three times using the `node_retry()` function from the `util` module. The function is `scheduled` to run every 10 seconds using the schedule module, and the number of nodes to check is provided as a command-line argument.

### Functions
- `periodic_healthcheck(node_count)`: This function takes in the number of nodes in the system and periodically checks the health of each node. It first generates a list of URLs to check using the `make_urls()` function from the `generate_urls` module. Then, it iterates over the list of URLs and sends a GET request to the `/health` endpoint of each node using the `requests` module. If a node responds with a status code other than 200, it is added to a list of nodes to retry. Nodes in the retry list are retried three times using the `node_retry()` function from the `util` module. The function is scheduled to run every 10 seconds using the `schedule` module.
- `__main__()`: This function parses the command-line argument for the number of nodes in the system, and schedules the `periodic_healthcheck()` function to run every 10 seconds using the `schedule` module. If an error occurs, it prints an error message and exits the program.

## make_graph_function.py
This module contains functions to generate a graph visualization from a given adjacency list.

### Functions
- `make_graph_from_adjacency_list(data)`: This function takes in an adjacency list in the form of a JSON dictionary, filters out redundancies, and generates a graph visualization using Plotly. The function converts the data into graph elements and creates a list of edges. It then uses Plotly to create a visualization of the graph. The resulting graph is not returned, but rather displayed in the web browser.

## util.py
The util.py file contains utility functions for starting nodes and retrying failed nodes. 

### Functions
- `start_all_nodes(n)`: This function takes in an integer n and starts n nodes by running the `node.py` script in separate terminal windows using `subprocess.Popen()`. Each node is started on a different port number, starting from 5000.

- `start_a_nodes(n,num_nodes)`: This function takes in an integer n and the total number of nodes `num_nodes`. It starts a single node on port number `5000+n` by running the `node.py` script using `subprocess.Popen()`.

- `start_health_monitor(num_nodes)`: This function takes in the total number of nodes `num_nodes` and starts the health monitor by running the `health_monitor.py` script in a separate terminal window using `subprocess.Popen()`.

- `node_retry(tries,node,num_nodes)`: This function takes in the number of `tries` to retry, the failed `node` number, and the total number of nodes `num_nodes`. It retries starting the failed node by running the `node.py` script using `subprocess.Popen()`. It tries up to `tries` times before giving up. If the retry is successful, the function returns, otherwise it recursively calls itself with `tries` decremented by 1.

## storage/
The `storage/` directory is where the scraped data is stored. The `crawler.py` module stores the HTML content of each page it crawls in a file within the `storage/` directory. The name of the file is based on the URL of the page being crawled.

It is important to note that the storage directory should not be directly accessed by any other module of the project. The storage files are only accessed by the `crawler.py` module and should be accessed through the `content.py` module.

## generate_urls.py
This module generates a list of URLs for the crawler to use.

### Functions
`generate_urls(port)`: This function takes in a port number and generates a list of URLs based on that port number. It uses the validators library to ensure that the URLs are valid.

## Conclusion
This project involved building a distributed web crawler using Python, Flask, and Requests. The main goal of the project was to create a system that can crawl multiple websites in parallel, distribute the workload across multiple nodes, and generate a graph representation of the website structure.

To achieve this, we created a set of Flask endpoints that can receive requests for crawling, health checks, and graph generation. We also implemented a load-balancing system that can assign crawling tasks to worker nodes in a round-robin fashion. Finally, we used a data structure to keep track of the website structure and used it to generate the graph representation.

This project was a great learning experience for understanding the basics of distributed systems, network programming, and load balancing. It provided insights into how to design and implement a scalable and fault-tolerant system that can handle large amounts of data and traffic.
