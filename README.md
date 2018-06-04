# Project Proposal

## Destination Picker

### Problem Statement

Een goede vakantiebestemming kiezen kan lastig zijn, zeker wanneer er een grote diversiteit is aan eisen. Het mag bijvoorbeeld niet
te warm zijn maar ook niet te koud dus in welk seizoen kan ik het beste gaan, de vliegtickets mogen niet duurder zijn dan 700 euro etc. 
Om een goed beeld te krijgen moet je vaak veel verschilende pagina's afgaan en informatie uit al deze pagina's onthouden om een 
goed afgewogen keuze te maken.


### Solution
De proposal gaat over een visualisatie die de gebruiker gemakkelijk en duidelijk verschillende vakantie bestemmingen laat vergelijken
aan de hand van een wereldkaart, ondersteunt met verschillende grafieken over een aangeklikt land.

![alt text](https://github.com/StevenProg/ProgrammeerProject/blob/master/Proposal_Idea.jpg)


#### Main features: 
- Ticket prijzen vanaf Schiphol voor verschillende steden per land
- Informatie over bepaalde variabelen, zoals temperatuur, per land

#### Minimaal werkend product:
- Klikken op verschillende landen, waardoor je informatie over het land krijgt

### Prerequisites

#### Data sources:
- https://partners.skyscanner.net
- https://developer.schiphol.nl/
- http://www.weatherbase.com/weather/countryall.php3 (of vergelijkbaar)
- source voor andere variabele?

#### External components:
- D3 Library, D3-Tip, D3-Queue
- TopoJSON

#### Lastigste deel:
- Al de data verzamelen voor alle landen, oplossing: in plaats van de hele wereld -> een select aantal landen/enkel europa/enkel continenten?


Steven Schoenmaker (10777679)
