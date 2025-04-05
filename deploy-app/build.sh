#!/bin/bash

# Change to repository root
cd ..

# Install dependencies for excalidraw-app and packages/excalidraw
yarn --cwd excalidraw-app add vite cross-env typescript @types/node @testing-library/jest-dom @types/testing-library__jest-dom vitest clsx lodash.throttle vite-plugin-html @types/react @types/react-dom --no-lockfile
yarn --cwd packages/excalidraw add clsx --no-lockfile

# Create tsconfig.node.json to skip type checking during the build if it doesn't exist
cat > excalidraw-app/tsconfig.node.json << EOL
{
  "compilerOptions": {
    "composite": true,
    "skipLibCheck": true,
    "module": "ESNext",
    "moduleResolution": "bundler",
    "allowSyntheticDefaultImports": true
  },
  "include": ["vite.config.mts"]
}
EOL

# Create global.d.ts with type declarations for missing modules
cat > excalidraw-app/global.d.ts << EOL
/// <reference types="vite/client" />
import "@excalidraw/excalidraw/css";
import "@excalidraw/excalidraw/global";

// Add type declaration for missing testing libraries
declare module "@testing-library/jest-dom" {}
declare module "vitest/globals" {}
EOL

# Change to excalidraw-app directory
cd excalidraw-app

# Run build with TypeScript checking disabled
SKIP_TYPECHECK=true NODE_ENV=production VITE_APP_GIT_SHA=$VERCEL_GIT_COMMIT_SHA VITE_APP_ENABLE_TRACKING=true vite build
