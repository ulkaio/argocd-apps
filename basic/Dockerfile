# syntax=docker/dockerfile:1.4

# -------------------------------
# 1) Builder stage
# -------------------------------
    FROM --platform=$BUILDPLATFORM python:3.11-slim AS builder

    # Set working directory
    WORKDIR /app
    
    # Copy requirements
    COPY requirements.txt ./
    
    # Install build dependencies
    RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        && rm -rf /var/lib/apt/lists/*
    
    # Install Python packages
    RUN pip install --no-cache-dir -r requirements.txt
    
    # -------------------------------
    # 2) Final (runtime) stage
    # -------------------------------
    FROM --platform=$BUILDPLATFORM python:3.11-slim
    
    WORKDIR /app
    
    # Install only essential runtime packages
    RUN apt-get update && apt-get install -y --no-install-recommends \
        curl \
        && rm -rf /var/lib/apt/lists/*
    
    # Copy dependencies installed in builder stage
    COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
    COPY --from=builder /usr/local/bin/ /usr/local/bin/
    
    # Copy app source code
    COPY . .
    
    # Expose default Streamlit port
    EXPOSE 8501
    
    # Optional healthcheck for container orchestrators
    HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1
    
    # Run Streamlit server
    ENTRYPOINT ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]