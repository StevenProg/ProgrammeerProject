# Project Proposal

## Destination Picker

### Problem Statement

Een goede vakantiebestemming kiezen kan lastig zijn, zeker wanneer er een grote diversiteit is aan eisen. Het mag bijvoorbeeld niet
te warm zijn maar ook niet te koud dus in welk seizoen kan ik het beste gaan, de vliegtickets mogen niet duurder zijn dan 700 euro etc. 
Om een goed beeld te krijgen moet je vaak veel verschilende pagina's afgaan en informatie uit al deze pagina's onthouden om een 
goed afgewogen keuze te maken.


### Solution
De proposal gaat over een visualisatie die de gebruiker gemakkelijk en duidelijk verschillende vakantie bestemmingen laat vergelijken
aan de hand van een kaart van Europa, ondersteunt met verschillende grafieken over een aangeklikt land.

![alt text](https://github.com/StevenProg/ProgrammeerProject/blob/master/Proposal_Europe.jpg)

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

#### Vergelijkbare sites:
- https://www.vliegtickets.nl/?gclid=EAIaIQobChMI-r3e6ZK62wIVBTPTCh0yvAYrEAAYASAAEgLDCvD_BwE&gclsrc=aw.ds&dclid=CJyN8OqSutsCFViWdwodlgUH9Q
Het nadeel aan dit soort sites is het langzaam navigeren en informatie verwerving tussen verschillende landen

#### Lastigste deel:
- Al de data verzamelen voor de vliegtickets vanuit Schiphol (handmatig?)
#### Toevoegingen:
- Favorieten bewaren -> snel vergelijken?

Steven Schoenmaker (10777679)
