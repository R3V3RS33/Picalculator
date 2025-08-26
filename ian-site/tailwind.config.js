/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Montserrat", "sans-serif"],
        display: ["Playfair Display", "serif"],
      },
      colors: {
        charcoal: "#1c1c1c",
        gold: "#d4af37",
      },
    },
  },
  plugins: [],
};

