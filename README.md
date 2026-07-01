# Latent Guest Behavior Discovery for Intelligent Hotel Operations

## Overview

Latent Guest Behavior Discovery for Intelligent Hotel Operations is an AI-powered hospitality analytics platform that identifies hidden guest behavior patterns using unsupervised machine learning.

The system analyzes guest interactions across dining, wellness, recreation, family activities, business services, concierge requests, and operational services to discover natural guest archetypes. These insights help hotel management improve personalization, operational efficiency, resource allocation, and customer experience.

---

## Problem Statement

Modern hotels generate large volumes of guest interaction data but often struggle to extract meaningful behavioral insights.

Traditional rule-based segmentation approaches fail to capture complex guest preferences and service utilization patterns.

This project addresses the problem by:

* Discovering hidden guest behavior segments
* Predicting guest archetypes using clustering models
* Generating personalized recommendations
* Providing operational intelligence
* Delivering real-time analytics dashboards

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
* Real-time cluster prediction
* Personalized guest classification

### Recommendation Engine

* Personalized guest recommendations
* Service bundle suggestions
* Experience enhancement recommendations

### Operational Intelligence

* Resource allocation insights
* Staffing recommendations
* Service optimization suggestions

### Analytics Dashboard

* Total predictions summary
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
* PCA (Principal Component Analysis)
* K-Means Clustering
* StandardScaler

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

## Dataset

Hospitality guest activity dataset containing:

* Dining interactions
* Wellness services
* Family activities
* Business services
* Concierge interactions
* Operational requests

### Dataset Statistics

* Records: 102,432
* Original Features: 51
* Clustering Features: 19

---

## Feature Engineering

The final clustering model uses behavioral features including:

* Restaurant Visits
* Restaurant Spend
* Bar Lounge Visits
* Spa Treatments
* Spa Spend
* Gym Check-ins
* Pool Visits
* Activity Bookings
* Kids Club Sessions
* Tour Bookings
* Business Center Usage
* Concierge Requests
* Transport Requests
* Laundry Requests
* Service Complaints

### Engineered Features

* Total Dining Spend
* Total Wellness Usage
* Total Business Services
* Family Activity Score

---

## Machine Learning Workflow

### Data Preprocessing

* Missing value handling
* Feature selection
* Behavioral feature engineering
* Standard scaling

### Dimensionality Reduction

* Principal Component Analysis (PCA)
* 85% variance retention
* 9 principal components retained

### Clustering Model

Algorithm:

* PCA + K-Means Clustering

Final Hyperparameters:

* PCA Variance: 0.85
* PCA Components: 9
* K-Means Clusters: 6
* Random State: 42

### Model Performance

* Silhouette Score: 0.2341
* Davies-Bouldin Score: 1.4100
* Calinski-Harabasz Score: 23832.67

---

## Discovered Guest Segments

| Cluster | Guest Segment                  |
| ------- | ------------------------------ |
| 0       | Luxury Dining Guests           |
| 1       | Family Leisure Guests          |
| 2       | Wellness Luxury Guests         |
| 3       | Business Travelers             |
| 4       | Budget Minimal Guests          |
| 5       | Premium Family Business Guests |

---

## Model Artifacts

Generated model files:

* pca_kmeans_model.pkl
* pca_kmeans_scaler.pkl
* pca_transformer.pkl

---

## Association Rule Mining

The platform also performs association rule mining using Apriori to identify frequently co-occurring guest service usage patterns.

Examples:

* Restaurant + Bar Lounge
* Concierge + Transport
* Laundry + Business Center
* Spa + Gym

These patterns support recommendation generation and operational planning.

---

## System Architecture

```text
Guest Activity Data
        │
        ▼
Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Standard Scaling
        │
        ▼
PCA Transformation
        │
        ▼
K-Means Clustering Model
        │
        ├────────► Recommendation Engine
        │
        ├────────► Operational Insights
        │
        ├────────► Prediction History
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
├── clustering/
├── preprocessing/
├── association_rules/
├── recommendations/
├── database/
├── models/
├── static/
├── templates/
│
├── training_pipeline.py
├── main.py
│
└── data/
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

### History

```http
GET /history
```

---

## Frontend Pages

### Home

* Project Overview
* Statistics Cards

### Predict

* Guest Activity Input Form
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
* Cloud deployment
* Docker containerization
* CI/CD pipelines
* Advanced recommendation engine

---

## Learning Outcomes

* Unsupervised Machine Learning
* PCA for Dimensionality Reduction
* K-Means Clustering
* Guest Behavior Analytics
* FastAPI Development
* JWT Authentication
* PostgreSQL Integration
* Full Stack Development
* Recommendation Systems
* Analytics Dashboard Development

---

## Author

Developed as an end-to-end Machine Learning and Full Stack Hospitality Analytics Project using FastAPI, PostgreSQL, JavaScript, Chart.js, and Scikit-Learn.
