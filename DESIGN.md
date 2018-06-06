# Design Document

## Destination Picker (Steven Schoenmaker 10777679)

### Data 

- https://www.ecad.eu/dailydata/predefinedseries.php  deze link bevat de downloadlinks voor weer data van alle Europese steden, 
het format van de data is hetzelfde als de KNMI temperatuur data, dus ik kan die op soortgelijke manier verkrijgen. Als ik extra 
figuren wil toevoegen met andere weerdate (sneeuw bijvoorbeeld) kan dit ook.

- http://ec.europa.eu/eurostat/web/tourism/data/main-tables  deze link bevat de downloadlinks voor de reden van de reis/leeftijdsgroepen
die de reis maken, de data is beschikbaar in een TSV bestand, wat weer op een soortgelijke manier te verkrijgen is. Ik wil minstens 
één van deze 2 datasets gebruiken voor in de grouped barchart.

- Vliegtickets api? Anders auto -> dan enkel de afstand bereken naar verschillende steden (op basis van één van deze de kaart van Europa inkleuren)

- https://github.com/leakyMirror/map-of-europe deze link bevat de data om de kaart van Europa in te laden met behulp van topoJSON


### Diagram

![alt text](https://github.com/StevenProg/ProgrammeerProject/blob/master/Images/Proposal_Europe_Diagram.jpg)

### Technische overview

Allereerst wordt een main-functie uitgevoerd die alle visualisaties 'leeg' weergeeft. Hiervoor moet de data van de kaart van Europa worden ingeladen en alle namen van de landen in Europa. De main functie gaat vervolgens bij onclick-events de visualisaties updaten die upgedate moeten worden.

- -Het vakje linksboven in de diagram- Hiervoor moeten de 2 onderdelen geprogrammeerd worden om tussen landen te wisselen; de kaart van Europa, met behulp van TopoJSON, en de zoekbalk met aanvulling. Bij het laden van de pagina moeten beide manieren 'leeg' geinitialiseerd worden. Als een land op één van beide manieren een land is gekozen moet dit land worden ingekleurd op de kaart, en -het vakje linksonder in de diagram- en -het vakje rechtsboven in de diagram- worden upgedate met behulp van een update functie. Op het moment dat de gebruik zijn muis hoovert over een land, zal dit land oplichten.

- -Het vakje rechtsboven in de diagram- Voordat dit vakje invulling kan krijgen moet er eerst een land worden gekozen. Hij gaat dus 'leeg' geinitialiseerd worden, met een dropdown menu zonder data. Op het moment dat een ander land geselecteerd is zal de informatie over de goedkoopste reis naar het bepaald land bovenaan geschreven worden. Het dropdown menu krijgt ook een invulling met reisopties naar andere locaties van het gekozen land. Na elke switch van bestemmings-land zal de data van deze gehele visualisatie moet worden upgedate. Als een bepaalde locatie is gekozen door te klikken op een optie in het dropdown menu zal de grouped barchart worden upgedate. Op het moment dat de gebruik zijn muis hoovert over een optie, zal dit deze optie een donkere achtergrond krijgen.

- -Het vakje linksonder in de diagram- Voordat dit vakje invulling kan krijgen moet er eerst een land worden gekozen. Hij gaat dus 'leeg' geinitialiseerd worden, met een grafiek zonder data. De X-as kan wel al worden geschreven, aangezien de maanden niet veranderen, de y-as kan wel variëren qua schaal. Op het moment dat een ander land geselecteerd is zal de grafiek invulling krijgen met weer data over het bepaalde land. Het is de bedoeling dat de grafiek een soortgelijke functionaliteit krijgt als de multiline van het vak data-processing, zoals de hover-over effects. Deze grafiek kan niet worden gebruikt om andere visualisaties te updaten.

- -Het vakje rechtsonder in de diagram- Voordat dit vakje invulling kan krijgen moet er eerst een stad worden gekozen. Hij gaat dus 'leeg' geinitialiseerd worden, met een grafiek zonder data. De Y-as kan wel al worden geschreven, aangezien het een schaal van 0 naar 100% is, de x-as hangt af van de keuze van de gebruiker. Om het moment dat er een stad is gekozen in -het vakje rechtsboven in de diagram- zal de keuze worden toegevoegd aan de grouped barchart, ook als er al data in staat. Op deze manier kan de gebruiker de keuzes vergelijken. In de grouped barchart wordt dan de leeftijds-gerelateerde data ingeladen van de gekozen stad. Als er wordt geklikt 
op een gekozen stad zullen de 3 andere 'diagram vakjes' (linksboven, rechtsboven en rechtsonder) weer worden upgedate alsof het land waar die stad in ligt aangeklikt zou zijn. Op het moment dat de gebruik zijn muis hoovert over een grouped bar, zal het bijbehorende land in de kaart van Europa oplichten.
### D3 plug-in List

- D3-Tip
- D3-Queue
- TopoJSON
