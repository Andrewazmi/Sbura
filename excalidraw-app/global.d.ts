/// <reference types="vite/client" />
import "@excalidraw/excalidraw/css";
import "@excalidraw/excalidraw/global";

// Add type declaration for missing testing libraries
declare module "@testing-library/jest-dom" {}
declare module "vitest/globals" {}

interface Window {
  __EXCALIDRAW_SHA__: string | undefined;
}
