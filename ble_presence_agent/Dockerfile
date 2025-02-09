FROM python:3.9-slim

# Build arguments for UID and GID
ARG USER_ID=1001
ARG GROUP_ID=1001

# Create group and user with the specified UID and GID
RUN groupadd -g ${GROUP_ID} bkam && \
    useradd -u ${USER_ID} -g bkam -m bkam

# Set working directory
WORKDIR /app

# Copy application code with ownership
COPY --chown=bkam:bkam . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Switch to the created user
USER bkam

# Default command
CMD ["python", "main.py"]
