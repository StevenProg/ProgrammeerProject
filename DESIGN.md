# Design Document

## Destination Picker

### Data 

- https://www.ecad.eu/dailydata/predefinedseries.php  deze link bevat de downloadlinks voor weer data van alle Europese steden, 
het format van de data is hetzelfde als de KNMI temperatuur data, dus ik kan die op soortgelijke manier verkrijgen. Als ik extra 
figuren wil toevoegen met andere weerdate (sneeuw bijvoorbeeld) kan dit ook.

- http://ec.europa.eu/eurostat/web/tourism/data/main-tables  deze link bevat de downloadlinks voor de reden van de reis/leeftijdsgroepen
die de reis maken, de data is beschikbaar in een TSV bestand, wat weer op een soortgelijke manier te verkrijgen is. Ik wil minstens 
één van deze 2 datasets gebruiken voor in de grouped barchart.

- Vliegtickets api? Anders auto -> dan enkel de afstand bereken naar verschillende steden (op basis van één van deze de kaart van Europa inkleuren)


### Diagram

![alt text](https://github.com/StevenProg/ProgrammeerProject/blob/master/Images/Proposal_Europe_Diagram.jpg)

### Technische overwiew

Allereerst wordt een main-functie uitgevoerd die alle visualisaties 'leeg' weergeeft. De main functie gaat vervolgens bij onclick-events de visualisaties updaten die upgedate moeten worden.

- -Het vakje linksboven in de diagram- Hiervoor moeten de 2 onderdelen geprogrammeerd worden om tussen landen te wisselen; de kaart van Europa, met behulp van TopoJSON, en de zoekbalk met aanvulling. Bij het laden van de pagina moeten beide manieren 'leeg' geinitialiseerd worden. Als een land op één van beide manieren een land is gekozen moet dit land worden ingekleurd op de kaart, en -het vakje linksonder in de diagram- en -het vakje rechtsboven in de diagram- worden upgedate met behulp van een update functie. 


### D3 plug-in List

- D3-Tip
- D3-Queue
- TopoJSON
