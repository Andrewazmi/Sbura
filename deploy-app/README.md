# Vercel Deployment Directory

This directory is specially created for deploying the Excalidraw app to Vercel.

When creating a new Vercel project, set the Root Directory to `deploy-app` in the project settings.

The build process will:
1. Run the install command from the repository root
2. Build the Excalidraw app located in `../excalidraw-app`
3. Use the build output from `../excalidraw-app/build`

This approach ensures that the correct directories are used during deployment.
