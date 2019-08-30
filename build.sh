#!/bin/bash
docker build -f Dockerfile.storage -t image/storage .  
docker build -f Dockerfile.sensor -t image/sensor .  
docker build -f Dockerfile.ingestion -t image/ingestion .
docker build -f Dockerfile.grafana -t custom/grafana .
