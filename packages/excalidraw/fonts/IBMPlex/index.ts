// Import font files
import { GOOGLE_FONTS_RANGES } from "@excalidraw/common";

import { type ExcalidrawFontFaceDescriptor } from "../Fonts";

import IBMPlexSansItalic from "./IBMPlexSans-Italic.woff2";
import IBMPlexSansRegular from "./IBMPlexSans-Regular.woff2";

export const IBMPlexFontFaces: ExcalidrawFontFaceDescriptor[] = [
  {
    uri: IBMPlexSansRegular,
    descriptors: {
      unicodeRange: `${GOOGLE_FONTS_RANGES.LATIN}, ${GOOGLE_FONTS_RANGES.ARABIC}`,
      weight: "400",
    },
  },
  {
    uri: IBMPlexSansItalic,
    descriptors: {
      unicodeRange: `${GOOGLE_FONTS_RANGES.LATIN}, ${GOOGLE_FONTS_RANGES.ARABIC}`,
      weight: "400",
      style: "italic",
    },
  },
];
