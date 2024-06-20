import petl as etl

# viewing data and preparing db column names
data = etl.fromcsv('Data/covid_edu/scripts/csv/transit_data.csv')
columns = {
    'Countries and territories':'Country',
    'Number of learners enrolled from pre-primary to upper-secondary education':'FormalEnrolment',
    'Number of learners enrolled in tertiary education programmes':'TertiaryEnrolment',
    'Additional information':'AdditionalInformation' 
}
to_view = data.rename(columns)
to_db = to_view


# converting relevant columns to integer for operations later 
to_db = etl.convert(to_db, ('TertiaryEnrolment','FormalEnrolment'), lambda i: int(float(i)))
to_view = etl.convert(to_db, ('TertiaryEnrolment','FormalEnrolment'), lambda i: int(float(i)))


# removing TOTAL column by selecting all except TOTAL row
to_sort = etl.select(to_db, lambda tot: tot['Country'] != 'TOTAL')
# verifying TOTAL has been removed
# print(etl.tail(to_sort))


# here, the database ingest file's numeric columns are formatted for legibility or usability
to_view = etl.convert(to_view, ('FormalEnrolment', 'TertiaryEnrolment'), lambda num : '{:,.0f}'.format(num))
# print(to_view)


# removing unneeded columns
to_db, to_db = etl.cutout(to_view, ''), etl.cutout(to_db, '')


# saving a version without the level of legibility characters provide but sorting capable since integers
impact = to_view.tocsv('Data/covid_edu/scripts/csv/impact_db.csv')
# saving to_db as a csv file to import into a database and handle queries
ingest = to_db.tocsv('Data/covid_edu/scripts/csv/ingest_db.csv')
