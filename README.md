# 🎹 stagedings
An API to navigate scenes and subscenes that has been configured in a [mididings](https://github.com/mididings) script

[![Core: mididings](https://img.shields.io/badge/core-mididings-blue)](https://github.com/mididings/mididings)
[![Backend: FastAPI](https://img.shields.io/badge/backend-FastAPI-green)](https://fastapi.tiangolo.com/)
[![Protocol: MIDI](https://img.shields.io/badge/protocol-MIDI-purple)](https://www.midi.org/specifications-old/item/table-1-summary-of-midi-message)
[![Protocol: OSC](https://img.shields.io/badge/protocol-OSC-purple)](http://opensoundcontrol.org/)
[![Protocol: WebSockets](https://img.shields.io/badge/protocol-WebSockets-purple)](https://fastapi.tiangolo.com/advanced/websockets/)
[![OpenAPI Spec](https://img.shields.io/badge/OpenAPI-Yes-green)](https://swagger.io/specification/)


---
### What does stagedings allow?
* A web-based interface
  * Alternative of the legacy **`livedings UI`**, which was based on Tkinter 🪓
* A HTTP layer that facilitates control and navigation allowing the abstraction of OSC subcalls
* An OpenAPI specification making possible to generate a client SDK in multiple language with a code  generator like [Kiota](https://github.com/microsoft/kiota) making possible to use the API in .NET, Go, Java, PHP, Python, Ruby and TypeScript.

⚠️ *A scene patch dictionary defined in the `run` section of your mididings script is required to work correctly, check the [`run` function documentation for more information](https://mididings.github.io/mididings/main.html#mididings.run) on how to structure your patch.*


## 📘 API documentation
- [stagedings endpoints](https://mididings.github.io/stagedings)
- [mididings manual](https://mididings.github.io/mididings)

## Frontend

### A responsive multiclient, real-time interface for scene/subscene navigation

<img src="docs/frontend.png" alt="stagedings UI screenshot" width="700"/>

---
## Features
- Web UI with real-time scene/subscene updates
- FastAPI backend with full REST and WebSocket support
- Multiple clients supported
- Use the mididings OSC interface
- It exposes a **fully compliant OpenAPI spec** for easy generation of SDK clients in any language, enabling flexible remote control of mididings

---

### The frontend allow
* Direct navigation through scenes and subscenes
* Exposes the Restart, Panic, Query and Quit commands

### The backend allow
* Endpoints for direct navigation through scenes and subscenes
* Endpoints to the Restart, Panic, Query and Quit commands

#### ℹ️ About commands
* ***Restart*** will restart mididings process
* ***Panic*** send not off to all ports and all channels
* ***Quit*** stop mididings, be carefull
* *Query is a work in progress*


---

## ⚒️ Installation & dependencies
#### On the server running mididings with OSC support
* Clone this repository
* In the stagedings/src directory
  * Create a .env file
    * Add the key STAGEDINGS_WS_HOST with the server name and the port of your choice:
      * STAGEDINGS_WS_HOST=localhost:5000

#### In a Python Virtual Environment
* mididings community >= **20250818** with OSC support 
  * See the mididings README for build instructions
* pip install fastapi
* pip install jinja2
* pip install uvicorn\[standard\]
## ▶️ Running the application
* In the stagedings/src directory
  
  * uvicorn main:app --port 5000 --host 0.0.0.0

* Then navigate to http://localhost:5000
## 🔗 Communication Workflow
<img src="docs/workflow.png" alt="stagedings UI screenshot" width="800"/>

### 💬 Feedback & Contributions

We welcome bug reports, feature ideas, and contributions! Please open an issue or discussion

### 📜 License

All files in this repository are released under the terms of the GNU
General Public License as published by the Free Software Foundation;
either version 2 or later of the License.

Made in 🇨🇦
