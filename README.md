# Docker Project: Two-Container Communication

This repository demonstrates the basic concept of **Docker container communication** by creating two containers connected via a custom Docker bridge network:

1. **Server Container**: A Python-based web server that listens on port `8080` and responds with a message.
2. **Client Container**: A Python-based client that connects to the server and fetches its response.

---

## **Project Structure**

```
.
├── server
│   ├── Dockerfile         # Dockerfile for the server container
│   └── server.py          # Python web server script
├── client
│   ├── Dockerfile         # Dockerfile for the client container
│   └── client.py          # Python client script
└── README.md              # Project documentation
```

---

## **How It Works**

### **1. Server Container**
- Runs a Python-based web server (`server.py`) on port `8080`.
- Responds to HTTP GET requests with the message: `"Hello from Python!"`.

### **2. Client Container**
- Runs a Python program (`client.py`) that connects to the **Server Container** via the **Bridge Network**.
- Sends an HTTP request to the server and prints the response.

### **3. Bridge Network**
- A custom Docker network (`bridge`) allows the containers to communicate securely using their **container names**.

---

## **Setup Instructions**

### **Step 1: Clone the Repository**
```bash
git clone <repository-url>
cd <repository-directory>
```

### **Step 2: Pull Pre-Built Docker Images (Optional)**
If you prefer to skip building the images, you can directly pull the pre-built images from Docker Hub:

- **Server Container Image**:
  ```bash
  docker pull badal07/simple-python-server
  ```
- **Client Container Image**:
  ```bash
  docker pull badal07/simple-python-client
  ```

### **Step 3: Build the Server Container**
If you prefer to build locally, navigate to the `server/` directory:
```bash
cd server
```
Build the Docker image:
```bash
docker build -t simple-python-server .
```

### **Step 4: Build the Client Container**
Navigate to the `client/` directory:
```bash
cd ../client
```
Build the Docker image:
```bash
docker build -t simple-python-client .
```

### **Step 5: Create a Custom Network**
Create a Docker bridge network to enable container communication:
```bash
docker network create simple-network
```

### **Step 6: Run the Server Container**
Start the server container and attach it to the custom network:
```bash
docker run -d --name server-container --network simple-network -p 8080:8080 simple-python-server
```

### **Step 7: Run the Client Container**
Start the client container and attach it to the same network:
```bash
docker run --rm --name client-container --network simple-network simple-python-client
```

---

## **Expected Output**
When the client container runs, it fetches the response from the server container and prints it:

```plaintext
Response from server: Hello from Python!
```

---

## **Diagram**

```
  Bridge Network
  +----------------------------------------+
  |                                        |
  |                                        |
  |        +------------------+            |
  |        |                  |            |
  |        |  Server Container|            |
  |        |  Python Web App  |            |
  |        |  (Port: 8080)    |            |
  |        +------------------+            |
  |                |                         |
  |                |                         |
  |        +------------------+            |
  |        |                  |            |
  |        |  Client Container|            |
  |        |  Python Program  |            |
  |        |                  |            |
  |        +------------------+            |
  |                                        |
  +----------------------------------------+
```

---

## **Key Concepts Learned**

1. **Container Communication**:
   - Using a custom Docker bridge network for seamless communication.

2. **Separation of Concerns**:
   - The server serves requests, while the client makes requests.

3. **Lightweight Use Case**:
   - Demonstrates a real-world-like container interaction without complexity.

---

## **Future Enhancements**
- Add logging to monitor container communication.
- Extend the project to include persistent data storage (e.g., database).
- Transition to a Docker Compose setup for easier management.
---

## **Contributions**
Contributions are welcome! Please fork the repository and submit a pull request for review.
