#!/bin/bash

# Star server
echo "Starting server..."
uvicorn app.main:app --host "0.0.0.0" --port "8080" --reload