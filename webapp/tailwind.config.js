/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
        colors:{
          /* primary color */
          'violet': '#644ab4',
          'ocean' : '#002665',

          /* secondary color */
          'lavender' : '#bda5e1',
          'aqua' : '#9fd0f0'
      },
      fontFamily: {
        "nunito": ['Nunito', 'serif']
    }
    },
  },
  plugins: [require("@tailwindcss/forms")],
}
