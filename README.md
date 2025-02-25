# Medicine Shop App

This repository contains a microservices-based Medicine Shop Application.

## Structure

- **frontend/**: Contains the React-based frontend.
- **backend/**: Contains the microservices for the backend including:
  - API Gateway
  - Authentication Service
  - User Account Service
  - Item Catalog Service
  - Order Management Service
  - Ledger Service
  - Reporting Service
  - Campaign Service
  - Geo-Tagging Service
  - Customer Connect Service
  - Inventory Service
  - Customer Profile Service
  - Common utilities

## Running Locally

### Frontend
1. Navigate to the `frontend/` directory.
2. Run `npm install` to install dependencies.
3. Run `npm start` to launch the development server.

### Backend
1. Navigate to the `backend/` directory.
2. Run `docker-compose up --build` to build and run all services.
   This will start the API gateway, all microservices, and a Redis instance for caching.

## Testing

Each microservice includes a `tests/` directory with sample tests.
For example, to run tests for the API Gateway, navigate to `backend/api-gateway/` and run:
pytest

bash
Copy

## Deployment

This application is fully dockerized and can be deployed to Google Cloud VMs.
Ensure that Docker and Docker Compose are installed on your deployment host.

## ADA Compliance

The frontend has been developed with ADA compliance in mind, using semantic HTML, proper ARIA attributes, and accessible form elements.

## License

MIT License.
