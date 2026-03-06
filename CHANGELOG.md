## [unreleased]

### 🐛 Bug Fixes

- Change target attribute of navbar brand link to _self

### 🚜 Refactor

- Replace navbar and footer with new templates

### 📚 Documentation

- Update README for clarity and structure improvements
- Update README for clarity and add API documentation links

### ⚙️ Miscellaneous Tasks

- Update CHANGELOG for version 1.4.0 release
- Update images
## [1.4.0] - 2026-01-21

### ⚙️ Miscellaneous Tasks

- Update CHANGELOG for version 1.3.0 release
- Remove unused images
- Ignore Kiota generator files
- Bump to jQuery 4.0.0
- Drop jQuery3 script
- Update screenshot
- Update screenshot (code18)
- Add footer and update navbar links
- Update README
## [1.3.0] - 2025-11-11

### 🚀 Features

- Add scalar API reference endpoint and update entry point
- Add navbar template and integrate it into the UI layout

### 🚜 Refactor

- Update UI and button labels for clarity
- Update no content view
- Update navbar link

### ⚙️ Miscellaneous Tasks

- Add CHANGELOG for version 1.2.0
- Update CHANGELOG for unreleased changes
- Update stagedings UI image
- Add scalar-fastapi installation instruction to README
- Remove doc url instructions from README
## [1.2.0] - 2025-09-12

### 🚀 Features

- Add endpoint to switch to a direct scene/subscene, convert parameters to path variable, enhance descriptions
- Add LICENSE file with GPL-2.0-or-later terms
- Implement core controllers and models for Scene and OSC management
- Add .env file for environment configuration

### 🐛 Bug Fixes

- Update UI elements for better readability and consistency
- Update badge syntax for status in README
- Update badge link for project status in README
- Update README badges and improve project description
- Allow .env file
- Update README for clearer installation instructions and default server settings
- Enhance .env file with detailed comments for better clarity

### 🚜 Refactor

- Switch to pyliblo3
- Remove unused import of pyliblo3 from osc.py
- Update link texts for Swagger and Redoc documentation for clarity
- [**breaking**] Update API endpoints, use POST method and improve OpenAPI schema details
- Bump Bootstrap version to 5.38
- Bump Bootswatch Cyborg theme to v5.3.8
- Move .env as a template and ignore .env

### 📚 Documentation

- Update README to enhance installation instructions
- Update README to clarify repository cloning instructions
- Fix typos in REST API section of README
- Update README with correct server URL and API documentation link
- Update screenshot
- Update readme, add screenshots
- Add ecosystem diagram to documentation

### ⚙️ Miscellaneous Tasks

- Remove LICENSE file
## [1.1.0] - 2025-07-10

### 🚀 Features

- Load environment variables and configure WebSocket connection dynamically (#10)

### 🐛 Bug Fixes

- Adjust refresh key
- Invalid instruction
- Update WebSocket URL to point to production server

### 🚜 Refactor

- Implement new logic
- Remove the osc observer thread
- Reduce timeout
- SOC for Rest calls
- Use id as var name
- Remove/api/ in routes
- Robust connection manager
- *(ws)* Minor move
- [**breaking**] Scene/Subscene id are now query parameters
- Use app
- [**breaking**] Rename controller namespace
- Update template and structure
- Handle client disconnection properly + UI change
- Remove unused socket import from main.py

### 📚 Documentation

- Update readme
- Add summary to endpoints
- Configure open api spec for Kiota generator
- Update README to include features, dependencies, and licensing information
- Fix typo in features description in README
- Update README and index.html for improved clarity and links
- Enhance README with detailed project information and add UI preview image
- Update README to clarify project description and add python-dotenv dependency

### ⚙️ Miscellaneous Tasks

- Add static files
- *(ui)* Use static files
- *(ui)* Rework to get same layout as flaskdings
- Update configuration file
- Rename services class + move connection manager in a single file
- *(ui)* Use cyborg theme (wip)
- Invalid class name
- Bump Bootstrap and Bootswatch to v5.3.7
## [1.0.0] - 2023-12-28
