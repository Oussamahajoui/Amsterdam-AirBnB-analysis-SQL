# Amsterdam-AirBnB-analysis-SQL
 Analysis of Amsterdam AirBnb Listings 

## Problematic:
We wanted to check potential revenues of an Airbnb listing in Amsterdam, and gather a list of potential customers/target for a business idea.
The main goals:
1. Gather list of the top 100 highest revenues in Amsterdam within a full year
2. List of potential customers/target for a cleaning service business

## Data Source:
We leveraged **[Inside Airbnb](http://insideairbnb.com/get-the-data/ 'Inside Airbnb')** to gather data on available listings of Amsterdam in Airbnb.
We collected:
1. Listings
2. Calendar
3. Reviews

*Last available data set update used: 7 September 2022*

## Findings:
### Top 100 listings by revenues:

Following is a snippet with the top 5 listings (from top 100 list - *parsing full top 100 will cluster the page*):
|**listing_url**|	**Name/Title**	| **#days booked out of 365** |	**price ($)** |	**Projected revenues per year** |
| ------------- |:-------------:| -----:|:-------------:| -----:|
| https://www.airbnb.com/rooms/17421031|	Nice room in Amsterdam City|	365	|999|	364635
| https://www.airbnb.com/rooms/617378058167008775|	Loft with amazing views	|365	|800|	292000
| https://www.airbnb.com/rooms/708475499003098001|	Typical Amsterdam Canal View Apartment - Jordaan	|360|	650	|234000
| https://www.airbnb.com/rooms/39026851|	Stylish & Spacious apartment in Oud-West	|326	|680	|221680
| https://www.airbnb.com/rooms/619993167609846775|	Beautiful and cozy apartment - NEW	|365|	600|	219000


### Potential cleaning service customers:
Following is a snippet with the dirtiest 5 listings in Amsterdam that could use some cleaning service:
|**Host url**|	**Host Name**|	**Occurences of** *"dirty"* **in reviews**|
| -----:|:-------------:| -----:|
| https://www.airbnb.com/users/show/48158577	| Eva En Tommie |	12|
| https://www.airbnb.com/users/show/68338234	| Dries |	11|
| https://www.airbnb.com/users/show/245267147	| ClinkNOORD	|10|
| https://www.airbnb.com/users/show/251479377	| Generator	|10|
| https://www.airbnb.com/users/show/10697763	| Gianna	|8|





###### *Made by Oussama Hajoui*
