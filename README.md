# GPL EDMC Plugin

Das ist ein einfaches Plugin f�r den [ED MarketConnector](https://github.com/Marginal/EDMarketConnector/wiki) welches urspr�nglich einzig dem Zwecke diente den Einflu� der "German Pilot Lounge" sowie der eigenen Reputation (Ruf) bei dieser Fraktion anzuzeigen. Mittlwerweile habe ich dieses Plugin jedoch ein wenig erweitert ...

![In-game Screenshot](edmc_plugins_gpl.png)

![In-game Screenshot](edmc_plugins_dark.png)

![In-game Screenshot](edmc_plugins_light.png) ![In-game Screenshot](edmc_plugins_light_nocolor.png) 


## Installation

So wie auch alle anderen EDMC-Plugins wird der Ordner aus dem heruntergeladenen Archiv in den Plugin-Ordner eures EDMC's entpackt, das sollte danach dann in etwa so aussehen:
```
$AppPath$\EDMarketConnector\plugins\GPL
```
Nach dem starten des EDMC ist das Plugin sofort einsatzbereit, es ist bereits kompatibel mit der neuen BETA-Version des EDMC 3.50 beta0, funktioniert jedoch auch in der Version 3.43 des EDMC.


## Anzeigen

Je nach gew�hlten Optionen kann das Plugin folgendes anzeigen:
- Den Einflu� der Fraktion "German Pilot Lounge"
- Die eigene Reputation bei der Fraktion "German Pilot Lounge"
- S�mtliche Fraktionen welche im aktuellen System vertreten sind mitsamt des aktuellen Status und dem Anteil an Einflu� in Prozent


## Optionen

![EDMC Optionen](edmc_options_gpl.png)

### Optionen erkl�rt:

1. Zeige andere System Fraktionen
- schaltet die Anzeige aller im System vorhandenen Fraktionen mitsamt aktuellem Status und Einflu�anteil in Prozent ein oder aus

1. A. Zeige Fraktion 'Pilots' Federation Local Branch' in Fraktionsansicht
- schaltet die Anzeige der genannten Fraktion ein bzw aus
- - da diese Fraktion in jedem System vertreten ist und eigentlich immer 0% Einflu� hat ist dies normalerweise nicht notwendig, nur wer es m�chte der kann es sich damit aktivieren

2. Zeige zus�tzlichen Einflu� der GPL
- zeigt den Einflu� der GPL-Fraktion in einer zus�tzlichen zeile an
- dient eigentlich daf�r den Einflu� anzuzeigen auch wenn andere Fraktionen (Option 1) deaktiviert sind

3. Zeige eigene Reputation in der GPL
- zeigt den Spielereigenen Ruf bei der GPL-Fraktion an
- der eigene Ruf wird nur angezeigt wenn die GPL im aktuellen System vertreten ist, andernfalls wird es ausgeblendet

4. Zeige farbige Prozentwerte
- die Prozentwerte des Einflu�es werden zus�tzlich coloriert dargestellt wenn diese Option aktiviert ist, dies gilt f�r alle angezeigten Prozentwerte


5. Dunkles Design
- das Plugin erkennt nicht automatisch welches Design (Theme) man in EDMC aktiviert hat, weshalb es eine Optionsseite mit der M�glichkeit der Designwahl f�r das Plugin gibt.


## Weiteres

Dieses Plugin ist lediglich f�r eigene statistische Auswertungen gedacht und synchronisiert sich selbst in keinster Weise mit irgendwelchen anderen Plattformen.
F�r jene welche in anderen Sprachen spielen ist es m�glich weitere �bersetzungsdateien an zu legen, diese kommen dann ebenso wie die deutsche �bersetzung in den L10n Ordner innerhalb des Plugin-Ordners.
