# rock-paper-scissors

Takehome Assignment creating a little rock-paper-scissors game that saves game outcomes between players.

# About this project

A very basic browser game of Rock Paper Scissors built with Flask, Redis, and Docker.

# Getting Started

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [GitHub](https://www.github.com/)

## NOTE

If you are running this on a newer Mac with an Apple chip, you may need to change line 20 of docker-compose.yml to `    image: arm64v8/redis:6.2` in order to use a compatible redis image for your machine.

## QuickStart Commands

from you terminal type the following:

- `git clone <this branch name>`
- `cd rock-paper-scissors`
- `docker-compose up --build` to run tests and build
- open a web browser and navigate to http://localhost:8000/ to play!

## To run tests

`docker-compose run tests`

## To stop project

`docker-compose down`

# Assumptions/Concerns

The instructions said to allow the users to save their games but there was no guidance on if all games should be saved or what information should be saved, so I autosaved the running results of all games played by the same two first names. This is definitely brittle and could be improved, see below for some suggestions.

To make the game make any sense, I hid the users' rock/paper/scissors selection after they clicked on an option, otherwise it would be very easy for the second play to always win. This experience could definitely use some help from product/UX/a designer in general.

The instructions said to allow the player to play against the computer, so I treated the computer as a user named "Computer" in terms of saving these games. This definitely will cause problems/confusion if the second player enters the name "Computer," as that would be treated as a game against the computer and not a second player.

# Future Improvements

- Validation on form inputs - lengths and types for names, for instance
- Better (any) error handling
- Better (any) logging
- Improvements to the UX:
  - hide rock/paper/scissors selection but allow user to change it before submitting
  - prefill user names after initial game for ease of multiple rounds
  - allow users to request their saved game(s) by identifier
- Switch from `name1:name2` key to a better identifier
  - weird use cases like 2 players with same names, 2 games where players have same names as another game
- Add any UI styling (sorry I am truly a backend engineer when left on my own)
- Add auth to the one endpoint
- Add more tests
