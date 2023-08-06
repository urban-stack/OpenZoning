# the Open Zoning Feed Specification

**The Open Zoning Feed Specification (OZFS)** is the culmination of months of work by the Open Zoning team to define a first-of-its-kind national data language -- or, schema -- for zoning codes, allowing zoning codes to be machine-readable.   

**Term Definitions**
This section defines terms that are used throughout this document.
* **machine-readable**: in a form that computers can process
* **municipality data feed**: a municipality's collection of machine-readable zoning information, collected within the required files written in the required format as specified by the Open Zoning Feed Specification
* **schema**: file defining the format of zoning and municipality information, referenced by municipality data feed files

The OZFS defines the format and structure of the files needed to create a municipality's **municipality data feed**. A municipality's data feed is the collection of its zoning information into files written in Open Zoning's pre-defined language, a machine-readable language. Once the required files with the required zoning information have been created in OZ's lanaguage, machines can then access the files and read them simply by understanding our pre-defined zoning language.  

### Open Zoning Feed Specification
| file type | schemas | description |
| --- | --- | --- |
| *municipality file* | municipality schema | --- |
| *district file(s)* | districts file schema | --- |
| | constraints application schema | --- |
| | constraints value schema | --- |



## OZFS Files

The OZFS is comprised of two types of files, the *municipality file* and *district files*. Each **municipality data feed** has one municipality file but can and should have multiple district files. Both files are described in more detail below. For a **municipality data feed** to be considered complete by Open Zoning, it must:
1. contain a *district file* for each zoning district within the municipality, as listed within the *municipality file*
2. capture the following constraints for each allowed use for each residential zoned lot within its jurisdiction:
*  maximum height(s) (all height values -- e.g. wall, roof -- defined within the *municipality file*)
*  setback values (all setback values -- e.g. front, side, rear -- defined within the *municipality file*)
*  FAR
*  number of stories
*  required parking (if denoted as regulated within the *municipality file*)
*  minimum lot size (if denoted as regulated within the *municipality file*)
*  maxiumum lot size (if denoted as regulated within the *municipality file*)
*  maximum lot coverage (if denoted as regulated within the *municipality file*)

Formatting the the *municipality file* and *district files* are 4 Open Zoning schemas. These schmas define the structure of the zoning information language that these files must speak and that machines must be able to read.

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
| ***district*** | | object | required | --- |
| | *identifier* |string | required | --- |
| | *name* | string | required | --- |
| ***author*** | | string | required | --- |
| ***date created*** | | date | required | --- |
| ***last updated*** | | array | required | --- |
| ***constraints*** | | array of objects | required | --- |
| | *constraintsModule* | object | required | --- |
| | *lot* | object | required | --- |

2. ### constraints application schema  
The *constraints application schema* is structured as follows with the indicated properties and sub-properties, including the status of each: required, conditionally required, or not required.  

**notes**  
* Any of the following properties can be sub-properties of any other one, i.e. any property can be nested as a sub-property within any other property. The intent of this design is to allow the structure of the zoning code that is regulating the constraint to be captured as close as possible to how it is written.
* Any of the following properties can take a constraint module as a sub-property. Constraint modules are defined within the **constraints value schema** section.

| property | sub-property | type | required | description |
| --- | --- | --- | --- | --- |
| ***bulkOptionality*** | | array of objects | optional | --- |
| | *bulks* | array | required | --- |
| ***developmentOptionality*** | | array of objects | optional | --- |
| | *developmentType* | array | required | --- |
| | *primaryStructures* | array | conditionally required | --- |
| | *accessoryStructures* | array | conditionally required | --- |
| ***ADbulkOptionality*** | | array of objects | optional | --- |
| | *ADbulk* | array | required | --- |
| ***ADtypeOptionality*** | | array of objects | optional | --- |
| | *ADtype* | array | required | --- |
| ***disrictTypeGroups*** | | array of objects | optional | --- |
| | *districtTypes* | array | required | --- |

3. ### constraints values schema   
The *constraints values schema* is structured as follows with the indicated properties and sub-properties, including the status of each: required, conditionally required, or not required.
* (first property here

| constraint | sub-property | <div style="width:10px">sub-property</div> | sub-property | type | required | description |
| --- | --- | --- | --- | --- | ---| --- | 
| ***lotWidth*** | | | | object | optional | --- |
| | *minimum* | | | non-negative integer | required | --- |
| ***lotArea*** | | | | object | optional | --- |
| | *minimum* | | | non-negative integer | conditionally required | --- |
| | *maximum* | | | non-negative integer | conditionally required | --- |
| ***height*** | | | | object | optional | --- |
| | *wall* | | | object | conditionally required | --- |
| | | *maximum*| | non-negative integer | required | --- |
| | *roof* | | | object | conditionally required | --- |
| | | *maximum*| | non-negative integer | required | --- |
| ***setbacks*** | | | | object | optional | --- |
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
| ***lot coverage*** | | | | object | optional | --- |
| | *maximum* | | | non-negative integer | required | --- |
| ***FAR*** | | | | object | optional | --- |
| | *residential* | | | non-negative integer | required | --- |
| ***floorArea*** | | | | object | optional | --- |
| | *unit* | | | object | required | --- |
| | | *standard* | | object | conditionally required | --- |
| | | | *minimum* | non-negative integer | required | --- |
| | | *efficiecny* | | object | conditionally required | --- |
| | | | *minimum* | non-negative integer | required | --- |
| ***floorWidth*** | | | | object | optional | --- |
| | *minimum* | | | object | required | --- |
| | | *value* | | non-negative integer | required | --- |
| | | *applicableFloorArea* | | non-negative integer | optional | --- |
| ***stories*** | | | | object | optional | --- |
| | *maximum* | | | non-negative integer | conditionally required | --- |
| | *floorAreaContribution* | | | object | conditionally required | --- |
| | | *storyFloorElevation* | | object | conditionally required | --- |
| | | | *minimum* | non-negative integer | required | --- |
| | | | *floorAreaPerimeterPercentage* | non-negative integer | optional | --- |


###  

# OZFS Data Standard
A portion of OZFS's work is establishing a minimum viable set of "core" constraints || set of core bulking components that are necessary to bulking on any given lot across America. Our work-in-progress list of these constraints are captured within an Airtable titled [OZFS schema](https://airtable.com/invite/l?inviteId=invIE9Rq8BJxoRZe9&inviteToken=c24d20d82c00f933e02ca4d7f9b78088b2eaefcef049f3691df85eb48f858fbc&utm_medium=email&utm_source=product_team&utm_content=transactional-alerts). 

Within this table, each constraint is catagorized into a core component of what is known as bulking, which is the process through which structures take their form on a lot within the modern-day zoning concept (the bucket is titled "core bulking component"). OpenZoning considers these components to be the core devices through which modern society has used zoning to conceptualize and abstract the tangible resource of land as discrete containers for bulks, i.e. structures and buildings. These containers are called lots -- discrete areas of land plus the volumes of air above and earth beneath them -- and are the base units of zoning. When applied to the lot, modern society's conceptualization of land is executed through a set of components meant to control the realization of bulks (i.e. bulking) on these lots. They are:

- buildable area limits
- height limits 
- structure envelopes
- number of structures
- types of structures
- relationship between structures
- number of units limits
- types of floor use

This list is a work in progress, and correctly identifying these components is essential to OpenZoning's goal of creating a standard machine-readable format that can accomodate the wide swathe of zoning codes that exist across America, and across the world. 

_Will go here_

Testing/working files to go in [Examples folder](/examples)


## Constraint Classifying Structure
Stored in a hierarchy of:

- [lot](glossary.md#lot)
  - [structure](glossary.md#structure)
    - [story](glossary.md#story) (i.e. floor)

Structures and their constraints are nested within the above hierarchy:
- [bulk](glossary.md#building-mass) (option) (i.e. mass)
- [base](glossary.md#base)
  - [height](glossary.md#building-height)
  - [setback](glossary.md#setback)
  - plane

  
## Constraints & Modifiers
#### Edges:
- [front](glossary.md#frontage) (lot line)
- [rear](glossary.md#lot-line-rear) (lot line)
- [side](glossary.md#lot-line-side) (lot line)

#### Dimensions:
in ft / sq ft
- [width](glossary.md#width)
- [depth](glossary.md#depth)
- area
- [frontage](glossary.md#frontage)

#### Counts:
- min
- max
- numberOf
- per
  - [Acre]
  - [DU (dwelling unit)](glossary.md#dwelling-unit)
  - Lot


## Special Definitions

### roof
TBD

### max
when used as a _suffix_, defines or applies to the top-most floor, height, etc.

### corner

## other constraints
- [FAR](glossary.md#FAR) / [Floor Area](glossary.md#floor-area)
- Parking
- [Units](glossary.md#units)
- Use types
  - Use groups
    - Uses

## variants
### bonuses


## Open questions:
- how to store ratios/formulas
  - purely numeric (e.g. `6:1` sky exposure plane)
  - relating to fixed figures (e.g. height can be 2X lot width)
  - relating to development decisions (e.g. tower can contain at most 45% of lot FAR)
