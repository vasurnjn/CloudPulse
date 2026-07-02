# CloudPulse

CloudPulse is a Python-based cloud infrastructure monitoring and log analytics platform. It continuously monitors system resources, collects application logs, parses them into structured data, stores everything in SQLite, and provides real-time monitoring through a terminal dashboard.

## Features

### System Monitoring
- Real-time CPU usage monitoring
- Memory usage monitoring
- Disk usage monitoring
- Network usage monitoring
- Hostname and timestamp collection

### Historical Analytics
- Average CPU, Memory, and Disk usage
- Maximum CPU, Memory, and Disk usage
- Minimum CPU, Memory, and Disk usage
- Total metrics collected

### Log Collection
- Incremental log collection using file offsets
- Persistent offset tracking
- Resume log collection after restart
- Reads only newly appended log entries

### Log Parsing
- Parses raw log lines into structured dictionaries
- Extracts timestamp
- Extracts log level
- Extracts log message

### Database
- SQLite storage for system metrics
- SQLite storage for parsed application logs
- SQLite storage for collector offsets

### Dashboard
- Live terminal dashboard
- Historical metrics
- Latest parsed application logs

## Technologies

- Python
- SQLite
- psutil
- Git
- GitHub

## Project Structure

- Metrics Collector
- Log Collector
- Log Parser
- Analytics Layer
- Database Layer
- Console Dashboard
- Utility Module

## Upcoming Features

- Alert Engine
- Log Filtering
- Streamlit Dashboard
- Docker Support
- AWS Deployment
- Multi-server Monitoring

## Current Version

**v0.6**