# 📦 Parcel-resolved zoning information dataset

Open Zoning's hosted **Parcel-resolved zoning information dataset** contains machine-readable constraint values for all combinations of zoning districts within a Municipality whose "[highest and best use](../the-open-zoning-feed-specification-explained/definitions-for-frequently-used-terms.md)" is a [missing middle housing](../the-open-zoning-feed-specification-explained/definitions-for-frequently-used-terms.md) typology.

Constraint conditions and values for each zoning combination are recorded within a single JSON file and categorized by each use that is allowed within that zoning combination, as recorded in the "allowedUses" constraint in the file for each combination's base district. Within each file is a list of parcels whose constraints are regulated by that unique combination of zoning districts.

Parcels are identified using the local Municipality's parcel Identification, or parcel ID, system. For a given Municipality, the constraints that values are recorded for within each file are dictated by the Municipality's list of regulated constraints, as is recorded in the "districtsHeirarchy" property within the Municipality File for each Municipality.&#x20;

The zoning combinations JSON files are regulated by the "parcel-resolved zoning schema", which references the "[constraint values schema](../the-open-zoning-feed-specification-explained/ozfs-files-and-file-schemas-explained-in-detail.md)" for recording all constraint values.

## parcel-resolved zoning schema

<table><thead><tr><th width="155">property</th><th width="175">sub-property</th><th>type</th><th>required</th><th>description</th></tr></thead><tbody><tr><td>district</td><td></td><td>object</td><td>required</td><td></td></tr><tr><td></td><td>identifier</td><td>string</td><td>required</td><td></td></tr><tr><td></td><td>name</td><td>string</td><td>required</td><td></td></tr><tr><td></td><td>districtType</td><td>string</td><td>required</td><td></td></tr><tr><td></td><td>districtID</td><td>string</td><td>required</td><td></td></tr><tr><td>author</td><td></td><td>string</td><td>required</td><td></td></tr><tr><td>dateCreated</td><td></td><td>date</td><td>required</td><td></td></tr><tr><td>lastUpdated</td><td></td><td>array</td><td>required</td><td></td></tr><tr><td>constraints</td><td></td><td>array of objects</td><td>required</td><td></td></tr><tr><td></td><td>constraintsModule</td><td>list</td><td>required</td><td></td></tr><tr><td></td><td>lot</td><td>object</td><td>required</td><td></td></tr></tbody></table>
