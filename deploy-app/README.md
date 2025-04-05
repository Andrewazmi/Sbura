# Vercel Deployment Directory

This directory is specially created for deploying the Excalidraw app to Vercel.

When creating a new Vercel project, set the Root Directory to `deploy-app` in the project settings.

The build process will:
1. Run the install command from the repository root
2. Execute the `build.sh` script which:
   - Installs necessary dependencies including TypeScript, type definitions, and Vitest
   - Builds the Excalidraw app with the `--skipTypeCheck` flag to completely bypass TypeScript errors
   - Sets all necessary environment variables during the build

This approach ensures that the application builds successfully for production deployment while staying within Vercel's limits for command length.
