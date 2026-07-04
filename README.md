# CloudPulse

CloudPulse is a Python-based cloud infrastructure monitoring and log analytics platform. It continuously monitors system resources, collects and parses application logs, stores historical data in SQLite, detects system alerts, and displays real-time information through a terminal dashboard.

## Features

### System Monitoring
- Real-time CPU monitoring
- Memory monitoring
- Disk monitoring
- Network statistics
- Hostname and timestamp collection

### Historical Analytics
- Average, Maximum, and Minimum CPU usage
- Average, Maximum, and Minimum Memory usage
- Average, Maximum, and Minimum Disk usage
- Total records collected

### Log Collection
- Incremental log collection using file offsets
- Persistent offset tracking
- Reads only newly appended log entries
- Automatic resume after restart

### Log Parsing
- Parses raw log lines into structured dictionaries
- Extracts timestamp, log level, and message

### Alert Engine
- CPU threshold alerts
- Memory threshold alerts
- Disk threshold alerts
- ERROR log detection
- Alert history stored in SQLite

### Configuration
- Centralized project settings
- Configurable polling interval
- Configurable alert thresholds
- Configurable dashboard history limits

### Database
- System metrics
- Application logs
- Log offsets
- Alert history

### Dashboard
- Live terminal monitoring
- Current system metrics
- Historical analytics
- Latest application logs
- Latest alerts

## Technologies

- Python
- SQLite
- psutil
- Git
- GitHub

## Current Version

**v0.8**