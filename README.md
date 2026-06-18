# Latent Guest Behavior Discovery for Intelligent Hotel Operations

## Overview

Latent Guest Behavior Discovery for Intelligent Hotel Operations is an AI-powered hospitality analytics platform designed to uncover hidden guest behavior patterns using unsupervised machine learning techniques.

The system analyzes guest interaction data across hotel services such as dining, wellness, recreation, concierge, and operational services to identify natural guest archetypes. These insights help hotel management improve personalization, resource allocation, service quality, and operational efficiency.

---

## Problem Statement

Modern hotels collect large volumes of guest activity data but often lack the ability to identify meaningful behavioral patterns.

Traditional rule-based segmentation fails to capture complex guest preferences and service utilization trends.

This project addresses the problem by:

* Discovering hidden guest behavior segments
* Predicting guest archetypes using trained clustering models
* Generating personalized recommendations
* Providing operational insights for hotel management
* Offering an interactive analytics dashboard

---

## Features

### Authentication & Security

* User Registration
* User Login
* JWT Authentication
* Password Hashing using Bcrypt
* Protected API Endpoints
* Session Management

### Guest Behavior Prediction

* Predict guest segment using activity data
* Confidence score generation
* Real-time prediction results
* Cluster identification

### Recommendation Engine

* Personalized guest recommendations
* Service bundle suggestions
* Experience enhancement recommendations

### Operational Intelligence

* Resource allocation recommendations
* Staff planning insights
* Service optimization suggestions

### Analytics Dashboard

* Total predictions summary
* Average confidence tracking
* Cluster distribution visualization
* Recent prediction monitoring

### Prediction History

* Historical prediction tracking
* Search functionality
* Pagination support
* Timestamp-based records

---

## Technology Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic
* JWT Authentication

### Machine Learning

* Scikit-Learn
* Gaussian Mixture Models (GMM)
* K-Means Clustering
* StandardScaler
* LabelEncoder

### Data Processing

* Pandas
* NumPy

### Association Rule Mining

* Mlxtend
* Apriori Algorithm
* Association Rules

### Frontend

* HTML5
* CSS3
* JavaScript
* Jinja2 Templates
* Chart.js

---

## Machine Learning Workflow

### Data Collection

Hospitality guest activity dataset containing:

* Dining interactions
* Wellness service usage
* Family activities
* Business services
* Concierge interactions
* Special requests

Dataset Size:

* 102,432 Records
* 17 Behavioral Features

---

### Feature Engineering

Selected features include:

* Restaurant visits
* Restaurant spend
* Room service orders
* Spa usage
* Gym check-ins
* Pool visits
* Activity bookings
* Concierge requests
* Laundry requests
* Transport requests
* Special requests
* Service complaints

---

### Clustering Model

Algorithm:

* Gaussian Mixture Model (GMM)

Model Artifacts:

* gmm_guest_clustering_model.pkl
* clustering_scaler.pkl

Discovered Guest Segments:

| Cluster | Guest Archetype         |
| ------- | ----------------------- |
| 0       | Luxury Wellness Guests  |
| 1       | Business Leisure Guests |
| 2       | Family Dining Guests    |
| 3       | Budget Minimal Guests   |

---

## System Architecture

```text
Guest Activity Data
        │
        ▼
Preprocessing
        │
        ▼
Feature Scaling
        │
        ▼
GMM Clustering Model
        │
        ▼
Cluster Prediction
        │
        ├────────► Recommendation Engine
        │
        ├────────► Operational Insights
        │
        └────────► Analytics Dashboard
```

---

## Project Structure

```text
app/
│
├── api/
│   ├── routes/
│   ├── schemas/
│   └── services/
│
├── database/
│
├── models/
│
├── templates/
│
├── static/
│
├── clustering/
│
├── preprocessing/
│
├── recommendations/
│
└── main.py
```

---

## Database Schema

### User Table

Stores:

* User ID
* Name
* Email
* Hashed Password
* Created Timestamp

### Prediction History Table

Stores:

* Cluster ID
* Cluster Name
* Confidence Score
* Guest Activity Features
* Prediction Timestamp

---

## API Endpoints

### Authentication

```http
POST /register
POST /login
```

### Prediction

```http
POST /predict-cluster
```

### Analytics

```http
GET /analytics/summary
GET /analytics/cluster-distribution
GET /analytics/recent-predictions
```

---

## Frontend Pages

### Home

* Project Overview
* Statistics Cards

### Predict

* Guest Activity Form
* Prediction Results
* Recommendations
* Operational Insights

### Analytics

* Dashboard Metrics
* Cluster Distribution Chart
* Recent Predictions

### History

* Prediction Records
* Search
* Pagination

### About

* Project Overview
* Feature Highlights

---

## Future Enhancements

* User-specific prediction history
* Role-based access control
* Real-time analytics updates
* Multi-property hotel support
* Advanced recommendation engine
* Cloud deployment
* CI/CD integration
* Docker containerization

---

## Learning Outcomes

* Unsupervised Machine Learning
* Guest Behavior Analytics
* FastAPI Development
* JWT Authentication
* PostgreSQL Integration
* Full Stack Development
* Analytics Dashboard Design
* Recommendation Systems

---

## Author

Developed as an end-to-end Machine Learning and Full Stack Hospitality Analytics Project using FastAPI, PostgreSQL, JavaScript, and Scikit-Learn.
