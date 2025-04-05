#!/bin/bash

# Change to repository root
cd ..

# Install dependencies for excalidraw-app
yarn --cwd excalidraw-app add vite cross-env typescript @types/node @testing-library/jest-dom @types/testing-library__jest-dom vitest --no-lockfile

# Change to excalidraw-app directory
cd excalidraw-app

# Run build with TypeScript checking disabled
SKIP_TYPECHECK=true NODE_ENV=production VITE_APP_GIT_SHA=$VERCEL_GIT_COMMIT_SHA VITE_APP_ENABLE_TRACKING=true vite build --skipTypeCheck
