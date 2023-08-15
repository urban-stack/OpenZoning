/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: "jit",
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        bahnschrift: ["Bahnschrift", "sans-serif"], // Add a fallback font
        "ibm-plex-mono": ["IBM Plex Mono", "monospace"],
      },
      fontWeight: {
        350: 350,
        700: 700,
      },
      colors: {
        // black: "#212b36",
        "oz-green": "#165448",
      },

      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "gradient-conic":
          "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
      },
    },
  },
  plugins: [],
};
