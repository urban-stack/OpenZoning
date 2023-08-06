# Open Zoning Feed Specification Schemas

There are 4 Open Zoning schemas that dictate the format of information within the two types of feed files, the municipality file and district files.

### Field types
* Date - Service day in the YYYYMMDD format. Since time within a service day can be above 24:00:00, a service day often contains information for the subsequent day(s).
Example: 20180913 for September 13th, 2018.
* Email - An email address.
  Example: example@example.com
* Enum - An option from a set of predefined constants defined in the "Description" column.
Example: The route_type field contains a 0 for tram, a 1 for subway...
* ID - An ID field value is an internal ID, not intended to be shown to riders, and is a sequence of any UTF-8 characters. Using only printable ASCII characters is recommended. IDs defined in one .txt file are often referenced in another .txt file.
Example: The stop_id field in stops.txt is a ID. The stop_id field in stop_times.txt is an ID referencing stops.stop_id.
* Language Code - An IETF BCP 47 language code. For an introduction to IETF BCP 47, refer to http://www.rfc-editor.org/rfc/bcp/bcp47.txt and http://www.w3.org/International/articles/language-tags/.
Example: en for English, en-US for American English or de for German.
* Latitude - WGS84 latitude in decimal degrees. The value must be greater than or equal to -90.0 and less than or equal to 90.0.
Example: 41.890169 for the Colosseum in Rome.
* Longitude - WGS84 longitude in decimal degrees. The value must be greater than or equal to -180.0 and less than or equal to 180.0.
Example: 12.492269 for the Colosseum in Rome.
* Non-negative Float - A floating point number greater than or equal to 0.
* Non-negative Integer - A integer greater than or equal to 0.
* Phone number - A phone number.
* Time - Time in the HH:MM:SS format (H:MM:SS is also accepted). The time is measured from "noon minus 12h" of the service day (effectively midnight except for days on which daylight savings time changes occur. For more information, see the guidelines article). For times occurring after midnight, enter the time as a value greater than 24:00:00 in HH:MM:SS local time for the day on which the trip schedule begins.
Example: 14:30:00 for 2:30PM or 25:35:00 for 1:35AM on the next day.
* Text - A string of UTF-8 characters, which is aimed to be displayed and which must therefore be human readable.
* URL - A fully qualified URL that includes http:// or https://, and any special characters in the URL must be correctly escaped. See the following http://www.w3.org/Addressing/URL/4_URI_Recommentations.html for a description of how to create fully qualified URL values.

## Municipality file  

Information in the Municipality file is formatted per the **municipality Schema**. The schema is structured as follows with the indicated properties and sub-properties, including the status of each: required, conditionally required, or not required.
* love
  - love

## District files  

Information in the district files is formatted per three nested schemas: 1. the **district file schema**, which internally references the 2. **constraints application schema**, which, in turn, internally references the 3. **constraints values schema**. 

1. ### districts file schema  
The **districts file schema** is structured as follows with the indicated properties and sub-properties, including the status of each: required, conditionally required, or not required.

| property | sub-property | type | required | description |
| --- | --- | --- | --- | --- |
| *district* | | object | required | --- |
| | *identifier* |string | required | --- |
| | *name* | string | required | --- |
| *author* | | string | required | --- |
| *date created* | | date | required | --- |
| *last updated* | | array | required | --- |
| *constraints* | | array of objects | required | --- |
| | *constraintsModule* | object | required | --- |
| | *lot* | object | required | --- |

2. ### constraints application schema  
The *constraints application schema* is structured as follows with the indicated properties and sub-properties, including the status of each: required, conditionally required, or not required.  

**notes**  
* Any of the following properties can be sub-properties of any other one, i.e. any property can be nested as a sub-property within any other property. The intent of this design is to allow the structure of the zoning code that is regulating the constraint to be captured as close as possible to how it is written.
* Any of the following properties can take a constraint module as a sub-property. Constraint modules are defined within the **constraints value schema** section.

| property | sub-property | type | required | description |
| --- | --- | --- | --- | --- |
| *bulkOptionality* | | array of objects | optional | --- |
| | *bulks* | array | required | --- |
| *developmentOptionality* | | array of objects | optional | --- |
| | *developmentType* | array | required | --- |
| | *primaryStructures* | array | conditionally required | --- |
| | *accessoryStructures* | array | conditionally required | --- |
| *ADbulkOptionality* | | array of objects | optional | --- |
| | *ADbulk* | array | required | --- |
| *ADtypeOptionality* | | array of objects | optional | --- |
| | *ADtype* | array | required | --- |
| *disrictTypeGroups* | | array of objects | optional | --- |
| | *districtTypes* | array | required | --- |

3. ### constraints values schema   
The *constraints values schema* is structured as follows with the indicated properties and sub-properties, including the status of each: required, conditionally required, or not required.
* (first property here

| constraint | sub-property | <div style="width:100px">sub-property</div> | sub-property | type | required | description |
| --- | --- | --- | --- | --- | ---| --- | 
| *lotWidth* | | | | object | optional | --- |
| | *minimum* | | | non-negative integer | required | --- |
| *lotArea* | | | | object | optional | --- |
| | *minimum* | | | non-negative integer | conditionally required | --- |
| | *maximum* | | | non-negative integer | conditionally required | --- |
| *height* | | | | object | optional | --- |
| | *wall* | | | object | conditionally required | --- |
| | | *maximum*| | non-negative integer | required | --- |
| | *roof* | | | object | conditionally required | --- |
| | | *maximum*| | non-negative integer | required | --- |
| *setbacks* | | | | object | optional | --- |
| | *front* | | | non-negative integer | required | --- |
| | *rear* | | | non-negative integer | required | --- |
| | *side* | | | object | required | --- |
| | | *interior* | | non-negative integer | required | --- |
| | | *corner* | | non-negative integer | conditionally required | --- |
| | | *bulkOptionality* | | non-negative integer | optional | --- |
| | | | (see **constraints application schema** section) | non-negative integer | required | --- |
| | | | *interior* | non-negative integer | required | --- |
| | | | *corner* | non-negative integer | conditionally required | --- |
| | *fromAnotherStructure* | | | non-negative integer | optional | --- |
| | | *primaryResidentialStructure* | | non-negative integer | conditionally required | --- |
| | | *habitableDwelling* | | non-negative integer | conditionally required | --- |
| | *bulkOptionality* | | | non-negative integer | optional | --- |
| | | (any *setbacks* property) | | n/a | n/a | --- |
| *lot coverage* | | | | object | optional | --- |
| | *maximum* | | | non-negative integer | required | --- |
| *FAR* | | | | object | optional | --- |
| | *residential* | | | non-negative integer | required | --- |
| *floorArea* | | | | object | optional | --- |
| | *unit* | | | object | required | --- |
| | | *standard* | | object | conditionally required | --- |
| | | | *minimum* | non-negative integer | required | --- |
| | | *efficiecny* | | object | conditionally required | --- |
| | | | *minimum* | non-negative integer | required | --- |
| *floorWidth* | | | | object | optional | --- |
| | *minimum* | | | object | required | --- |
| | | *value* | | non-negative integer | required | --- |
| | | *applicableFloorArea* | | non-negative integer | optional | --- |
| *stories* | | | | object | optional | --- |
| | *maximum* | | | non-negative integer | conditionally required | --- |
| | *floorAreaContribution* | | | object | conditionally required | --- |
| | | *storyFloorElevation* | | object | conditionally required | --- |
| | | | *minimum* | non-negative integer | required | --- |
| | | | *floorAreaPerimeterPercentage* | non-negative integer | optional | --- |


