# 🧪 Django CQRS Laboratory

## 📌 Description

This repository is focused on the **practical experimentation of the CQRS (Command Query Responsibility Segregation) architecture** using Django.

The main objective is to deeply understand:

- Separation between commands (write operations) and queries (read operations)
- Use of multiple databases
- Communication through a message broker
- Eventual consistency
- Deployment with Docker
- Lightweight distributed architecture

This project is not intended to be a production-ready system, but rather a learning laboratory.

---

## 🧠 What is CQRS?

CQRS (Command Query Responsibility Segregation) proposes separating:

- 🔴 **Commands** → Operations that modify the system state.
- 🔵 **Queries** → Operations that only read data.

In this laboratory, both logical and physical separation between these models will be implemented.

---

## 🏗 General Architecture

The system will consist of:

- `write-service` → Handles commands.
- `read-service` → Handles queries.
- `message-broker` → Event propagation.
- `write-database` → Database for write operations.
- `read-database` → Database optimized for read operations.
- (Optional) `event-store` → Historical record of system events.

---

## 🗄 Databases

| Role | Technology |
|------|------------|
| DB Command | PostgreSQL |
| DB Query | PostgreSQL |
| Event Store (optional) | PostgreSQL |

> Separate databases are used to simulate a real CQRS environment with eventual consistency.

---

## 📬 Service Communication

A message broker will be used for event propagation:

- RabbitMQ (pub/sub)

Expected flow:

1. The Write Service processes a command.
2. The state is saved in the Write DB.
3. An event is published.
4. The Read Service consumes the event.
5. The Read DB is updated.

---

## 🐳 Infrastructure

The project will be orchestrated using Docker Compose.

Expected services:

- write-service
- read-service
- rabbitmq
- write-db
- read-db

---

## 🎯 Learning Objectives

- Understand CQRS beyond theory.
- Learn about eventual consistency.
- Implement asynchronous communication between services.
- Learn Docker networking.
- Practice domain-oriented design.
- Improve discipline in Git versioning.

---

## Phases

 The laboratory is going to be composed in 3 phases:

 1- Understand CQRS concept -> a smaller sistem with less caracteristics
 2- Aply most complex caracteristics -> adding concepts like a message broker
 3- make a miniature CQRS system -> separating two services aplying the already covered concepts
  
---

## ⚠️ Notes

This project is experimental.  
It may evolve, change structure, or even break as part of the learning process.
