# Open Zoning Feed Specification Schemas

There are 4 Open Zoning schemas that dictate the format of information within the two types of feed files, the municipality file and district files.

### Field types
* Date - Service day in the YYYYMMDD format. Since time within a service day can be above 24:00:00, a service day often contains information for the subsequent day(s).
Example: 20180913 for September 13th, 2018.
* Email - An email address.
  Example: example@example.com
Enum - An option from a set of predefined constants defined in the "Description" column.
Example: The route_type field contains a 0 for tram, a 1 for subway...
ID - An ID field value is an internal ID, not intended to be shown to riders, and is a sequence of any UTF-8 characters. Using only printable ASCII characters is recommended. IDs defined in one .txt file are often referenced in another .txt file.
Example: The stop_id field in stops.txt is a ID. The stop_id field in stop_times.txt is an ID referencing stops.stop_id.
Language Code - An IETF BCP 47 language code. For an introduction to IETF BCP 47, refer to http://www.rfc-editor.org/rfc/bcp/bcp47.txt and http://www.w3.org/International/articles/language-tags/.
Example: en for English, en-US for American English or de for German.
Latitude - WGS84 latitude in decimal degrees. The value must be greater than or equal to -90.0 and less than or equal to 90.0.
Example: 41.890169 for the Colosseum in Rome.
Longitude - WGS84 longitude in decimal degrees. The value must be greater than or equal to -180.0 and less than or equal to 180.0.
Example: 12.492269 for the Colosseum in Rome.
Non-negative Float - A floating point number greater than or equal to 0.
Non-negative Integer - A integer greater than or equal to 0.
Phone number - A phone number.
Time - Time in the HH:MM:SS format (H:MM:SS is also accepted). The time is measured from "noon minus 12h" of the service day (effectively midnight except for days on which daylight savings time changes occur. For more information, see the guidelines article). For times occurring after midnight, enter the time as a value greater than 24:00:00 in HH:MM:SS local time for the day on which the trip schedule begins.
Example: 14:30:00 for 2:30PM or 25:35:00 for 1:35AM on the next day.
Text - A string of UTF-8 characters, which is aimed to be displayed and which must therefore be human readable.
Timezone - TZ timezone from the https://www.iana.org/time-zones. Timezone names never contain the space character but may contain an underscore. Refer to http://en.wikipedia.org/wiki/List_of_tz_zones for a list of valid values.
Example: Asia/Tokyo, America/Los_Angeles or Africa/Cairo.
URL - A fully qualified URL that includes http:// or https://, and any special characters in the URL must be correctly escaped. See the following http://www.w3.org/Addressing/URL/4_URI_Recommentations.html for a description of how to create fully qualified URL values.

## Municipality file  

Information in the Municipality file is formatted per the **municipality Schema**. The schema is structured as follows with the indicated properties and sub-properties, including the status of each: required, conditionally required, or not required.
* love
  - love

## district files  

Information in the district files is formatted per three nested schemas: 1. the **district file schema**, which internally references the 2. **constraints application schema**, which, in turn, internally references the 3. **constraints values schema**. 

1. ### districts file schema  
The **districts file schema** is structured as follows with the indicated properties and sub-properties, including the status of each: required, conditionally required, or not required.
* *district*
  * *identifier* [required] (type: string, value: can be the code-specified abbreviation of any zoning district)
  * *name* [required] (type: string, value: the full name of the zoning district, as specified in the zoning code)
* *author* [required] (type: string, value: the name of the author who created the file, optionally accompanied by their organization and/or affiliation)
* *date created* [required] (type: date, value: the date the file was created)
* *last updated* [required] (type: a 2-dimensional array (type_1: date, value: the date of the last time the file was edited, type_2: string, value: the name of the author who created the file, optionally accompanied by their organization and/or affiliation)
* *constraints* [required] (type: an array of objects)
  * (objects formatted according to the **constraints application schema**)

2. ### constraints application schema  
The *constraints application schema* is structured as follows with the indicated properties and sub-properties, including the status of each: required, conditionally required, or not required.
* (first property here)

3. ### constraints values schema   
The *constraints values schema* is structured as follows with the indicated properties and sub-properties, including the status of each: required, conditionally required, or not required.
* (first property here

