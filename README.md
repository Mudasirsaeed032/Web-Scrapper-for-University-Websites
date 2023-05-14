# Web-Scrapper-for-University-Websites
The University Website Data Analysis and Visualization Tool is a web scraping application designed to extract data from three different university websites in Pakistan. By scraping five web pages from each university, the tool collects valuable information for analysis and visualization.

The application utilizes the power of web scraping using Python's requests and urllib libraries to fetch the webpage content. It then leverages the spacy library for natural language processing (NLP) tasks such as noun and verb extraction.

Once the data is collected, the tool performs comprehensive analysis by comparing the three university websites in terms of adjectives, verbs, and nouns. The frequency and distribution of these linguistic elements are calculated, providing insights into the characteristics and emphasis of each university's web content.

To enhance understanding and visualization of the gathered data, the tool employs the networkx and matplotlib libraries. It constructs a graph representation, where nouns are considered nodes, and two nouns are connected if they occur in the same sentence. The resulting graph highlights relationships and connections between different nouns, revealing the semantic structure of the university website content.

The University Website Data Analysis and Visualization Tool provides several key metrics for each website, including the number of connected components within the graph. Additionally, it identifies the top 10 nouns with the highest degree, indicating the most prominent and central terms in the website content. This information offers valuable insights into the themes and focus areas of each university's online presence.

Moreover, the tool allows users to explore the proximity of nouns to the term "quality" within a distance of less than five. It retrieves all nouns found in the selected pages containing "quality," enabling users to identify related concepts and evaluate their prominence within the context of quality.

This project incorporates various Python libraries, including networkx, matplotlib, spacy, and pandas, to facilitate graph construction, visualization, and data manipulation.

The University Website Data Analysis and Visualization Tool provides a comprehensive and efficient solution for extracting, analyzing, and visualizing data from university websites. It offers valuable insights into linguistic patterns and semantic connections, enabling users to gain a deeper understanding of the content and themes present on these websites.


# HOW TO RUN
Install the required libraries:

networkx: Install using pip install networkx.
spacy: Install using pip install spacy. Download the English language model using python -m spacy download en_core_web_sm.
pandas: Install using pip install pandas.
matplotlib: Install using pip install matplotlib.
requests: Install using pip install requests.
urllib: Install using pip install urllib3.
BeautifulSoup: Install using pip install beautifulsoup4.
dframcy: Install using pip install dframcy.
Prepare your URLs:

Modify the urluaar1, urluet, urlcomsats1, and urlcomsats2 variables with the desired URLs of the university websites you want to scrape.
Run the code:

Execute the code, and it will scrape the specified university websites and store the data in separate text files: Uaar.txt, Uet.txt, and Comsats.txt.
The code will prompt you to choose a university website by entering a number (1, 2, or 3).
Enter the corresponding number and press Enter.
The code will perform analysis on the chosen university's web content, including extracting nouns, adjectives, and verbs, and displaying their frequencies.
It will also construct a graph showing the connections between the nouns based on co-occurrence in sentences.
Additionally, it will display the top 10 nouns with the highest weighted degree and print the five words near the word "Quality" within the selected university's content.
Note: Ensure that you have a stable internet connection to fetch the website data successfully.

Remember to have the required permissions to scrape the university websites, as some websites may have restrictions or terms of use.
