# Changelog

All notable changes to this project will be documented in this file.

## 1.5.0 - 2026-06-13

### Bug Fixes

- update uvicorn dependency to include standard extras

### Documentation

- update CHANGELOG for version 1.4.2 release
- Update README for PyPI installation and improve image links #23

### Features

- Configure for PyPI (WIP) #23
- Add release-test target and script for package release process #23
- Add release script and update Makefile for package release process

### Miscellaneous Tasks

- Remove dead wood

### Refactor

- Remove dotenv (WIP) #23
- Ensure the port is the same for uvicorn and the websocket
- Remove the ws-host switch in favor of window.location.host

## 1.4.2 - 2026-05-25

### Documentation

- Update the excalidraw document and  images for the README

### Miscellaneous Tasks

- add git-cliff configuration for changelog generation

## 1.4.1 - 2026-05-20

### Bug Fixes

- change target attribute of navbar brand link to _self
- correct button label for next scene

### Documentation

- update README for clarity and structure improvements
- update README for clarity and add API documentation links
- Add overview diagram to documentation
- update CHANGELOG
- update README to remove unnecessary badges and clarify WS host configuration

### Miscellaneous Tasks

- Update CHANGELOG for version 1.4.0 release
- update images
- update CHANGELOG

### Refactor

- replace navbar and footer with new templates

## 1.4.0 - 2026-01-21

### Miscellaneous Tasks

- Update CHANGELOG for version 1.3.0 release
- Remove unused images
- Ignore Kiota generator files
- Bump to jQuery 4.0.0
- Drop jQuery3 script
- Update screenshot
- Update screenshot (code18)
- Add footer and update navbar links
- Update README

## 1.3.0 - 2025-11-11

### Features

- Add scalar API reference endpoint and update entry point
- Add navbar template and integrate it into the UI layout

### Miscellaneous Tasks

- Add CHANGELOG for version 1.2.0
- Update CHANGELOG for unreleased changes
- Update stagedings UI image
- Add scalar-fastapi installation instruction to README
- Remove doc url instructions from README

### Refactor

- Update UI and button labels for clarity
- Update no content view
- Update navbar link

## 1.2.0 - 2025-09-12

### Bug Fixes

- Update UI elements for better readability and consistency
- Update badge syntax for status in README
- Update badge link for project status in README
- Update README badges and improve project description
- Allow .env file
- Update README for clearer installation instructions and default server settings
- Enhance .env file with detailed comments for better clarity

### Documentation

- Update README to enhance installation instructions
- Update README to clarify repository cloning instructions
- Fix typos in REST API section of README
- Update README with correct server URL and API documentation link
- Update screenshot
- Update readme, add screenshots
- Add ecosystem diagram to documentation
- Update README.md

### Features

- Add endpoint to switch to a direct scene/subscene, convert parameters to path variable, enhance descriptions
- Add LICENSE file with GPL-2.0-or-later terms
- Implement core controllers and models for Scene and OSC management
- Add .env file for environment configuration

### Miscellaneous Tasks

- Remove LICENSE file

### Refactor

- Switch to pyliblo3
- Remove unused import of pyliblo3 from osc.py
- Update link texts for Swagger and Redoc documentation for clarity
- Update API endpoints, use POST method and improve OpenAPI schema details
- Bump Bootstrap version to 5.38
- Bump Bootswatch Cyborg theme to v5.3.8
- Move .env as a template and ignore .env

## 1.1.0 - 2025-07-10

### Bug Fixes

- Adjust refresh key
- Invalid instruction
- Update WebSocket URL to point to production server

### Documentation

- Update readme
- Add summary to endpoints
- Configure open api spec for Kiota generator
- Update README to include features, dependencies, and licensing information
- Fix typo in features description in README
- Update README and index.html for improved clarity and links
- Enhance README with detailed project information and add UI preview image
- Update README to clarify project description and add python-dotenv dependency

### Features

- Load environment variables and configure WebSocket connection dynamically (#10)

### Miscellaneous Tasks

- Add static files
- Use static files
- Rework to get same layout as flaskdings
- Update configuration file
- Rename services class + move connection manager in a single file
- Use cyborg theme (wip)
- Invalid class name
- Bump Bootstrap and Bootswatch to v5.3.7

### Refactor

- Implement new logic
- Remove the osc observer thread
- Reduce timeout
- SOC for Rest calls
- refactor : Use pydantic
- Use id as var name
- Remove/api/ in routes
- Robust connection manager
- Minor move
- Scene/Subscene id are now query parameters
- Use app
- Rename controller namespace
- Update template and structure
- Handle client disconnection properly + UI change
- Remove unused socket import from main.py

## 1.0.2 - 2024-03-21

### Other (unconventional)

- WIP sio
- Implement WebSocket ()
- Implement websockets

## 1.0.1 - 2024-03-21

### Other (unconventional)

- Render UI (wip)

## 1.0.0 - 2023-12-28

### Documentation

- Update README.md

### Other (unconventional)

- First commit
- WIP live osc
- Fix route syntax

<!-- generated by git-cliff -->
