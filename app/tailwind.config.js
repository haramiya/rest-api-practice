module.exports = {
  purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      fontFamily: {
        body: ['Noto Sans JP']
        // body: ['Kiwi Maru']
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
