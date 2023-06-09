# TicTacToe

Sovellus on Ristinolla peli jota pelaa kaksi pelaajaa paikallisesti yhdellä koneella. Sovellusta on tarokitus myös laajentaa isomman kokoiseen ristinolla peliin, eli 4x4, 5x5 jne.


### Dokumentaatio 

* [Vaatimusmäärittely](https://github.com/modaralgayal/ot-harjoitustyo/blob/master/TicTacToe/dokumentaatio/vaatimusmaarittely.md)
* [Changelog](https://github.com/modaralgayal/ot-harjoitustyo/blob/master/TicTacToe/dokumentaatio/changelog.md)
* [Arkkitehtuurikuvaus](https://github.com/modaralgayal/ot-harjoitustyo/blob/master/TicTacToe/dokumentaatio/arkkitehtuuri.md)
* [Työaikakirjanpito](https://github.com/modaralgayal/ot-harjoitustyo/blob/master/TicTacToe/dokumentaatio/Tuntikirjanpito.md)


### Release

* [Ohjelma](https://github.com/modaralgayal/ot-harjoitustyo/releases/tag/Release)


### Ohjelman asennus ja ajaminen Poetrylla

* Asenna riippuvuudet komennolla:

```bash
poetry install
```

* Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```


### Komentorivitoiminnot

#### Ohjelman suorittaminen

* Ohjelman käynnistäminen komennolla:

```bash
poetry run invoke start
```


#### Testaus

* Ohjelman testaaminen komennolla:

```bash
poetry run invoke test
```


#### Testikattavuus

* Ohjelman testikattavuus komennolla:

```bash
poetry run invoke coverage-report
```


#### Pylint

* Ohjelman laadun testaaminen komennolla:

```bash
poetry run invoke lint
```
