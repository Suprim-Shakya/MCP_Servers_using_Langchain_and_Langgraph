# MCP_Servers_using_Langchain_and_Langgraph

## Project Description

This project implements multiple servers using Langchain and Langgraph technologies. It provides various functionalities through different Python modules such as client, main server logic, math server, and weather server. The project aims to demonstrate the integration of Langchain and Langgraph for building modular and scalable server applications.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd MCP_Servers_using_Langchain_and_Langgraph
   ```
3. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirement.txt
   ```

## Usage

- To run the main server:
  ```bash
  python main.py
  ```
- To run the client:
  ```bash
  python client.py
  ```
- To run the math server:
  ```bash
  python mathserver.py
  ```
- To run the weather server:
  ```bash
  python weather.py
  ```

## Features

- Modular server architecture using Langchain and Langgraph
- Separate servers for different functionalities (math, weather, etc.)
- Easy to extend and integrate new services

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes and commit (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

## License

This project is licensed under the MIT License. See the LICENSE file for details.
