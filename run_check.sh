#!/bin/bash

# 1. Load the .env file (if it exists)
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

# 2. Define the variables we need
REQUIRED_VARS=("SUPABASE_URL" "SUPABASE_KEY")

# 3. Iterate and validate
for var in "${REQUIRED_VARS[@]}"; do
    if [ -z "${!var}" ]; then
        echo "❌ Error: Environment variable $var is not set."
        exit 1
    fi
done

# 4. If we passed, run the node script
echo "✅ Environment verified. Running connection check..."
node check_conn.mjs