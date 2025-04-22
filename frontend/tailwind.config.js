

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,ts,jsx,tsx,html}",
  ],
  theme: {
    extend: {
      colors: {
         lamaSky:"#c3ebfa",
         lamaSkyLight:"#edf9fd",
         lamaPurple:"#cfceff",
         lamaPurpleLight:"#f1f0ff",
         lamaYellow:"#fae27c",
         lamaYellowLight:"#fefceb"
      },
    },
  },
  plugins: [],
}
