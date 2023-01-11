/** @type {import('tailwindcss').Config} */
const colors = require("tailwindcss/colors");

module.exports = {
  content: [
    "./src/components/*.{js,jsx,ts,tsx}",
    "./src/components/**/*.{js,jsx,ts,tsx}",
    "./src/components/**/**/*.{js,jsx,ts,tsx}",
    "./src/pages/*.{js,jsx,ts,tsx}",
    "./src/**/*.{js,jsx,ts,tsx}",
    "./index.html",
  ],
  theme: {
    extend: {
      colors: {
        // custom color palette
        // gray, zinc, stone, slate
        // stone, red, orange, yellow, emerald
        // teal, blue, indigo, purple
        // all from tailwind

        primary: {
          primary: "#441151",
          50: "#f9f5f0",
          100: "#f3eae1",
          200: "#f3eae1",
          300: "#e7d6c4",
          400: "#e1ccb5",
          500: "#dbc1a6",
          600: "#d5b797",
          700: "#cfad89",
          800: "#c9a27a",
          900: "#171717",
        },
        tags: {
          lg: "#065F46",
        },
        gold: {
          DEFAULT: "#c3986b",
          50: "#fafafa",
          100: "#f5f5f5",
          200: "#e5e5e5",
          300: "#d4d4d4",
          400: "#a3a3a3",
          500: "#737373",
          600: "#525252",
          700: "#404040",
          800: "#262626",
          900: "#171717",
        },
        neutral: {
          50: "#fafafa",
          100: "#f5f5f5",
          200: "#e5e5e5",
          300: "#d4d4d4",
          400: "#a3a3a3",
          500: "#737373",
          600: "#525252",
          700: "#404040",
          800: "#262626",
          900: "#171717",
        },
        grey: {
          1: "#FAFAFA",
          2: "#C0C6D4",
          3: "#F7F8FD",
        },
        darkgold: "#C3986B",
        secondary: "#EE85B5",
        background: "#FAFAFA",
        violet: "#883677",
        congo: "##FF958C",
        success: "#5FC790",
        warning: "#FFA600",
        danger: "#FF5630",
        dark: "#2E3A44",
        info: "#1CA7EC",
        light: "#F9FBFC",
        card: {
          DEFAULT: "#F9F9F9",
          divider: "#EAEAEB",
          text: "#3c3a38",
          grey: "#707070",
        },
      },
    },
    fontFamily: {
      // add new font family
      main: ["Alliance No 2"],
      alliance: ["Alliance No 2", "sans-serif"],
      arimo: ["Arimo", "sans-serif"],
    },

    screens: {
      sm: "640px",
      md: "768px",
      xl: "1280px",
      xxl: "2500px",
    },
    spacing: {
      2: "4px",
      4: "8px",
      6: "12px",
      8: "16px",
      10: "20px",
      12: "24px",
      14: "28px",
      16: "32px",
      18: "36px",
      20: "40px",
      22: "44px",
      24: "48px",
      28: "56px",
      32: "64px",
      40: "80px",
      48: "96px",
      56: "112px",
      64: "128px",
      72: "144px",
      80: "160px",
      88: "176px",
      96: "192px",
      104: "208px",
      112: "224px",
      120: "240px",
      128: "256px",
      144: "288px",
      160: "320px",
      192: "384px",
    },
  },
  plugins: [],
};
