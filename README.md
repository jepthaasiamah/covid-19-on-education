# covid-19 impact-on-education
### gathering, transformation, exploratory analysis and database ingestion
https://en.wikipedia.org/wiki/Impact_of_the_COVID-19_pandemic_on_education

<h2>Introduction</h2>
<p>In this project, I use Python's libraries to extract information from Wikipedia about the impact of Covid-19 on education. This data may be relevant for ingestion into a database with the right data transformation based on well-defined requirements. In this project, I have created a database with tables suitable for easy referencing or legibility and one for running SQL queries effectively. </p>
<img src="assets/wikipedia_shot.png">

<h2>Scenario</h2>
<p>Covid-19 has affected society in many different ways... 
The pandemic has had various impacts on our society; enrollment in educational institutions across populous nations and details about the duration provided may reveal differing attitudes. </p>

<p>wikipedia: " The COVID-19 pandemic affected educational systems across the world.[1] The number of cases of COVID-19 started to rise in March 2020 and many educational institutions and universities underwent closure. Most countries decided to temporarily close educational institutions to reduce the spread of COVID-19. UNESCO estimates that at the height of the closures in April 2020, national educational shutdowns affected nearly 1.6 billion students in 200 countries: 94% of the student population and one-fifth of the global population. "</p>

<h2>Data collection</h2>
<p>To gather the data, I used Python's intuitive web scraping library, 'BeautifulSoup' to send a request to the website host. Inspecting the site reveals some details to pick the specific data needed; the HTML class 'wikitable sortable' is its implementation. For pulling columns and rows the library provides a parser which looks for the relevant HTML tags, 'th' and 'tr' respectively. </p>
<img src="assets/soup_script_!.jpg">

<p>In the screenshot above, the code implementation can be observed. The code imports the 'Request' and 'BeautifulSoup', libraries which are used to get a response from the website host and to pull data under the specified HTML class table. Using the 'th' and 'tr' tags which specify columns and rows in HTML (hypertext markup language), 'BeautifulSoup' can find data from specific tables. In this code snippet, the 'table[0]' value represents the first table, 'Country-wide school closures by country/territory'. </p>

<h2>Data transformation</h2>
<p>After the table as a CSV file, several columns contained null values. Using 'Pandas', 
After reading the CSV file into a 'Pandas' frame, I checked for null values as the first inspection revealed some mostly empty columns; some columns in the raw data contain multiple data types. These inconsistencies can occur when gathering data so transformation is empirical. 
The table contains five columns, 'Country or territories', 'Number of learners enrolled from pre-primary to upper-secondary education', 'Number of learners enrolled in tertiary education programmes', 'Additional Information ' and 'Ref']</p>
<img src='assets/raw_data.png'>
<p>There are three main problems with the data gathered from the internet. Not all the data is under the correct field names, null values are present in multiple columns and spelling errors in the first column containing the names of relevant countries or territories. Null columns are unneeded, however, upon investigating each null column since some contain column names and potentially more misplaced data. To improve usability, it is good to make these changes.</p>

<img src='assets/raw_data.png'>

<ol type="a">
  <li>Data in wrong columns can be noticed starting with field names in the first record, index 0.</li>
  <li>Null columns contain misplaced values that may be part of the table. </li>
  <li>The first column can serve as a primary identifier, however it contains spelling errors.</li>
</ol>
<img src='assets/missing_details_script.png'> 

<img src="assets/clean_data_out.png">

In the shot above, all columns contain appropriate, accurate data. The details which were misplaced have also been extracted for the various countries using 'Countries and territories' as the key since it is a primary identifier for each record. 

<p> Created a grammar function seen here which checks for grammatical errors using the SpellChecker Python module to make corrections on wrongly spelt nations in the 'Countries and Territories' field. It can be seen in a shot above, 'Austriag' which should be 'Austria.' This error inspired this function since correcting errors in a CSV file can be very timely. After running this function on ['Countries and territories' and 'Additional information'], I can be sure each word is spelt correctly in the transformed data. </p>

<img src='assets/spellling_checker.png'>

<h4> Extract, transform, load </h4>
<p> The first task I took on, now with some viable data gathered was to modify column names. Using the 
<p>Now with an idea of the final data, I atarted thinking of use cases such as ingestion into a database. I decided to create two CSV files, one with comma formatting for the numbers as they are hard to identify at first glance. The second file contains manipulative numeric data which is stored as an integer instead of 'string' as with the other file. This provides options to those with access.</p>
<img src='assets/etl.png'>

<p>It may be useful to add this data to a database as part of record keeping and for efficient access. To do this, SQL has various data control languages to create, model and query databases so I created a local server using a Microsoft SQL Server container installed in an isolated environment via virtualisation software, 'Docker'.
One csv file contains comma formatting for numeric values which makes it easy to read the information and the other contains th. This was sent into  I named 'Ingest.db' and the other 'Impact.db' </p> 

<h4>Reflective </h4>
<p></p>
