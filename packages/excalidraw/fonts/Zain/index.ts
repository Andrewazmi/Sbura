// Import font files
import { type ExcalidrawFontFaceDescriptor } from "../Fonts";

import ZainBlack from "./Zain-Black.woff2";
import ZainBold from "./Zain-Bold.woff2";
import ZainExtraBold from "./Zain-ExtraBold.woff2";
import ZainExtraLight from "./Zain-ExtraLight.woff2";
import ZainItalic from "./Zain-Italic.woff2";
import ZainLight from "./Zain-Light.woff2";
import ZainLightItalic from "./Zain-LightItalic.woff2";
import ZainRegular from "./Zain-Regular.woff2";

// Arabic unicode range
const ARABIC_UNICODE_RANGE =
  "U+0600-06FF, U+0750-077F, U+08A0-08FF, U+FB50-FDFF, U+FE70-FEFF";

export const ZainFontFaces: ExcalidrawFontFaceDescriptor[] = [
  {
    uri: ZainRegular,
    descriptors: {
      unicodeRange: ARABIC_UNICODE_RANGE,
      weight: "400",
    },
  },
  {
    uri: ZainBold,
    descriptors: {
      unicodeRange: ARABIC_UNICODE_RANGE,
      weight: "700",
    },
  },
  {
    uri: ZainLight,
    descriptors: {
      unicodeRange: ARABIC_UNICODE_RANGE,
      weight: "300",
    },
  },
  {
    uri: ZainExtraLight,
    descriptors: {
      unicodeRange: ARABIC_UNICODE_RANGE,
      weight: "200",
    },
  },
  {
    uri: ZainExtraBold,
    descriptors: {
      unicodeRange: ARABIC_UNICODE_RANGE,
      weight: "800",
    },
  },
  {
    uri: ZainBlack,
    descriptors: {
      unicodeRange: ARABIC_UNICODE_RANGE,
      weight: "900",
    },
  },
  {
    uri: ZainItalic,
    descriptors: {
      unicodeRange: ARABIC_UNICODE_RANGE,
      weight: "400",
      style: "italic",
    },
  },
  {
    uri: ZainLightItalic,
    descriptors: {
      unicodeRange: ARABIC_UNICODE_RANGE,
      weight: "300",
      style: "italic",
    },
  },
];
