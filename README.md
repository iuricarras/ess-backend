# Hypervisor Cluster HA & LM Manager - Backend

**⚠️ Warning:** This code is an academic project and is not intended for production use.

This is the backend service for the Hypervisor Cluster HA & LM Manager. It provides user authentication, cluster management, and real-time communication via WebSockets between the frontend platform and the hypervisor clusters.

## Main Functionalities

- **User Authentication:**  
  - Sign up and log in with secure password hashing.
  - Token-based authentication for WebSocket connections.

- **Cluster Management:**  
  - Organize clusters into groups associated with users.
  - Add, remove, and query clusters by IP or session ID.
  - Manage cluster groups dynamically as clients connect/disconnect.

- **WebSocket Communication:**  
  - Real-time communication using Flask-SocketIO.
  - Secure connection with token validation.
  - Room-based messaging for user-specific cluster groups.
  - Acts as a bridge between the Vue.js interface and the hypervisor clusters by communicating with the daemons installed on the cluster networks.
  
- **REST API:**  
  - Endpoints for user signup and login.

## Installation

### Prerequisites

- Python 3.12+
- python3-virtualenv package (install with `sudo apt install python3-virtualenv` on Debian/Ubuntu)
- pip (comes bundled with recent Python versions)
- (Optional) [Nix](https://nixos.org/download.html) for reproducible development environments

### Clone the Repository

```sh
git clone https://github.com/iuricarras/ess-backend
cd ess-backend
```

### Install Dependencies

#### Using venv (recommended)

Create and activate a virtual environment:

```sh
python3 -m venv venv
source venv/bin/activate
```

Install all dependencies:

```sh
pip install -r requirements.txt
```

#### Using Nix (optional)

If you have Nix installed, you can enter a shell with all dependencies:

```sh
nix-shell
```

### Initialize the Database

The database will be automatically created on first run if it does not exist.

### Run the Application

```sh
flask run
```

## Frontend

For the frontend application, see: [ess-frontend](https://github.com/rodrigo-gom3s/ess-frontend)

## License

This project is licensed under the MIT License.