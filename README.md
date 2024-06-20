# covid-19 impact-on-education
### gathering, transformation and exploratory analysis
https://en.wikipedia.org/wiki/Impact_of_the_COVID-19_pandemic_on_education

<h2>Introduction</h2>
<p>In this project, I use Python's libraries to extract information from Wikipedia about the impact of Covid-19 on education. This data may be relevant for ingestion into a database with the right data transformation based on well-defined requirements. In this project, I have created a database with tables suitable for easy referencing or legibility and one for running SQL queries effectively. </p>
<img src="assets/wikipedia_shot.png">

<h2>Scenario</h2>
<p>Covid-19 has affected society in many different ways... 
The pandemic has had various impacts on our society; enrollment in educational institutions across populous nations and details about the duration provided may reveal differing attitudes. </p>

<p>From wikipedia: " The COVID-19 pandemic affected educational systems across the world.[1] The number of cases of COVID-19 started to rise in March 2020 and many educational institutions and universities underwent closure. Most countries decided to temporarily close educational institutions to reduce the spread of COVID-19. UNESCO estimates that at the height of the closures in April 2020, national educational shutdowns affected nearly 1.6 billion students in 200 countries: 94% of the student population and one-fifth of the global population. "</p>

<h2>Data collection</h2>
<p>To gather the data, I used Python's intuitive web scraping library, 'BeautifulSoup' to send a request to the website host. Inspecting the site reveals some details to pick the specific data needed; the HTML class 'wikitable sortable' is its implementation. For pulling columns and rows the library provides a parser which looks for the relevant HTML tags, 'th' and 'tr' respectively. </p>
<img src="assets/soup_script_!.jpg">

<p>In the screenshot above, the code implementation can be observed. The code imports the 'Request' and 'BeautifulSoup', libraries which are used to get a response from the website host and to pull data under the specified HTML class table. Using the 'th' and 'tr' tags which specify columns and rows in HTML (hypertext markup language), 'BeautifulSoup' can find data from specific tables. In this code snippet, the 'table[0]' value represents the first table, 'Country-wide school closures by country/territory'.

<h2>Data transformation</h2>
After the table had been saved as a CSV file, several columns contained null values. Using the 'Pandas' library, I conducted some cleaning and transformation to prepare it for succinct exploratory analysis. After reading the CSV file into a 'Pandas' frame, I checked for null values as the first inspection revealed some mostly empty columns. Some columns contain multiple data types as well which are a consequence of parsing markup language on Wikipedia into a readable form.
The first table can be seen containing five columns, 'Country or territories', 'Number of formal', 'Additional Information', 'Ref']

<img src='assets/raw_data.png'>
<b>raw data here </b>

There are three main problems with the data gathered from the internet. Not all the data is in the right columns, there are several null values in multiple columns and there are mistakes in the first column which contains the names of relevant countries or territories. Null columns are not needed and have just been collated to our web-gathering effort however I decided to investigate each null column since some contain column names and potentially more misplaced data. To improve the usability it is important to make these changes.

<ol type="a">
  <li>Data in the wrong columns can be noticed with field names as the first record, index 0.</li>
  <li>Null columns containing some useful, misplaced data. </li>
  <li>First column can be a primary identifier however it contains spelling errors</li>
</ol>

code snippet here <img src='assets/missing_details_script.png'> 

This screenshot shows the code responsible for extracting non-null values from the messy data which we are currently cleaning. 

<h6> final transformed data <img src="assets/clean_data_out.png"> </h6>

In the final shot here, it can be seen that all columns contain appropriate, accurate data. All missing information or misplacements due to extra commas in the comma-separated values file or unavoidable errors from data gathering. Easy to perform sorting and indexing 
Created a grammar function seen here which checks for grammatical errors using the SpellChecker Python module to make corrections on wrongly spelt words firstly in the 'Countries and Territories' column. It can be seen in a shot above, 'Austriag' which should be 'Austria.' This error inspired this function since correcting errors in a CSV file can be very timely. After running this function on ['Countries and territories' and 'Additional information'], I can be sure each word is spelt correctly in the transformed data.

<h6> Checking spelling <img src='assets/spellling_checker.png'> </h6>

Converted to floating point numerical values where it was relevant. To do so it was a simple matter of changing the characters using the 'Numpy' Python library. With this result, it is much easier to sort by those numeric data points, namely, 'Number of learners enrolled in primary and secondary education programmes' and 'Number of learners enrolled in tertiary education programmes.' Then in the next rotation, I decided to perform some simple distribution analysis. To analyse the significance of these numbers, I think I could collect some data on the populations of these nations. I thought to use a percentile calculator to find the nations which are above or at the 75th quartile.

<h4> Extract, transform, load </h4>
Now with 

<h4>Reflective </h4>
It may be useful to add this data to a database as part of record keeping and for efficient access. To do this, SQL has various data control languages to create, model and query databases so I created a local server using a Microsoft SQL Server container installed in an isolated environment via an application called 'Docker'.
One csv file contains comma formatting for numeric values which makes it easy to read the information and . This file I named 'Ingest.db' and the other

