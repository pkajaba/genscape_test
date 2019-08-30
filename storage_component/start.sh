#!/bin/bash
# wait until postgres is ready
sleep 10
alembic upgrade head
./app.py
