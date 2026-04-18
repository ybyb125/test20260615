# Custom Dockerfile to fix Yarn GPG key issue
FROM mcr.microsoft.com/devcontainers/dotnet:1-6.0

# Remove old Yarn source if present, then add the key and repo
RUN rm -f /etc/apt/sources.list.d/yarn.list \
    && apt-get update \
    && apt-get install -y curl gnupg \
    && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | gpg --dearmor | tee /usr/share/keyrings/yarnkey.gpg > /dev/null \
    && echo "deb [signed-by=/usr/share/keyrings/yarnkey.gpg] https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
