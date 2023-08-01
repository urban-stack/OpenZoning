# Open Zoning Feed Specification Schemas

There are 4 Open Zoning schemas that dictate the format of information within the two types of feed files, the municipality file and district files.

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

