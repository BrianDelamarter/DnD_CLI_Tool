# Welcome to the DnD CLI Tool

This tool is designed to be a helpful addition to anyone playing DnD remotely. It is not designed
to run campaign or even fully track characters or other aspects of the game. The primary focus will
be a low distraction way to quickly get information and perform some quick actions rather than be
an all encompassing tool.

While it will hopefully prove helpful its primary function is to provide an opportunity to practice
and learn new programming skills.

## Required Packages

* requests
* terminaltexteffects
* pyfiglet

## API Details

API: [Open5e](https://open5e.com/)

The Open5e API provides programmatic access to all resources and rules included on this site. 

### Searching

To search the entire Open5e data-set, you can use the /search endpoint with the /query query parameter. 

`https://api.open5e.com/v2/search/?query=goblin`

### Filtering

Each resource can be filtered by a variety of properties. Some properties are common across all resource types, but many are specific to a given resource. 

`https://api.open5e.com/v2/creatures/?type=dragon`

### Field Selection

Visiting an Open5e API endpoint will typically return all the data associated with that entry. In most cases this will be overkill. The API is designed so that users can explicitly include or exclude the specific fields they require in their application so that their API classes execute as quickly as possible. 

Selecting:
`https://api.open5e.com/v2/creatures/?fields=name,key,document`
Exluding:
`https://api.open5e.com/v2/species/?exclude=traits`

### Ordering

By default Open5e returns API data sorted alphabetically (descending). The sort order can be changed by passing a ?ordering query parameter. 

`https://api.open5e.com/v2/creatures/?ordering=challenge_rating_decimal`
