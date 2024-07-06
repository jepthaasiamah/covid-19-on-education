### gathering, transformation, database ingestion and exploratory analysis
https://en.wikipedia.org/wiki/Impact_of_the_COVID-19_pandemic_on_education

<h3> Introduction</h3>
<p>In this project, I use Python's libraries to extract information from Wikipedia about the impact of Covid-19 on education. This data may be relevant for ingestion into a database with the right data transformation based on well-defined requirements. In this project, I have created a database with tables suitable for easy referencing or legibility and one for running SQL queries effectively. </p>
<img src="assets/wikipedia_shot.png">

<h3> Scenario</h3>
<p>Covid-19 has affected society in many different ways... 
The pandemic has had various impacts on our society; enrollment in educational institutions across populous nations and details about the duration provided may reveal differing attitudes. </p>

<p> wikipedia: " The COVID-19 pandemic affected educational systems across the world.[1] The number of cases of COVID-19 started to rise in March 2020 and many educational institutions and universities underwent closure. Most countries decided to temporarily close educational institutions to reduce the spread of COVID-19. UNESCO estimates that at the height of the closures in April 2020, national educational shutdowns affected nearly 1.6 billion students in 200 countries: 94% of the student population and one-fifth of the global population. "</p>

<h3> Data collection</h3>
<p> To gather the data, I used Python's intuitive web scraping library, 'BeautifulSoup' to send a request to the website host. Inspecting the site reveals some details to pick the specific data needed; the HTML class 'wikitable sortable' is its implementation. For pulling columns and rows the library provides a parser which looks for the relevant HTML tags, 'th' and 'tr' respectively. </p>
<img src="assets/soup_script_!.jpg">

<p> In the screenshot above, the code implementation can be observed. The code imports the 'Request' and 'BeautifulSoup', libraries which are used to get a response from the website host and to pull data under the specified HTML class table. Using the 'th' and 'tr' tags which specify columns and rows in HTML (hypertext markup language), 'BeautifulSoup' can find data from specific tables. In this code snippet, the 'table[0]' value represents the first table, 'Country-wide school closures by country/territory'. </p>

<h3> Data transformation</h3>
<p>After the table as a CSV file, several columns contained null values. Using 'Pandas', 
After reading the CSV file into a 'Pandas' frame, I checked for null values as the first inspection revealed some mostly empty columns; some columns in the raw data contain multiple data types. These inconsistencies can occur when gathering data so transformation is empirical. </p>

<img src='assets/messy_data.png'>
<p> There are three main problems with the data gathered from the internet. Not all the data is under the correct field names, null values are present in multiple columns and spelling errors in the first column containing the names of relevant countries or territories. Null columns are unneeded, however, upon investigating each null column since some contain column names and potentially more misplaced data. To improve usability, it is good to make these changes. </p>
  
<p>The table contains five columns, 'Country or territories', 'Number of learners enrolled from pre-primary to upper-secondary education', 'Number of learners enrolled in tertiary education programmes', 'Additional Information ' and 'Ref'].</p>

<img src="assets/transit_data.png">
<ol type="a">
  <li>Data in wrong columns can be noticed starting with field names in the first record, index 0.</li>
  <li>Null columns contain misplaced values that may be part of the table. </li>
  <li>The first column can serve as a primary identifier, however it contains spelling errors.</li>
</ol>

<p> Created a grammar function seen here which checks for grammatical errors using the SpellChecker Python module to make corrections on wrongly spelt nations in the 'Countries and Territories' field. It can be seen in a shot above, 'Austriag' which should be 'Austria.' This error inspired this function since correcting errors in a CSV file can be very timely. After running this function on ['Countries and territories' and 'Additional information'], I can be sure each word is spelt correctly in the transformed data. </p>

<img src='assets/spellling_checker.png'>

<h5> Data Modelling using petl, ETL library </h5>
<p> The first task I took on, now with some viable data gathered was to modify column names. Simple field names, ['Country', 'FormalEnrolment', 'TertiaryEnrolment', 'AdditionalInformation'] simplifies the table for data ingestion. 
<p>I decided to create two CSV files, one with comma formatting for the numbers as they are hard to identify at first glance. The second file contains manipulative numeric data which is stored as an integer instead of 'string' as with the other file. This provides options to those with access.</p>
<img src='assets/to_database.png'>
<img src='assets/to_db.png'>
<p></p>

<p>It may be useful to add this data to a database as part of record keeping and for efficient access. To do this, SQL has various data control languages to create, model and query databases so I created a local server using a Microsoft SQL Server container installed in an isolated environment via virtualisation software, 'Docker'.
One csv file contains comma formatting for numeric values which makes it easy to read the information and the other contains th. This was sent into  I named 'Ingest.db' and the other 'Impact.db' </p> 

<h5>Querying the database</h5>
<p>With data modelled in our database, using SQL queries is a fantastic way to investigate various insights by asking different questions about it.</p>
<img src='assets/sql_query.png'>

<p>
  Within a few SQL queries, I was able to unpack useful information from the data. 
  <ol type='a'>
    <li>A query displays nations with no enrolment during the pandemic</li>
        <img src='assets/dbvis_q.png'>
    <li>Top 10 Nations with the most number of formally enrolled students from greatest to lowest </li>
        <img src='assets/identifier_wrong.png'>
    <li></li>
  </ol>
</p>

<p> It was after this, I realised spelling errors were still present. After creating another database with a grammatically correct primary column and attempting to join results from the original database containing comma formatting on metrics, I noticed the omission of all the incorrect nation names as they were not a match. </p>
<p> In the screenshot below, I ran another query; it combines results from the comma formatted metrics table ('Impact') and evaluates the condition using the numerically formatted metrics table ('Ingest'). </p>
<img src='assets/identifier_right.png'>
<p> The sixth country is 'Azerbaijan' whereas in the top ten nations by formal enrolment, the sixth country is 'Austriag'; appropriate primary key columns allow the SQL join statement to combine relevant records. </p>
<img src='assets/primary_key.png'>
<p> In the image above, the correct spellings for each row of primary key, 'Country' are registered in the database, 'Covid_Education_Report'</p>
<p>The query below shows metrics formatted by commas for easy reading of information. With multiple versions of the transformed data, developers or enthusiasts may be able to analyse insights, expand on the research or incorporate it in a report or application. 
Here's one last query to display the available information.</p>
<img src='assets/final_query.png'>

<h5>Reflective </h5>
<p> This is an example of the potential beyond gathering data online. The procedure almost always precedes the process of improving usability allowing for record keeping or interpretation. </p>
