# RA-Monitor
# Preface
Resident Advisor is a platform for club promoters to sell tickets to their events. If an event is sold out and a ticket holder can no longer attend, they can list it to be resold and the ticket is put back in stock on the website. However, a major flaw is that a customer's only way of finding out if a ticket is in stock is to repeatedly check the website, which is a very frustrating and time-consuming process.
# Purpose
This is program which is designed to monitor sold out events on Resident Advisor (https://ra.co) and check for availability. If tickets are back in stock, a discord notification is sent to the user.

### Setup
- Currently only works with MacOS and Chrome 98
- run `make install` to install dependencies
- Insert link to event and discord webhook in config.json
- run `make` to run script
