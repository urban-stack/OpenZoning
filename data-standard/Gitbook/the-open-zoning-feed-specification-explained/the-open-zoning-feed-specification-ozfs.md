---
description: the nitty-gritty of the OZFS
---

# 🌟 the Open Zoning Feed Specification (OZFS)

## Table of contents

* [**Feeds and machine readability**](the-open-zoning-feed-specification-ozfs.md#feeds-and-machine-readability)
* [**a municipality data feed**](the-open-zoning-feed-specification-ozfs.md#a-municipality-data-feed)
* [**OZFS files**](the-open-zoning-feed-specification-ozfs.md#ozfs-files)
* [**OZFS file schemas**](the-open-zoning-feed-specification-ozfs.md#ozfs-file-schemas)

***

## Feeds and machine readability

The Open Zoning Feed Specification specifies how a data feed of zoning data should be structured and formatted in order to be successfully machine-readable. A data feed is a set of data written in a machine-readable language. Machine-readable languages are created specifically to be able to communicate the unique semantic structures of the data that it was designed to communicate. Therefore, any computer hoping to read and process a data feed must speak its specific language, and thus be able make sense of it.

## a municipality data feed

The OZFS is a rule book that allows municipalities to create their own data feed of zoning data, i.e. their unique **municipality data feed**. A municipality's data feed is the collection of its zoning information into files written in Open Zoning's pre-defined machine-readable language. Once the required files with the required zoning information have been created in OZ's language, machines can then understand a municipality's zoning.

## OZFS files

The OZFS is made up of only two types of files, the _municipality file_ and _district files_. Each **municipality data feed** has one municipality file but can and should have multiple district files. A **municipality data feed** is simply an online database with these two types of files in it. Both files are described in detail in the **OZFS Files and File Schemas, explained in detail** section.

## OZFS file schemas

Formatting the _municipality file_ and _district files_ are 4 Open Zoning schemas, i.e. instructions for the language that their contents must be written in, including what information is required, conditionally required, and optional. These schemas define the language and the structure of the zoning information language that these files must speak and that machines must be able to read. The Open Zoning schemas live as json files (a type of data meta-language) within this Github repository and are listed in the table below. They have been translated from their json format into a more human-readable form within the next section, **OZFS Files and File Schemas, explained in detail.**

### **Open Zoning Feed Specification structure**

| file              | schema                             | description |
| ----------------- | ---------------------------------- | ----------- |
| municipality file | municipality file schema           | ...         |
| districts file    | districts file schema              | ...         |
|                   | --> constraints application schema | ...         |
|                   | ---> constraints values schema     | ...         |



**Diagrams showing files-schemas relationships**

<figure><img src="broken-reference" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="broken-reference" alt="" width="563"><figcaption></figcaption></figure>
