# Security Policy

## Scope

`pubg-external-esp` is a **research / educational** external overlay toolkit.
It reads memory of a process you own for the purpose of studying external
overlay architecture. It intentionally does **not** include:

- anti-cheat bypasses
- kernel-mode drivers
- HWID / MAC spoofers
- packet manipulation
- injection into the target process

## Reporting

If you find a bug in the host (crash, memory leak, unsafe handle usage),
open a private security advisory. Do not open a public issue for anything
that could be weaponized.

## Disclaimer

Using this software against PUBG or any online game violates that game's
Terms of Service and may result in a permanent ban. The maintainers accept
no responsibility for misuse. Run it only against your own local test
process.