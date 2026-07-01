# CloudPulse

CloudPulse is a cloud infrastructure monitoring and log analytics platform built with Python. It continuously monitors system resources, collects application logs, stores historical data, and lays the foundation for intelligent monitoring and alerting.

## Features

### System Monitoring
- Real-time CPU usage monitoring
- Real-time memory usage monitoring
- Real-time disk usage monitoring
- Network statistics collection
- Hostname and timestamp tracking

### Historical Analytics
- Average CPU, Memory, and Disk usage
- Maximum CPU, Memory, and Disk usage
- Minimum CPU, Memory, and Disk usage
- Total records collected
- Latest metrics retrieval

### Database
- Automatic SQLite database creation
- Persistent storage of system metrics
- Persistent storage of log file offsets

### Log Collection
- Reads application log files
- Tracks file offsets using SQLite
- Reads only newly appended log entries
- Resumes log collection after application restart

### Monitoring Agent
- Continuous monitoring every 10 seconds
- Live console dashboard
- Automatic terminal refresh

## Technologies Used

- Python 3
- SQLite
- psutil
- Git
- GitHub

## Current Architecture

- Metrics Collector
- Log Collector
- SQLite Database Layer
- Analytics Layer
- Console Dashboard
- Utility Module

## Upcoming Features

- Log parsing
- Structured log storage
- Alert engine
- Streamlit dashboard
- Docker support
- AWS deployment
- Multi-server monitoring

## Project Status

! Active Development !

Current Version: **v0.5**